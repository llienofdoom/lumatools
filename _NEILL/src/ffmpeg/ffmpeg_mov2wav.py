from ffmpeg_base import *

input_file = ''
try:
    input_file = sys.argv[1]
except IndexError:
    la_utils.print_error('You need to supply a file to convert...')
input_name = str(os.path.basename(input_file)).split('.')[0]
folder = os.path.dirname(input_file) + '/'
output_file = folder + input_name + '_AUD.wav'
if not os.path.exists(folder):
    os.mkdir(folder)
cmd = ffmpeg + ' -y -i ' + input_file + ' -vn -acodec pcm_s16le -ar 44100 -ac 2 ' + output_file
cmd = cmd.replace('\\', '/')
la_utils.runCmd(cmd)
