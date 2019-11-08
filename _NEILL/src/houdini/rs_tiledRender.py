from houdini_base import *

setHoudiniEnv()
setRedshiftEnv()

args = sys.argv[1:]
res = raw_input("Please enter resolution  [ w h ] : ").split()
dim = raw_input("Please type in divisions [ w h ] : ").split()

for rs_file in args:
    name = os.path.basename(rs_file)[:-3]
    path = os.path.dirname(rs_file)
    w = 0
    if (int(res[0]) % int(dim[0])) != 0:
        w = int(res[0]) / int(dim[0]) + 1
    else:
        w = int(res[0]) / int(dim[0])
    h = 0
    if (int(res[1]) % int(dim[1])) != 0:
        h = int(res[1]) / int(dim[1]) + 1
    else:
        h = int(res[1]) / int(dim[1])

    for y in range(0, int(dim[1])):
        for x in range(0, int(dim[0])):
            cropOffsetX = x * w
            cropOffsetY = y * h
            cropWidth   = w
            cropHeight  = h
            crop = '-crop %i %i %i %i' % (cropOffsetX, cropOffsetY, cropWidth, cropHeight)

            rpcmd = '"' + os.environ['RP_CMDRC_DIR'] + 'RpRcCmd.exe"'
            cmd = rpcmd
            name_crop = name + '_crop_%d-%d' % (x, y)
            cmd += ' -nj_name "%s"' % ('RS TILED : ' + name_crop)
            cmd += ' -nj_tags "LUMA"'
            cmd += ' -nj_priority 5'
            cmd += ' -nj_renderer "Redshift/2.6.44_Tiled"'
            cmd += ' -nj_pools "testing"'
            # cmd += ' -nj_paused'
            path_crop = path + os.sep + 'crop_%d-%d' % (x, y)
            cmd += ' -outdir "%s"' % path_crop
            cmd += ' -width "%d"' % int(res[0])
            cmd += ' -height "%d"' % int(res[1])
            cmd += ' -cropOffsetX "%d"' % cropOffsetX
            cmd += ' -cropOffsetY "%d"' % cropOffsetY
            cmd += ' -cropWidth "%d"'   % cropWidth
            cmd += ' -cropHeight "%d"'  % cropHeight
            cmd += ' %s' % rs_file
            print cmd
            njid = os.system('"' + cmd + '"')

raw_input('Press Enter to close.')
