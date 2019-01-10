from ffmpeg_base import *

input_file = ''
try:
    input_file = sys.argv[1]
except IndexError:
    la_utils.print_error('You need to supply a file to convert...')
path          = os.path.dirname(input_file)
parent        = os.path.dirname(str(path).rstrip(os.sep))
basename      = os.path.basename(input_file).split('.')[0]

quality   = raw_input('Please specify quality. [ 0 - 32 ] (best to worst) Press enter to use default (13) : ')
if quality == '':
    quality = '13'
audio = raw_input('Do you need to supply an audio file? [ y/n ] (n): ')
if audio == '':
    audio = 'n'
audio_file = ''
if audio == 'y':
    audio_file = raw_input('Please drag audio file to riiiight... HERE. : ')

cmd  = ffmpeg + ' -y'
cmd += ' -gamma 2.2'
cmd += ' -i %s' % input_file
if audio == 'y':
    cmd += ' -i %s' % audio_file
    cmd += ' -c:a aac -shortest'
cmd += ' -c:v prores_ks'
cmd += ' -profile:v 3'
cmd += ' -qscale:v %s' % quality
cmd += ' -vendor ap10'
cmd += ' -pix_fmt yuv422p10le'
cmd += ' %s' % ( path + os.sep + basename + '_prores422.mov' )
cmd = cmd.replace('\\', '/')
# print cmd
la_utils.runCmd(cmd)
