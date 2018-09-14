from houdini_base import *

try:
    checkLocalCopy()
    setHoudiniEnv()
    setRedshiftEnv()
    setMopsEnv()
    setQlibEnv()
    # setGameDevEnv()

    cmd  = env['HB'] + '/houdinifx'
    print 'Starting', cmd
    la_utils.runCmd(cmd, env)
except:
    la_utils.print_error('Something broke.')