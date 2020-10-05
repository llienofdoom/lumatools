import os, sys
import la_utils

# Read settings ###############################################################
opsys    = la_utils.getOs()
settings = la_utils.readSettings()
config_current = ''
try:
    config_current = os.environ['LA_MAYA_CURRENT']
except KeyError:
    config_current = str(settings['current'])
config_versions    = settings['config'][config_current]
version_maya    = str(config_versions['maya'])

# Check for local version #####################################################
use_local_maya = False
def useLocalMaya():
    global use_local_maya
    path_remote      = str(settings['location_remote'][opsys]  + version_maya)
    path_local       = str(settings['location_local' ][opsys]  + version_maya)
    if os.path.exists(path_local):
        print 'Using Local.'
    else:
        print 'Updating Local.'
        print 'Copying from', path_remote, 'to', path_local
        print 'Please be patient. Go have a coffee or something.'
        la_utils.copyFolder(path_remote, path_local)
        print 'Update complete! Continuing startup.'
    use_local_maya = True

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
def setMayaEnv():
    global env
    global use_local_maya
    path_remote  = str(settings['location_remote'][opsys] + version_maya)
    path_local   = str(settings['location_local'][opsys]  + version_maya)
    path_maya    = path_local if use_local_maya else path_remote
    path_hsite   = str(settings['hsite'][opsys])
    del os.environ['OCIO']
    env['MAYA_LOCATION']   = path_maya
    env['PATH']  = env['MAYA_LOCATION'] + os.sep + 'bin' + os.pathsep + env['PATH']
    env['MAYA_MODULE_PATH']  = path_hsite + os.sep + 'maya' + version_maya + os.sep + 'modules'
    env['MAYA_SCRIPT_PATH']  = path_hsite + os.sep + 'maya' + version_maya + os.sep + 'scripts'
    env['MAYA_PLUG_IN_PATH'] = path_hsite + os.sep + 'maya' + version_maya + os.sep + 'plug-ins'
    env['MAYA_SHELF_PATH']   = path_hsite + os.sep + 'maya' + version_maya + os.sep + 'shelves'
    env['ADSKFLEX_LICENSE_FILE'] = '2080@192.168.35.28'
    env['MAYA_LICENSE_METHOD']   = 'network'
    env['AUTODESK_ADLM_THINCLIENT_ENV'] = 'H:/_distros/Maya2016.5/AdlmThinClientCustomEnv.xml'
    

###############################################################################
def runMaya(app, local=False):
    if local:
        useLocalMaya()
    setMayaEnv()

    args = ' '.join(sys.argv[1:])
    cmd = '%s %s' % (app, args)
    print 'Starting', cmd
    print la_utils.runCmd(cmd, env)
