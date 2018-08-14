import logging
import platform
import os

# Setup Logging ###############################################################
logging.basicConfig(
    # filename='neill.log',
    level=logging.DEBUG, # DEBUG | INFO | WARNING | ERROR | CRITICAL
    # format='LUMA-%(asctime)s-%(levelname)s :: %(message)s'
    format='LUMA-%(asctime)s :: %(message)s'
)
logging.info('Setting up main environment...')
# DEBUG - Print env ###########################################################
def print_env(env):
    logging.debug('Printing environment:')
    for key, value in env.iteritems():
        logging.debug('ENV : %s = %s', key, value)
# Test which os ###############################################################
os_win = 0
os_cyg = 0
os_lin = 0
os_mac = 0
if 'windows' in platform.system().lower():
    os_win = 1
    logging.info('OS type set to WINDOWS.')
if 'cygwin' in platform.system().lower():
    os_cyg = 1
    logging.info('OS type set to CYGWIN.')
if 'linux'  in platform.system().lower():
    os_lin = 1
    logging.info('OS type set to LINUX.')
if 'darwin' in platform.system().lower():
    os_mac = 1
    logging.info('OS type set to MAC.')
###############################################################################
def write_exe():
    exe_file_path = os.environ['TEMP'] + os.sep + 'LUMA_CMD.bat'
    logging.info('Saving cmd file to %s.', exe_file_path)
    env_set       = 'export'
    if os_win:
        env_set = 'SET'

    return exe_file_path

# Setup global env ############################################################
LA_ENV = {}
if os_win:
    LA_ENV['ROOT'] = 'H:'
LA_ENV['SETTINGS'] = LA_ENV['ROOT'] + '/_distros/_lumatools/lumatools/_TESTING_NEILL/settings'
# OCIO
LA_ENV['OCIO'] = LA_ENV['ROOT'] + '/SITE/ocio/nuke-default/config.ocio'
###############################################################################
