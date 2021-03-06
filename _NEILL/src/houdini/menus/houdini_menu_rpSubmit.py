def RP_selected_write_nodes():
    import os
    import hou

    if hou.hipFile.hasUnsavedChanges():
        hou.ui.displayMessage('Unsaved changes. Save First!')

    else:
        # rpcmd = '"' + os.environ['RP_CMDRC_DIR'] + 'RpRcCmd.exe"'
        rpcmd = '"' + os.environ['RP_CMDRC_DIR'] + '/rprccmd"'
        # redshift_version = os.environ['REDSHIFT_COREDATAPATH'].split('-')[1]

        for node in hou.selectedNodes():
            node_path = node.path()
            path = hou.hipFile.path()[:-4]
            proj = path.split('/')[1]
            scene = path.split('/')[-1]

            # frames = hou.playbar.frameRange()
            frames = []
            frames.append(node.parm('f1').eval())
            frames.append(node.parm('f2').eval())

            cmd = rpcmd
            cmd += ' -nj_name "RS-GEN : %s - %s - %s"' % (proj, scene, node.name())
            cmd += ' -nj_priority 5'
            cmd += ' -nj_paused'
            cmd += ' -nj_renderer "Redshift/RS_EXPORT"'
            cmd += ' -nj_pools "gen"'
            cmd += ' "-nj_splitmode" "2,5"'
            cmd += ' -frames "%s-%s"' % (frames[0], frames[1])
            cmd += ' -rop "%s"' % (node_path)
            cmd += ' %s' % path + '.hip'
            # print cmd
            os.system('"' + cmd + '"')
            hou.ui.displayMessage('Submitted "%s" to RenderPal!' % node_path)

RP_selected_write_nodes()
