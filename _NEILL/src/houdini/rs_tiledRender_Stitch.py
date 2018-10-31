from houdini_base import *
import glob

args = sys.argv[1:]
parent_path = os.path.dirname(args[0])
list_of_crops = glob.glob(parent_path + os.sep + 'crop_?-?' + os.sep + '*')
ext = list_of_crops[0].split('.')[-1]

string_crops = ""
for i in list_of_crops:
    string_crops += i + " "

cmd  = 'X:\_studiotools\software\ImageMagick\magick.exe'
cmd += ' convert '
cmd += string_crops
cmd += ' -background none'
cmd += ' -flatten'
cmd += ' ' + parent_path + os.sep + 'stitch.' + ext
# print cmd
os.system('"' + cmd + '"')
raw_input('Press Enter to close.')
