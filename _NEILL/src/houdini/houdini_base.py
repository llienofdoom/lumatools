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

# Set environment #############################################################
env = {}
env['PATH'] = os.environ['PATH']

def setHoudiniEnv():
    global env
    env['HFS']   = path_houdini
    env['H']     = env['HFS']
    env['HB']    = env['HFS'] + '/bin'
    env['HD']    = env['HFS'] + '/demo'
    env['HH']    = env['HFS'] + '/houdini'
    env['HHC']   = env['HFS'] + '/houdini/config'
    env['HT']    = env['HFS'] + '/toolkit'
    env['HTB']   = env['HFS'] + '/toolkit/bin'
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
    env['HOUDINI_PATH'] += '$HFS/bin'
    env['PATH']         = env['HB'] + os.pathsep + env['PATH']

