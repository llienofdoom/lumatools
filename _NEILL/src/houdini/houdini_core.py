from houdini_base import *

try:
    useLocalHoudini()
    setHoudiniEnv()
    setRedshiftEnv()
    setMopsEnv()
    setQlibEnv()
    # setGameDevEnv()

    cmd  = env['HB'] + '/houdinicore'
    print 'Starting', cmd
    la_utils.runCmd(cmd, env)
except:
    la_utils.print_error('Something broke.')
