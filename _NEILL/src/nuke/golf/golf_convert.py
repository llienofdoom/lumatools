import sys, os

input_file = sys.argv[1]
path          = os.path.dirname(input_file)
parent        = os.path.dirname(str(path).rstrip(os.sep))
basename      = os.path.basename(input_file).split('.')[0]

ffmpeg   = 'X:/_studiotools/software/ffmpeg/bin/ffmpeg'
cmd  = ffmpeg + ' -y'
cmd += ' -gamma 2.2'
cmd += ' -i %s' % input_file
cmd += ' -pix_fmt yuv420p'
cmd += ' -c:v libx264'
cmd += ' %s' % ( path + os.sep + basename + '.mp4' )
cmd = cmd.replace('\\', '/')
os.system(cmd)
