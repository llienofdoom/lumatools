from ffmpeg_base import *

input_files = sys.argv[1:]
for input_file in input_files:
    input_name = str(os.path.basename(input_file))[:-4]
    folder = os.path.dirname(input_file)
    output_file = folder + '/' + input_name + '.jpg'
    cmd = ffmpeg + ' -y -i ' \
          + input_file \
          + ' -qscale:v 2 ' \
          + output_file
    cmd = cmd.replace('\\', '/')
    # print cmd
    la_utils.runCmd(cmd)
