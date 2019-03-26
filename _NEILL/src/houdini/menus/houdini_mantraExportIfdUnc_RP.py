import hou, os, sys


def mantraExportIfdUnc_RP():
    if hou.hipFile.hasUnsavedChanges():
        hou.ui.displayMessage('Unsaved changes. Save First!')

    else:
        old_hip = hou.getenv('HIP')
        old_hif = hou.getenv('HIPFILE')
        old_job = hou.getenv('JOB')

        if 'X:/' in old_hip:
            new_hip = old_hip.replace('X:/', '//192.168.35.14/x/')
            hou.hscript('set -u HIP')
            hou.hscript('set -g HIP = ' + new_hip)
        if 'X:/' in old_hif:
            new_hif = old_hip.replace('X:/', '//192.168.35.14/x/')
            hou.hscript('set -u HIPFILE')
            hou.hscript('set -g HIPFILE = ' + new_hif)
        if 'X:/' in old_job:
            new_job = old_hip.replace('X:/', '//192.168.35.14/x/')
            hou.hscript('set -u JOB')
            hou.hscript('set -g JOB = ' + new_job)

        rpcmd = '"' + os.environ['RP_CMDRC_DIR'] + 'RpRcCmd.exe"'
        for node in hou.selectedNodes():
            node.render()

            node_path = node.path()
            path = hou.hipFile.path()
            proj = path.split('/')[4]
            scene = hou.getenv('HIPNAME')

            frames = []
            frames.append(int(node.parm('f1').eval()))
            frames.append(int(node.parm('f2').eval()))

            diskFile = node.parm('soho_diskfile').eval()
            path = os.path.dirname(diskFile)
            basename = os.path.basename(diskFile).split('.')[0] + '.*.ifd'
            ifds = '@' + path + '/' + basename

            output = node.parm('vm_picture').eval()
            output = os.path.dirname(output)
            output = output.replace('//192.168.35.14/x', 'X:')

            hou_ver = hou.getenv('HOUDINI_VERSION')
            hou_ver = 'RenderEXR/' + hou_ver
            print hou_ver

            cmd = rpcmd
            cmd += ' -nj_name "IFD-REN : %s - %s - %s"' % (proj, scene, node.name())
            cmd += ' -nj_priority 5'
            cmd += ' -nj_renderer "%s"' % hou_ver
            cmd += ' -nj_pools "testing_ifd"'
            cmd += ' -frames "%s-%s"' % (frames[0], frames[1])
            cmd += ' -outdir "%s"' % output
            cmd += ' %s' % ifds
            # print cmd
            os.system('"' + cmd + '"')
            hou.ui.displayMessage('Submitted "%s" to RenderPal!' % node_path)

        hou.hscript('set -u HIP')
        hou.hscript('set -g HIP = ' + old_hip)
        hou.hscript('set -u HIPFILE')
        hou.hscript('set -g HIPFILE = ' + old_hif)
        hou.hscript('set -u JOB')
        hou.hscript('set -g JOB = ' + old_job)


mantraExportIfdUnc_RP()
