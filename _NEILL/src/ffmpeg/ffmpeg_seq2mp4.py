from ffmpeg_base import *
import glob

input_file = ''
try:
    input_file = sys.argv[1]
except IndexError:
    la_utils.print_error('You need to supply a file to convert...')
path          = os.path.dirname(input_file)
parent        = os.path.dirname(str(path).rstrip(os.sep))
basename      = os.path.basename(input_file).split('.')[0]
extention     = os.path.basename(input_file).split('.')[2]
list_of_files = glob.glob( path + os.sep + basename + '.????.*' )
if len(list_of_files) < 1:
    la_utils.print_error('List of files is empty. Wrong filename pattern. Must be [name].[####].[ext]')
list_of_files.sort()
start_frame   = int(str(list_of_files[0]).split('.')[-2])

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

framerate = raw_input('Please specify framerate [ 23.976 / 24 / 25 / 29.97 / 30 ] (25) : ')
if framerate == '':
    framerate = '25'
quality   = raw_input('Please specify quality [ 0 - 51 ] (23) : ')
if quality == '':
    quality = '23'

cmd  = ffmpeg + ' -y'
cmd += ' -r %s' % framerate
cmd += ' -start_number %d' % start_frame
cmd += ' -gamma 2.2'
cmd += ' -i %s' % ( path + os.sep + basename + '.%04d.' + extention )
cmd += ' -pix_fmt yuv420p'
cmd += ' -c:v libx264'
cmd += ' -crf %s' % quality
cmd += ' -vf scale=%d:%d' % (w,h)
cmd += ' %s' % ( parent + os.sep + basename + '.mp4' )
cmd = cmd.replace('\\', '/')
la_utils.runCmd(cmd)
