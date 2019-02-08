def RP_selected_write_nodes():
    import os
    import hou

    if hou.hipFile.hasUnsavedChanges():
        hou.ui.displayMessage('Unsaved changes. Save First!')

    else:
        rpcmd = '"' + os.environ['RP_CMDRC_DIR'] + 'RpRcCmd.exe"'
        redshift_version = os.environ['REDSHIFT_COREDATAPATH'].split('-')[1]

        for node in hou.selectedNodes():
            node_path = node.path()
            path = hou.hipFile.path()[:-4]
            proj = path.split('/')[1]
            scene = path.split('/')[-1]

            frames = hou.playbar.frameRange()

            cmd = rpcmd
            cmd += ' -nj_name "%s - %s - %s"' % (proj, scene, node.name())
            cmd += ' -nj_priority 5'
            cmd += ' -nj_paused'
            cmd += ' -nj_renderer "Redshift/RS_EXPORT"'
            cmd += ' -nj_pools "rs_gen_always"'
            cmd += ' "-nj_splitmode" "2,10"'
            cmd += ' -frames "%s-%s"' % (frames[0], frames[1])
            cmd += ' -rop "%s"' % (node_path)
            cmd += ' %s' % path + '.hip'
            print cmd
            os.system('"' + cmd + '"')
            hou.ui.displayMessage('Submitted to RenderPal!')
