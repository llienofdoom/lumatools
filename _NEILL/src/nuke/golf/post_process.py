import sys
import os
import glob

root_dir = str(sys.argv[1])
post_log = open(root_dir + '/post_log.txt', 'a')

post_log.write('Starting Post Process...\n')
post_log.write('Root as : ' + root_dir + '\n')

vids = os.listdir(root_dir)
for vid in vids:
    full_path = root_dir + '/' + vid
    if os.path.isdir(full_path):
        post_log.write('\tProcessing ' + vid + '.\n')

        # AUDIO
        aud = open(full_path + '/aud', 'r')
        audio_file = aud.readline()
        aud.close()
        post_log.write('\t\tSetting audio as : ' + audio_file + '.\n')

        # IMAGES
        images = glob.glob(full_path + '/*.*.png')
        name = os.path.basename(images[0]).split('.')[0]
        ext  = os.path.basename(images[0]).split('.')[2]
        seq  = name + '.%04d.' + ext
        post_log.write('\t\tSetting input as  : ' + seq + '.\n')
        parent = os.path.dirname(str(full_path).rstrip(os.sep))
        out_name = parent + '/' + vid + '.mp4'
        post_log.write('\t\tSetting output as : ' + out_name + '.\n')

        # FFMPEG
        post_log.write('\t\tFiring up FFMPEG...' + '.\n')
        ffmpeg = 'X:/_studiotools/software/ffmpeg/bin/ffmpeg'
        cmd = ffmpeg + ' -y '  # -hide_banner -loglevel panic -threads 8'
        cmd += ' -gamma 2.2'
        cmd += ' -i %s' % (full_path + '/' + seq)
        cmd += ' -i %s' % audio_file
        cmd += ' -pix_fmt yuv420p'
        cmd += ' -c:v libx264'
        cmd += ' -crf 20'
        # cmd += ' -vf scale -1:240:flags=bicubic'
        # cmd += ' -vf scale=-2:240'
        cmd += ' -c:a libvorbis -shortest'
        cmd += ' %s' % out_name
        cmd = cmd.replace('\\', '/')
        post_log.write('\t\t\tCMD : ' + cmd + '\n\n')
        os.system('"' + cmd + '"')

post_log.write('Cleaning up...' + '.\n')

post_log.write('\tRemoving Comps' + '.\n')

post_log.write('\tRemoving Images' + '.\n')

post_log.write('FUCKING DONE!')


post_log.close()
