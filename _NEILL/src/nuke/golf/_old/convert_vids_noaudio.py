import sys, os
import la_utils

opsys    = la_utils.getOs()
settings = la_utils.readSettings()
bin_dir  = settings['ffmpeg_location'][opsys]
ffmpeg   = bin_dir + '/ffmpeg'
ffprobe  = bin_dir + '/ffprobe'

folders = sys.argv
for folder in folders:
    for root, dirs, files in os.walk(folder):
        for name in files:
            if '.mp4' in name:
                old_name   = os.path.join(root, name)
                new_folder = root.replace(folder, folder + '_CONVERTED_NoAudio')
                new_name   = os.path.join(new_folder, name)
                if not os.path.exists(new_folder):
                    os.makedirs(new_folder)
                cmd = ffmpeg + ' -y '
                cmd += ' -i %s' % old_name
                cmd += ' -an'
                cmd += ' %s' % new_name
                cmd = cmd.replace('\\', '/')
                print 'Converting %s' % old_name ,
                la_utils.runCmd(cmd)
                print 'DONE'
