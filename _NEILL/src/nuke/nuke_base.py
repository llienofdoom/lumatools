import os, sys
import la_utils

# Read settings ###############################################################
opsys    = la_utils.getOs()
settings = la_utils.readSettings()
config_current = ''
try:
    config_current = os.environ['LA_NUKE_CURRENT']
except KeyError:
    config_current = str(settings['current'])

# Check for local version #####################################################
use_local_nuke = False
def useLocalNuke():
    global use_local_nuke
    path_remote      = str(settings['location_remote'][opsys]  + config_current)
    path_local       = str(settings['location_local' ][opsys]  + config_current)
    if os.path.exists(path_local):
        print 'Using Local.'
    else:
        print 'Updating Local.'
        print 'Copying from', path_remote, 'to', path_local
        print 'Please be patient. Go have a coffee or something.'
        la_utils.copyFolder(path_remote, path_local)
        print 'Update complete! Continuing startup.'
    use_local_nuke = True

# Set environment #############################################################
env = dict()
env['PATH'] = os.environ['PATH']
env['PATH'] += os.pathsep + 'X:/_studiotools/software/ffmpeg/bin' + os.pathsep
env['TMP']  = '/tmp'
env['TEMP'] = '/tmp'
env['LA_ROOT']   = os.environ['LA_ROOT']
env['LA_VENV']   = os.environ['LA_VENV']
env['LA_BRANCH'] = os.environ['LA_BRANCH']
if opsys is 'win':
    env['SystemRoot'] = 'C:/Windows'
    env['TMP']        = 'C:/tmp'
    env['TEMP']       = 'C:/tmp'

###############################################################################
def setNukeEnv():
    global env
    global use_local_houdini
    path_remote  = str(settings['location_remote'][opsys] + config_current)
    path_local   = str(settings['location_local'][opsys]  + config_current)
    path_nuke = path_local if use_local_houdini else path_remote
    env['HFS']   = path_houdini

