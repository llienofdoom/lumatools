from ffmpeg_base import *
import math

input_files = sys.argv[1:]


w, h = 1280, 720
dim = la_getImageSize(input_files[0])

dimInput = raw_input('Please specify dimensions [ 0 (input rez), 1 (half rez), 2 (double rez), 3 (babyHD), 4 (fullHD), 5 (4k) ] (default 3) : ')
if dimInput == '0':
    w = dim[0]
    h = dim[1]
elif dimInput == '1':
    w = math.floor(dim[0] /2)
    h = math.floor(dim[1] /2)
elif dimInput == '2':
    w = dim[0]*2
    h = dim[1]*2
elif dimInput == '3':
    w = 1280
    h = 720
elif dimInput == '4':
    w = 1920
    h = 1080
elif dimInput == '5':
    w = 3840
    h = 2160
else:
    w = 1280
    h = 720

for input_file in input_files:
    input_name = str(os.path.basename(input_file))[:-4]
    folder = os.path.dirname(input_file)
    output_file = folder + '/' + input_name + '.jpg'
    cmd = ffmpeg + ' -y ' \
          + ' -gamma 2.2 '\
          + ' -i ' \
          + input_file \
          + ' -qscale:v 2 ' \
          + ' -vf scale=%d:%d ' % (w,h) \
          + output_file
          
    cmd = cmd.replace('\\', '/')
    # print cmd
    la_utils.runCmd(cmd)
    #+ ' -vf scale=%d:%d ' % (w,h) \

