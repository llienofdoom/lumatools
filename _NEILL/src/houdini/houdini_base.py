import os, sys
import la_utils

# Read settings ###############################################################
opsys    = la_utils.getOs()
settings = la_utils.readSettings()
config_current = ''
try:
    config_current = os.environ['LA_HOU_CURRENT']
except KeyError:
    config_current = str(settings['current'])
config_versions    = settings['config'][config_current]
version_houdini    = str(config_versions['houdini'])
version_redshift   = str(config_versions['redshift'])
version_plugin_rs  = str(config_versions['plugin_rs'])
version_arnold     = str(config_versions['arnold_version'])
location_arnold    = str(settings['arnold_location' ][opsys])

# Check for local version #####################################################
use_local_houdini = False
def useLocalHoudini():
    global use_local_houdini
    path_remote      = str(settings['location_remote'][opsys]  + version_houdini)
    path_local       = str(settings['location_local' ][opsys]  + version_houdini)
    if os.path.exists(path_local):
        print 'Using Local.'
    else:
        print 'Updating Local.'
        print 'Copying from', path_remote, 'to', path_local
        print 'Please be patient. Go have a coffee or something.'
        la_utils.copyFolder(path_remote, path_local)
        print 'Update complete! Continuing startup.'
    use_local_houdini = True

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
def setHoudiniEnv():
    global env
    global use_local_houdini
    path_remote  = str(settings['location_remote'][opsys] + version_houdini)
    path_local   = str(settings['location_local'][opsys]  + version_houdini)
    path_houdini = path_local if use_local_houdini else path_remote
    path_hsite   = str(settings['hsite'][opsys])
    env['HFS']   = path_houdini
    env['HSITE'] = path_hsite
    env['H']     = env['HFS']
    env['HB']    = env['HFS'] + '/bin'
    env['HD']    = env['HFS'] + '/demo'
    env['HH']    = env['HFS'] + '/houdini'
    env['HHC']   = env['HFS'] + '/houdini/config'
    env['HT']    = env['HFS'] + '/toolkit'
    env['HTB']   = env['HFS'] + '/toolkit/bin'
    env['HOUDINI_MAJOR_RELEASE'] = str(version_houdini).split('.')[0]
    env['HOUDINI_MINOR_RELEASE'] = str(version_houdini).split('.')[1]
    env['HOUDINI_BUILD_VERSION'] = str(version_houdini).split('.')[2]
    env['HOUDINI_VERSION']       = str(version_houdini)
    env['HOUDINI_EXTERNAL_HELP_BROWSER'] = '1'
    env['HOUDINI_WINDOW_CONSOLE']        = '1'
    env['HOUDINI_BUFFEREDSAVE']          = '1'
    env['HOUDINI_PATH']  = '$HIP'                   + os.pathsep
    env['HOUDINI_PATH'] += '$HOUDINI_USER_PREF_DIR' + os.pathsep
    env['HOUDINI_PATH'] += '$HSITE/houdini' \
                           + env['HOUDINI_MAJOR_RELEASE'] + '.' + env['HOUDINI_MINOR_RELEASE'] \
                           + os.pathsep
    env['HOUDINI_PATH'] += '$HFS/houdini'           + os.pathsep
    env['HOUDINI_PATH'] += '$HFS/bin'               + os.pathsep
    env['HOUDINI_OTLSCAN_PATH'] = '@/otls'          + os.pathsep
    env['HOUDINI_OTLSCAN_PATH'] = os.environ['LA_ROOT'] \
                                  + '/_' + os.environ['LA_BRANCH'] \
                                  + '/src/houdini/otls' \
                                  + os.pathsep \
                                  + env['HOUDINI_OTLSCAN_PATH']
    env['HOUDINI_MENU_PATH']    = '@'               + os.pathsep
    env['HOUDINI_NVIDIA_OPTIX_DSO_PATH'] = str(settings['optix_location'][opsys])
    env['PATH'] = env['HB'] + os.pathsep + env['PATH']

    env['HOUDINI_ENABLE_OLD_PRESETS'] = '1'
    env['HOUDINI_GALLERY_PATH']       = env['HSITE'] + '/h_galleries' + os.pathsep + env['HFS'] + '/houdini/gallery'
    env['HOUDINI_MENU_PATH']          = env['HSITE'] + '/h_menu' + os.pathsep + env['HOUDINI_MENU_PATH']
    env['HOUDINI_ACCESS_METHOD']      = '2'
    env['HOUDINI_SOLARIS']            = '1'

    env['DM']            = env['HSITE'] + '/houdini_DM'
    env['HOUDINI_PATH'] += env['HSITE'] + '/houdini_DM'

    # ARNOLD TEMP
    path_arnold  = location_arnold + os.sep + version_arnold + os.sep + version_arnold
    env['HOUDINI_PATH'] = path_arnold + os.pathsep + env['HOUDINI_PATH']
    env['PATH'] = path_arnold + os.sep + 'scripts/bin' + os.pathsep + env['PATH']
    env['PXR_PLUGINPATH_NAME'] = path_arnold + os.sep + 'hydra'

