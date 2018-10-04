import os, sys
import la_utils

# Read settings ###############################################################
opsys    = la_utils.getOs()
settings = la_utils.readSettings()

config_current = ''
try:
    config_current = os.environ['LA_BLEND_CURRENT']
except KeyError:
    config_current = str(settings['current'])
config_versions    = settings['config'][config_current]
version_blender    = str(config_versions['blender'])
path               = str(settings['location'][opsys]  + version_blender)
blender            = path + '/blender'

print 'Starting luma remote blender version %s.' % version_blender
print 'Running from %s.' % path

def setBlenderEnv():
    pass

args = ' '.join(sys.argv[1:])
cmd = blender + ' ' + args
cmd = cmd.replace('\\', '/')
print cmd
la_utils.runCmd(cmd)
