import sys, os

oiiotool = "H:/SITE/OpenImageIO-1.5.0-OCIO/bin/oiiotool.exe"

input_files = sys.argv[1:]
for input_file in input_files:
    input_name = str(os.path.basename(input_file))[:-4]
    folder = os.path.dirname(input_file)
    output_file = folder + '/' + input_name + '_sRGB.jpg'
    
    cmd  = oiiotool
    cmd += ' --colorconvert'
    cmd += ' "ACES - ACEScg" "Output - sRGB"'
    cmd += ' %s' % input_file
    cmd += ' -o %s' % output_file
    cmd = cmd.replace('\\', '/')
    print cmd
    os.system(cmd)