###############################################################################
def setRedshiftEnv():
    global env
    path_redshift  = str(settings['rs_location'][opsys] + version_redshift)
    path_plugin_rs = path_redshift + '/Plugins/Houdini/' + version_plugin_rs
    env['redshift_LICENSE']         = '5053@192.168.35.254'
    env['REDSHIFT_COREDATAPATH']    = path_redshift
    env['REDSHIFT_LOCALDATAPATH']   = path_redshift
    env['REDSHIFT_PROCEDURALSPATH'] = path_redshift + '/Procedurals'
    env['REDSHIFT_PREFSPATH']       = path_redshift + '/preferences.xml'
    env['REDSHIFT_LICENSEPATH']     = path_redshift
    env['HOUDINI_DSO_ERROR']        = '2'
    env['HOUDINI_PATH'] = path_plugin_rs + os.pathsep + env['HOUDINI_PATH']
    env['PATH'] = path_redshift + '/bin' + os.pathsep + env['PATH']

###############################################################################
def setMopsEnv():
    global env
    env['MOPS'] = env['HSITE'] + '/houdini_MOPS'
    env['HOUDINI_OTLSCAN_PATH'] = env['MOPS'] + '/otls' + os.pathsep + env['HOUDINI_OTLSCAN_PATH']

###############################################################################
def setQlibEnv():
    global env
    env['QLIB'] = env['HSITE'] + '/houdini_qLib'
    env['QOTL'] = env['QLIB']  + '/otls'
    env['HOUDINI_OTLSCAN_PATH'] =   env['QOTL'] + '/base'         + os.pathsep \
                                  + env['QOTL'] + '/future'       + os.pathsep \
                                  + env['QOTL'] + '/experimental' + os.pathsep \
                                  + env['HOUDINI_OTLSCAN_PATH']
    env['HOUDINI_MENU_PATH'] = env['QLIB'] + '/menu' + os.pathsep + env['HOUDINI_MENU_PATH']
    env['HOUDINI_PATH'] = env['QLIB'] + os.pathsep + env['HOUDINI_PATH']

###############################################################################
def setGameDevEnv():
    global env
    env['HOUDINI_PATH'] = env['HSITE'] + '/houdini_gameDev' + os.pathsep + env['HOUDINI_PATH']

###############################################################################
def setAeLib():
    global env
    env['HOUDINI_PATH'] = env['HSITE'] + '/houdini_aelib' + os.pathsep + env['HOUDINI_PATH']

###############################################################################
def setFeatherTools():
    global env
    env['HOUDINI_PATH'] = env['HSITE'] + '/houdini_featherTools2FX' + os.pathsep + env['HOUDINI_PATH']

###############################################################################
def runHou(app, local=True, plug_rs=False, plug_mops=False, plug_qlib=False, plug_gdev=False, plug_aelib=False, plug_feathers=False):
    if local:
        useLocalHoudini()
    setHoudiniEnv()
    if plug_rs:
        setRedshiftEnv()
    if plug_mops:
        setMopsEnv()
    if plug_qlib:
        setQlibEnv()
    if plug_gdev:
        setGameDevEnv()
    if plug_aelib:
        setAeLib()
    if plug_feathers:
        setFeatherTools()

    args = ' '.join(sys.argv[1:])
    cmd = env['HB'] + '/%s %s' % (app, args)
    print 'Starting', cmd
    print la_utils.runCmd(cmd, env)

