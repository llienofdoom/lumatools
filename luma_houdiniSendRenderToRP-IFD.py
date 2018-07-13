import settings.luma_site_settings

import os
import hou

###############################################################################
g_job = {
    "name"     : "TESTING - ifd_job_001",
    "priority" : 5,
    "rop"      : "/out/rop_hm_base",
    "frames"   : "1-100",
    "files"    : "X:/_studiotools/TMP/HQ/mantra_test/mantra_test_103.hip",
    "outdir"   : ""
}

###############################################################################
def buildCmdLine(l_job):
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
    print njid

###############################################################################
def main():
    global g_job
    hou.hipFile.load("X:/_studiotools/TMP/HQ/mantra_test/mantra_test_103.hip")
    rop_list = []

    rop_out = hou.node("/out/OUT")
    rop_children = rop_out.inputAncestors()
    for child in rop_children:
        type = child.type().name()
        if type == 'ifd':
            rop_list.append(child)

    for rop in rop_list:
        parm_diskFile      = hou.parm(rop.path() + '/soho_diskfile').unexpandedString()
        parm_outputPicture = hou.parm(rop.path() + '/vm_picture').unexpandedString()
        parm_outputDir     = os.path.dirname(hou.parm(rop.path() + '/vm_picture').eval())
        parm_frameStart    = int(hou.evalParm(rop.path() + '/f1'))
        parm_frameEnd      = int(hou.evalParm(rop.path() + '/f2'))

        g_job['name']   = "IFD-GEN : %s - %s - %s" % (os.environ["USERNAME"], os.environ["HIPNAME"], rop.path())
        g_job['rop']    = rop.path()
        g_job['frames'] = "%d - %d" % (parm_frameStart, parm_frameEnd)
        g_job['files']  = os.environ['HIPFILE']
        g_job['outdir'] = parm_outputDir

        # IFD submission
        buildCmdLine(g_job)

    hou.releaseLicense()

###############################################################################
if __name__ == '__main__':
    main()
