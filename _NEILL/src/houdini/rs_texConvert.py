from houdini_base import *

setHoudiniEnv()
setRedshiftEnv()

args = sys.argv[1:]

for i in args:
    f = '%s' % i
    cmd = env['REDSHIFT_COREDATAPATH'] + os.sep + 'bin' + os.sep + 'redshiftTextureProcessor %s' % f
    print 'Converting %s' % f
    la_utils.runCmd(cmd, env)
    print 'Done!'
print 'All Done!'
raw_input('Press Enter to close.')
