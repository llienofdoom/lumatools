from ffmpeg_base import *
import math

input_file = ''
dimInput = raw_input('Please specify dimensions [ 0 (input rez), 1 (half rez), 2 (double rez), 3 (babyHD), 4 (fullHD), 5 (4k) ] (default 3) : ')
quality = raw_input('Please specify quality. [ 0 - 51 ] (best to worst) Press enter to use default (23) : ')

for i in range(1, len(sys.argv)):
    try:
        input_file = sys.argv[i]
    except IndexError:
        la_utils.print_error('You need to supply a file to convert...')
    path          = os.path.dirname(input_file)
    parent        = os.path.dirname(str(path).rstrip(os.sep))
    basename      = os.path.basename(input_file).split('.')[0]

    if quality == '':
        quality = '23'
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
    if dimInput == '0':
        w = w
        h = h
    elif dimInput == '1':
        w = math.floor(w /2)
        h = math.floor(h /2)
    elif dimInput == '2':
        w = w*2
        h = h*2
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

    cmd  = ffmpeg + ' -y'
    cmd += ' -gamma 2.2'
    cmd += ' -i %s' % input_file
    cmd += ' -pix_fmt yuv420p'
    cmd += ' -c:v libx264'
    cmd += ' -crf %s' % quality
    cmd += ' -vf scale=%d:%d' % (w,h)
    cmd += ' %s' % ( path + os.sep + basename + '_CONVERTED.mp4' )
    cmd = cmd.replace('\\', '/')
    # print cmd
    la_utils.runCmd(cmd)
