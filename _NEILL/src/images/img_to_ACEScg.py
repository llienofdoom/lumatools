import sys, os

oiiotool = 'H:/SITE/OpenImageIO-1.5.0-OCIO/bin/oiiotool.exe'

input_files = sys.argv[1:]

choice = raw_input('Source Colour Space? [ 1 - old sRGB | 2 - old linear ] (1) : ')
space = ''
if choice is '1':
    space = '"Output - sRGB"'
elif choice is '2':
    space = '"Utility - Linear - sRGB"'
else:
    space = '"Output - sRGB"'

for input_file in input_files:
    input_name = str(os.path.basename(input_file))[:-4]
    input_ext  = str(input_file)[-3:]
    folder = os.path.dirname(input_file)
    output_file = folder + '/ACEScg_' + input_name  + '.' + input_ext
    
    cmd  = oiiotool
    cmd += ' --colorconvert'
    cmd += ' %s "ACES - ACEScg"' % space
    cmd += ' %s' % input_file
    cmd += ' -o %s' % output_file
    cmd = cmd.replace('\\', '/')
    print cmd
    os.system(cmd)

os.system('pause')
