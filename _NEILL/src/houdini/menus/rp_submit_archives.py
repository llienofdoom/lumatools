import os
import hou

rpcmd = '"' + os.environ['RP_CMDRC_DIR'] + '/rprccmd"'

###############################################################################
def checkSelected():
    selected_nodes = []
    for node in hou.selectedNodes():
        if 'Redshift_ROP' in node.type().name():
            selected_nodes.append(node)
        if 'ifd' in node.type().name():
            selected_nodes.append(node)
    return selected_nodes

###############################################################################
def processRop(rop):
    user = hou.expandString('$USER')
    hip  = hou.expandString('$HIPFILE')
    frame_s = 0
    frame_e = 0
    archive_name = ''
    archive_root = ''
    ioutput_name = ''
    ioutput_root = ''
    archive_ext = ''
    renderer = ''

    trange = rop.parm('trange').eval()
    if trange is 0:
        frame_s = int(hou.frame())
        frame_e = int(hou.frame())
    else:
        frame_s = int(rop.parm('f1').eval())
        frame_e = int(rop.parm('f2').eval())

    if 'ifd' in rop.type().name(): ############################################
        archive_on = rop.parm('soho_outputmode').eval()
        if archive_on is 0:
            hou.ui.displayMessage('Please ENABLE and set ARCHIVE!')
            exit(0)
        archive_path = rop.parm('soho_diskfile').eval()[:-9]
        archive_name = os.path.basename(archive_path)
        archive_root = os.path.dirname( archive_path)
        ioutput_path = rop.parm('vm_picture'   ).eval()[:-9]
        ioutput_name = os.path.basename(ioutput_path)
        ioutput_root = os.path.dirname( ioutput_path)
        archive_ext = 'ifd'
        renderer    = 'RenderEXR/17.5.364'
    elif 'Redshift_ROP' in rop.type().name(): #################################
        archive_on = rop.parm('RS_archive_enable').eval()
        if archive_on is 0:
            hou.ui.displayMessage('Please ENABLE and set ARCHIVE!')
            exit(0)
        archive_path = rop.parm('RS_archive_file').eval()[:-8]
        archive_name = os.path.basename(archive_path)
        archive_root = os.path.dirname( archive_path)
        ioutput_path = rop.parm('RS_outputFileNamePrefix').eval()[:-9]
        ioutput_name = os.path.basename(ioutput_path)
        ioutput_root = os.path.dirname( ioutput_path)
        archive_ext = 'rs'
        renderer    = 'Redshift/17.5_2.6.44'

    if not os.path.exists(archive_root):
        os.makedirs(archive_root)
    for i in range(frame_s, frame_e + 1):
        filename = '%s/%s.%04d.%s' % (archive_root, archive_name, i, archive_ext)
        open(filename, 'a').close()
    files = '"@%s/%s.*.%s"' % (archive_root, archive_name, archive_ext)

    # ARCHIVE
    cmd = rpcmd
    cmd += ' -nj_name "[%s] ARCHIVE : %s - %s"' % (user, hip, rop.name())
    cmd += ' -retnjid'
    cmd += ' -nj_priority 9'
    cmd += ' -nj_renderer "gen/CURRENT"'
    cmd += ' -nj_pools "gen"'
    # cmd += ' -nj_pools "testing"'
    cmd += ' -nj_splitmode "2,10"'
    cmd += ' -frames "%s-%s"' % (frame_s, frame_e)
    cmd += ' -outdir "%s"' % (archive_root)
    cmd += ' -rop "%s"' % (rop.path())
    cmd += ' %s' % hip
    # print cmd
    id = os.system('"' + cmd + '"')

    # EXR
    cmd = rpcmd
    cmd += ' -nj_name "[%s] RENDER : %s - %s"' % (user, hip, rop.name())
    cmd += ' -nj_priority 5'
    cmd += ' -nj_renderer "%s"' % (renderer)
    cmd += ' -nj_pools "ren"'
    # cmd += ' -nj_splitmode "2,1"'
    cmd += ' -nj_dependency "%d"' % (id)
    cmd += ' -nj_deptype "0"'
    cmd += ' -outdir "%s"' % (ioutput_root)
    cmd += ' %s' % files
    # print cmd
    os.system('"' + cmd + '"')

###############################################################################
def main():
    if hou.hipFile.hasUnsavedChanges():
        hou.ui.displayMessage('Unsaved changes. Save First!')
        exit(0)

    selected_nodes = checkSelected()
    for rop in selected_nodes:
        processRop(rop)
    hou.ui.displayMessage('Submitted! Please check RenderPal.')

###############################################################################
main()
###############################################################################
