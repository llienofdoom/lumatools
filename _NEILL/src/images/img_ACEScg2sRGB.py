import sys, os, glob

oiiotool = "H:/SITE/OpenImageIO-1.5.0-OCIO/bin/oiiotool.exe"

input_file = sys.argv[1]

if 's' in raw_input('One file or sequence? (o/s) : '):
    dirname  = os.path.dirname(input_file)
    basename = os.path.basename(input_file)
    name     = basename.split('.')[0]
    input_files = glob.glob(dirname + os.sep + name + '*')
    for input_file in input_files:
        input_name = str(os.path.basename(input_file))[:-4]
        folder = os.path.dirname(input_file)
        output_file = folder + '/' + input_name + '_sRGB.jpg'
        cmd  = oiiotool
        cmd += ' --colorconvert'
        cmd += ' "ACES - ACEScg" "Output - sRGB"'
        cmd += ' %s' % input_file
        cmd += ' --ch R,G,B'
        cmd += ' -o %s' % output_file
        cmd = cmd.replace('\\', '/')
        print cmd
        os.system(cmd)
else:
    input_name = str(os.path.basename(input_file))[:-4]
    folder = os.path.dirname(input_file)
    output_file = folder + '/' + input_name + '_sRGB.jpg'
    cmd  = oiiotool
    cmd += ' --colorconvert'
    cmd += ' "ACES - ACEScg" "Output - sRGB"'
    cmd += ' %s' % input_file
    cmd += ' --ch R,G,B'
    cmd += ' -o %s' % output_file
    cmd = cmd.replace('\\', '/')
    print cmd
    os.system(cmd)
