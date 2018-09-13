from houdini_base import *

setHoudiniEnv()
setRedshiftEnv()
setMopsEnv()
setQlibEnv()
setGameDevEnv()

cmd  = env['HB'] + '/houdinicore'
la_utils.runCmd(cmd, env)
