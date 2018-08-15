from env import *
import os, json

LA_HOU_VERSION = '002'
HOU_VER = ''
RS_VER  = ''
RSP_VER = ''

logging.info('Setting up HOUDINI environment.')
# Read settings ###############################################################
settings_file = ''
if "LA_HOU_VERSION" in os.environ:
    logging.info('Found environment var for Houdini version.')
    settings_file = LA_ENV['SETTINGS'] + '/houdini/hou_' + os.environ['LA_HOU_VERSION'] + '.json'
else:
    logging.info('Using standard Houdini version.')
    settings_file = LA_ENV['SETTINGS'] + '/houdini/hou_' + LA_HOU_VERSION + '.json'
logging.info('Using %s for settings.', settings_file)
settings = json.load(open(settings_file))
HOU_VER = settings['hou_ver']
RS_VER  = settings['rs_ver']
RSP_VER = settings['rs_plugin_ver']
logging.info('Using H-%s : R-%s : P-%s.', HOU_VER, RS_VER, RSP_VER)
# Houdini Setup ###############################################################
LA_ENV['HFS']                           = LA_ENV['ROOT'] + '/_distros/hfs.windows-x86_64_' + HOU_VER
LA_ENV['H']                             = LA_ENV['HFS']
LA_ENV['HB']                            = LA_ENV['H'] + '/bin'
LA_ENV['HD']                            = LA_ENV['H'] + '/demo'
LA_ENV['HH']                            = LA_ENV['H'] + '/houdini'
LA_ENV['HHC']                           = LA_ENV['H'] + '/houdini/config'
LA_ENV['HT']                            = LA_ENV['H'] + '/toolkit'
LA_ENV['HTB']                           = LA_ENV['H'] + '/toolkit/bin'
LA_ENV['HSITE']                         = LA_ENV['ROOT'] + '/SITE'
LA_ENV['HOUDINI_EXTERNAL_HELP_BROWSER'] = '1'
LA_ENV['HOUDINI_WINDOW_CONSOLE']        = '1'
LA_ENV['HOUDINI_BUFFEREDSAVE']          = '1'
LA_ENV['PATH']                          = LA_ENV['HB'] + os.pathsep + os.environ['PATH']
LA_ENV['HOUDINI_MAJOR_RELEASE']         = str(HOU_VER).split('.')[0]
LA_ENV['HOUDINI_MINOR_RELEASE']         = str(HOU_VER).split('.')[1]
LA_ENV['HOUDINI_BUILD_VERSION']         = str(HOU_VER).split('.')[2]
LA_ENV['HOUDINI_VERSION']               = str(HOU_VER)
LA_ENV['HOUDINI_PATH']                  = '$HIP' + os.pathsep + '$HOUDINI_USER_PREF_DIR' + os.pathsep + '$HSITE/houdini16.5' + os.pathsep + '$HFS/houdini' + os.pathsep + '$HFS/bin'
# LA_ENV['HOUDINI_PATH']                  = '$HIP' + os.pathsep + '$HOUDINI_USER_PREF_DIR' + os.pathsep + LA_ENV['HSITE'] + '/houdini16.5' + os.pathsep + LA_ENV['HH'] + os.pathsep + LA_ENV['HB']
# Redshift Setup ##############################################################
LA_ENV['REDSHIFT_COREDATAPATH']    = LA_ENV['ROOT'] + '/_distros/Redshift-' + RS_VER
LA_ENV['REDSHIFT_LOCALDATAPATH']   = LA_ENV['REDSHIFT_COREDATAPATH']
LA_ENV['REDSHIFT_PROCEDURALSPATH'] = LA_ENV['REDSHIFT_COREDATAPATH'] + '/Procedurals'
LA_ENV['REDSHIFT_PREFSPATH']       = LA_ENV['REDSHIFT_COREDATAPATH'] + '/preferences.xml'
LA_ENV['REDSHIFT_LICENSEPATH']     = LA_ENV['REDSHIFT_COREDATAPATH']
LA_ENV['HOUDINI_DSO_ERROR']        = '2'
LA_ENV['PATH']                     = LA_ENV['REDSHIFT_COREDATAPATH'] + '/bin' + os.pathsep + LA_ENV['PATH']
LA_ENV['HOUDINI_PATH']             = LA_ENV['REDSHIFT_COREDATAPATH'] + '/Plugins/Houdini/' + RSP_VER + os.pathsep + LA_ENV['HOUDINI_PATH']
LA_ENV['redshift_LICENSE']         = '5053@192.168.35.254'
#############################################################################
