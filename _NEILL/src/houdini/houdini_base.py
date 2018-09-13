import sys, os
import la_utils

# Read settings ###############################################################
opsys    = la_utils.getOs()
settings = la_utils.readSettings()

config_current    = str(settings['current'])
config_versions   = settings['config'][config_current]
version_houdini   = str(config_versions['houdini'])
version_redshift  = str(config_versions['redshift'])
version_plugin_rs = str(config_versions['plugin_rs'])

# Check for local version, and set up base paths ##############################

###########################################################
## TODO Check for local version, copy over, use that!
###########################################################

location = 'remote'
# location = 'local'
path_houdini   = str(settings['location_%s' % location][opsys] + '/hfs.windows-x86_64_' + version_houdini)
path_redshift  = str(settings['location_%s' % location][opsys] + '/Redshift-'           + version_redshift)
path_plugin_rs = path_redshift + '/Plugins/Houdini/' + version_plugin_rs
path_hsite     = str(settings['hsite'][opsys])
path_pose_lib  = str(settings['pose_lib'][opsys])

# Set environment #############################################################
env = dict()
env['PATH'] = os.environ['PATH']
env['TMP']  = '/tmp'
env['TEMP'] = '/tmp'
if opsys is 'win':
    env['SystemRoot'] = 'C:/Windows'
    env['TMP']        = 'C:/tmp'
    env['TEMP']       = 'C:/tmp'

def setHoudiniEnv():
    global env
    env['HFS']   = path_houdini
    env['H']     = path_houdini
    env['HB']    = path_houdini + '/bin'
    env['HD']    = path_houdini + '/demo'
    env['HH']    = path_houdini + '/houdini'
    env['HHC']   = path_houdini + '/houdini/config'
    env['HT']    = path_houdini + '/toolkit'
    env['HTB']   = path_houdini + '/toolkit/bin'
    env['HSITE'] = path_hsite

    env['HOUDINI_MAJOR_RELEASE'] = str(version_houdini).split('.')[0]
    env['HOUDINI_MINOR_RELEASE'] = str(version_houdini).split('.')[1]
    env['HOUDINI_BUILD_VERSION'] = str(version_houdini).split('.')[2]
    env['HOUDINI_VERSION']       = str(version_houdini)

    env['HOUDINI_EXTERNAL_HELP_BROWSER'] = '1'
    env['HOUDINI_WINDOW_CONSOLE']        = '1'
    env['HOUDINI_BUFFEREDSAVE']          = '1'

    env['HOUDINI_PATH']  = '$HIP'                   + os.pathsep
    env['HOUDINI_PATH'] += '$HOUDINI_USER_PREF_DIR' + os.pathsep
    env['HOUDINI_PATH'] += '$HSITE/houdini16.5'     + os.pathsep
    env['HOUDINI_PATH'] += '$HFS/houdini'           + os.pathsep
    env['HOUDINI_PATH'] += '$HFS/bin'               + os.pathsep
    env['HOUDINI_OTLSCAN_PATH'] = '@/otls'          + os.pathsep
    env['HOUDINI_MENU_PATH']    = '@'               + os.pathsep
    env['PATH']         = env['HB'] + os.pathsep + env['PATH']

def setRedshiftEnv():
    global env
    env['redshift_LICENSE']         = '5053@192.168.35.254'
    env['REDSHIFT_COREDATAPATH']    = path_redshift
    env['REDSHIFT_LOCALDATAPATH']   = path_redshift
    env['REDSHIFT_PROCEDURALSPATH'] = path_redshift + '/Procedurals'
    env['REDSHIFT_PREFSPATH']       = path_redshift + '/preferences.xml'
    env['REDSHIFT_LICENSEPATH']     = path_redshift
    env['HOUDINI_DSO_ERROR']        = '2'
    env['HOUDINI_PATH'] = path_plugin_rs + os.pathsep + env['HOUDINI_PATH']
    env['PATH'] = path_redshift + '/bin' + os.pathsep + env['PATH']

def setMopsEnv():
    global env
    env['MOPS'] = path_hsite + '/houdini16.5/MOPS'
    env['HOUDINI_OTLSCAN_PATH'] = env['MOPS'] + '/otls' + os.pathsep + env['HOUDINI_OTLSCAN_PATH']

def setQlibEnv():
    global env
    env['QLIB'] = path_hsite + '/houdini16.5/qLib'
    env['QOTL'] = env['QLIB'] + '/otls'
    env['HOUDINI_OTLSCAN_PATH'] =   env['QOTL'] + '/base' + os.pathsep \
                                  + env['QOTL'] + '/future' + os.pathsep \
                                  + env['QOTL'] + '/experimental' + os.pathsep \
                                  + env['HOUDINI_OTLSCAN_PATH']
    env['HOUDINI_MENU_PATH'] = env['QLIB'] + '/menu' + os.pathsep + env['HOUDINI_MENU_PATH']
    env['HOUDINI_PATH'] = env['QLIB'] + os.pathsep + env['HOUDINI_PATH']

def setGameDevEnv():
    global env
    env['HOUDINI_PATH'] = path_hsite + '/houdini16.5/gamedev_toolset' + os.pathsep + env['HOUDINI_PATH']
