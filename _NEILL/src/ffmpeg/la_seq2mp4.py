import sys, os
import la_utils

opsys    = la_utils.getOs()
settings = la_utils.readSettings()
bin_dir  = settings['location'][opsys]
ffmpeg   = bin_dir + '/ffmpeg.exe'

input_file = ''
try:
    input_file = sys.argv[1]
    input_name = str(os.path.basename(input_file)).split('.')[0]
    folder = os.path.dirname(input_file) + '/jpg/'
    output_file = folder + input_name + '.%04d.jpg'
    start_frame = 1001
    if not os.path.exists(folder):
        os.mkdir(folder)
    cmd = ffmpeg + ' -y -i ' + input_file + ' -start_number ' + str(start_frame) + ' -qscale:v 2 ' + output_file
    cmd = cmd.replace('\\', '/')
    la_utils.runCmd(cmd)
except IndexError:
    raw_input('You need to supply a file to convert...')
    exit(0)

