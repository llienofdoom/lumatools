from houdini_base import *
import glob
import subprocess

tool = 'H:/_distros/htoa-5.1.1_r126b954_houdini-18.0.391/htoa-5.1.1_r126b954_houdini-18.0.391/scripts/bin/'

setHoudiniEnv()

args = sys.argv[1:]

format = raw_input('Please enter precisely the file extension : ')

for current_folder in args:
    print 'Traversing %s' % current_folder
    list_of_imgs = glob.glob(current_folder + os.sep + '*.' + format)
    if len(list_of_imgs) > 0:
        for img in list_of_imgs:
            folder = os.path.dirname(img)
            basename = os.path.basename(img).split('.')[0]
            new_name = folder + os.sep + basename + '.tx'
            cmd = tool + 'maketx.exe -v -u --oiio --checknan --filter lanczos3 %s -o %s' % (img, new_name)
            print 'Converting %s' % img
            try:
                la_utils.runCmd(cmd, env)
            except subprocess.CalledProcessError:
                print 'Error converting %s' % img
                continue
            print 'Done!'
print 'All Done!'
raw_input('Press Enter to close.')
