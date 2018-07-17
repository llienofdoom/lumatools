import settings.luma_site_settings
import os, sys
import hou

###############################################################################
g_jobIFD = {
    "name"     : "",
    "priority" : 9,
    "rop"      : "/out/rop_hm_base",
    "frames"   : "1-100",
    "files"    : "",
    "outdir"   : ""
}
g_jobEXR = {
    "name"     : "IFD-REN - TESTING",
    "priority" : 5,
    "files"    : "",
    "outdir"   : "",
    "dep"      : 0
}

###############################################################################
def buildCmdLineIFD(l_job):
    rpcmd = '"' + os.environ['RP_CMDRC_DIR'] + 'RpRcCmd.exe"'
    cmd = rpcmd
    cmd += ' -nj_name "%s"' % (l_job['name'])
    cmd += ' -nj_priority %d' % (l_job['priority'])
    cmd += ' -nj_renderer GenerateIFD/16.5.473'
    cmd += ' -nj_splitmode 2,1'
    cmd += ' -nj_pools "mantra"'
    cmd += ' -nj_paused'
    cmd += ' -retnjid'
    cmd += ' -rop "%s"' % (l_job['rop'])
    cmd += ' -frames "%s"' % (l_job['frames'])
    cmd += ' -outdir "%s"' % (l_job['outdir'])
    cmd += ' %s' % (l_job['files'])
    print cmd
    njid = os.system('"' + cmd + '"')
    return njid

def buildCmdLineEXR(l_job):
    rpcmd = '"' + os.environ['RP_CMDRC_DIR'] + 'RpRcCmd.exe"'
    cmd = rpcmd
    cmd += ' "-nj_name" "%s"' % (l_job['name'])
    cmd += ' "-nj_priority" "%d"' % (l_job['priority'])
    cmd += ' "-nj_renderer" "RenderEXR/16.5.473"'
    cmd += ' "-nj_splitmode" "2,1"'
    cmd += ' "-nj_pools" "mantra"'
    cmd += ' "-nj_dependency" "%d"' % (l_job['dep'])
    cmd += ' "-nj_deptype" "0"'
    cmd += ' "-nj_paused"'
    cmd += ' "-outdir" "%s"' % (l_job['outdir'])
    cmd += ' %s' % (l_job['files'])
    print cmd
    tempfile_path = os.environ['TEMP'] + os.sep + '___cmd.bat'
    tempfile = open(tempfile_path, 'w')
    tempfile.write(cmd)
    tempfile.close()
    os.system( tempfile_path )
    os.remove(tempfile_path)


###############################################################################
def main():
    if (len(sys.argv) != 2):
        exit(1)

    global g_jobIFD, g_jobEXR
    print 'Loading File...',
    hou.hipFile.load(sys.argv[1], ignore_load_warnings=True)
    print 'DONE!'
    rop_list = []
    rop_out = hou.node("/out/OUT")
    rop_children = rop_out.inputAncestors()
    for child in rop_children:
        type = child.type().name()
        if type == 'ifd':
            rop_list.append(child)
    for rop in rop_list:
        parm_diskName      = os.path.basename(hou.parm(rop.path() + '/soho_diskfile').eval()).split('.')[0]
        parm_outputDir_IFD = os.path.dirname(hou.parm(rop.path() + '/soho_diskfile').eval())
        parm_outputDir_EXR = os.path.dirname(hou.parm(rop.path() + '/vm_picture').eval())
        parm_frameStart    = int(hou.evalParm(rop.path() + '/f1'))
        parm_frameEnd      = int(hou.evalParm(rop.path() + '/f2'))

        g_jobIFD['name']   = "IFD-GEN : %s - %s - %s" % (os.environ["USERNAME"], os.environ["HIPNAME"], rop.name())
        g_jobIFD['rop']    = rop.path()
        g_jobIFD['frames'] = "%d - %d" % (parm_frameStart, parm_frameEnd)
        g_jobIFD['files']  = os.environ['HIPFILE']
        g_jobIFD['outdir'] = parm_outputDir_IFD
        # IFD submission
        njid = buildCmdLineIFD(g_jobIFD)

        g_jobEXR['name']   = "IFD-REN : %s - %s - %s" % (os.environ["USERNAME"], os.environ["HIPNAME"], rop.name())
        files = ""
        for i in range(parm_frameStart, parm_frameEnd + 1):
            files += '"%s/%s.%04d.ifd" ' % (parm_outputDir_IFD, parm_diskName, i)
        g_jobEXR['files']  = files
        g_jobEXR['outdir'] = parm_outputDir_EXR
        g_jobEXR['dep']    = njid
        # EXR submission
        buildCmdLineEXR(g_jobEXR)

    #hou.releaseLicense()

###############################################################################
if __name__ == '__main__':
    main()
