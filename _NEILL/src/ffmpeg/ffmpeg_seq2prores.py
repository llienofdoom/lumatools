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

framerate = raw_input('Please specify framerate [ 23.976 / 24 / 25 / 29.97 / 30 ] (25) : ')
if framerate == '':
    framerate = '25'
quality   = raw_input('Please specify quality [ 0 - 32 ] (13) : ')
if quality == '':
    quality = '13'

cmd  = ffmpeg + ' -y'
cmd += ' -r %s' % framerate
cmd += ' -start_number %d' % start_frame
cmd += ' -gamma 2.2'
cmd += ' -i %s' % ( path + os.sep + basename + '.%04d.' + extention )
cmd += ' -c:v prores_ks'
cmd += ' -profile:v 3'
cmd += ' -qscale:v %s' % quality
cmd += ' -vendor ap10'
cmd += ' -pix_fmt yuv422p10le'
cmd += ' %s' % ( parent + os.sep + basename + '_prores422.mov' )
cmd = cmd.replace('\\', '/')
# print cmd
la_utils.runCmd(cmd)
