from ffmpeg_base import *
import math, win32file

input_file = 'NONE'
path = ''
tmp_path = os.environ['TMP'] + os.sep + 'LA_EDIT_TMP.txt'
tmp_list = open(tmp_path, 'w+')
print tmp_path
tmp_path = win32file.GetLongPathName(tmp_path)
print tmp_path

while input_file != '':
    input_file = raw_input('Add video to EDIT : ')
    if input_file == '':
        break
    path       = os.path.dirname(input_file)
    input_file = input_file.replace('\\', '/')
    tmp_list.write('file ' + input_file + '\n')
tmp_list.close()

cmd  = ffmpeg + ' -y'
cmd += ' -f concat -safe 0'
cmd += ' -i %s' % tmp_path
cmd += ' -c copy'
cmd += ' %s' % ( path + os.sep + 'EDIT.mp4' )
# cmd = cmd.replace('\\', '/')
print cmd
la_utils.runCmd(cmd)
