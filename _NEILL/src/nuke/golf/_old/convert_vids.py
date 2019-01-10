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
                new_folder = root.replace(folder, folder + '_CONVERTED')
                new_name   = os.path.join(new_folder, name)
                if not os.path.exists(new_folder):
                    os.makedirs(new_folder)
                cmd = ffmpeg + ' -y ' #-hide_banner -loglevel panic -threads 8'
                cmd += ' -gamma 2.2'
                cmd += ' -i %s' % old_name
                cmd += ' -pix_fmt yuv420p'
                cmd += ' -c:v libx264'
                cmd += ' -crf 20'
                # cmd += ' -vf scale -1:240:flags=bicubic'
                cmd += ' -vf scale=-2:240'
                cmd += ' %s' % new_name
                cmd = cmd.replace('\\', '/')
                # print cmd
                print 'Converting %s' % old_name ,
                la_utils.runCmd(cmd)
                print 'DONE'
# Scaling algorithms
# fast_bilinear
# bilinear
# bicubic
# experimental
# neighbor
# area
# bicublin
# gauss
# sinc
# lanczos
# spline
