from houdini_base import *

# setHoudiniEnv()
# env['HOUDINI_SPLASH_FILE'] = env['HSITE'] + '/houdini16.5/pic/houdinisplash2.png'

runHou(app='houdinicore', local=True, plug_rs=False, plug_mops=True,plug_qlib=True)
