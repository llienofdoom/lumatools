from ffmpeg_base import *

input_file = ''
try:
    input_file = sys.argv[1]
except IndexError:
    la_utils.print_error('You need to supply a file to convert...')
path          = os.path.dirname(input_file)
parent        = os.path.dirname(str(path).rstrip(os.sep))
basename      = os.path.basename(input_file).split('.')[0]

# Check width & height divisible by 2, stupid h264.
w, h = 1280, 720
dim = la_getImageSize(input_file)
if dim[0] % 2 != 0:
    w = dim[0] - 1
else:
    w = dim[0]
if dim[1] % 2 != 0:
    h = dim[1] - 1
else:
    h = dim[1]

cmd  = ffmpeg + ' -y'
cmd += ' -gamma 2.2'
cmd += ' -i %s' % input_file
cmd += ' -pix_fmt yuv420p'
cmd += ' -c:v libx264'
cmd += ' -vf scale=%d:%d' % (w,h)
cmd += ' %s' % ( path + os.sep + basename + '_CONVERTED.mp4' )
cmd = cmd.replace('\\', '/')
# print cmd
la_utils.runCmd(cmd)
