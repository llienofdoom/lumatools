import sys
from houdini_base import *

setHoudiniEnv()

args = sys.argv[1:]
inFile = str(args[0])
outFile = inFile.split('.')[0] + '.rat'
cmd = env['HB'] + '/iconvert %s %s' % (inFile, outFile)
print 'Starting', cmd
la_utils.runCmd(cmd, env)
