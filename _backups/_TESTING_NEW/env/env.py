import logging
import platform
import os
import sys
import time
import subprocess
# Global Env Vars #############################################################
LA_ROOT   = os.environ['LA_ROOT']
LA_TOOLS  = os.environ['LA_TOOLS']
LA_BRANCH = '_' + os.environ['LA_BRANCH']
# Setup Logging ###############################################################
log_path = ''
if 'windows' in platform.system().lower():
    log_path = LA_ROOT + '/__store/logs/' + str(time.ctime()).replace(' ', '-').replace(':', '-') + '_' + os.environ['USERNAME'] + '.log'
else:
    log_path = LA_ROOT + '/__store/logs/' + str(time.ctime()).replace(' ', '-').replace(':', '-') + '_' + os.environ['USER'] + '.log'
logging.basicConfig(
    # filename=log_path,
    level=logging.DEBUG,
    # level=logging.INFO,
    # level=logging.WARNING,
    # level=logging.ERROR,
    # level=logging.CRITICAL,
    # format='LUMA-%(asctime)s-%(levelname)s :: %(message)s'
    format='LUMA-%(asctime)s :: %(message)s'
)
logging.info('Setting up main environment...')
# DEBUG - Print env ###########################################################
def print_env(env):
    logging.debug('#'*80)
    logging.debug('Printing environment:')
    for key, value in env.iteritems():
        logging.debug('ENV : %s = %s', key, value)
    logging.debug('#' * 80)
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
# Write_Exe ###################################################################
def write_exe(cmd, env):
    exe_file_path = os.environ['TEMP'] + os.sep + 'LUMA_CMD_' + str(time.time()) + '.cmd'
    logging.info('Saving cmd file to %s.', exe_file_path)
    env_set       = 'export'
    exe_file = open(exe_file_path, 'w')
    if os_win:
        env_set = 'SET'
        exe_file.write('@echo off\n')
    for key, value in env.iteritems():
        exe_file.write('%s %s=%s\n' % (env_set, key, value))
    exe_file.write('\n')
    if os_win:
        exe_file.write('%s\n' % cmd)
    else:
        exe_file.write('%s\n' % cmd)
    exe_file.close()
    return exe_file_path
###############################################################################
def run_exe(env, exe):
    print_env(env)
    if os_win:
        # pass
        subprocess.call([exe], shell=False)
    else:
        # pass
        subprocess.call(['/bin/sh', exe], shell=False)
    os.remove(exe)
# Setup global env ############################################################
LA_ENV = {}

LA_ENV['ROOT']   = LA_ROOT
LA_ENV['TOOLS']  = LA_TOOLS
LA_ENV['BRANCH'] = LA_BRANCH
LA_ENV['SETTINGS'] = '%s/_distros/_lumatools/lumatools/%s/settings' % (LA_ENV['ROOT'], LA_ENV['BRANCH'])
# OCIO ################################
LA_ENV['OCIO'] = LA_ENV['ROOT'] + '/SITE/ocio/nuke-default/config.ocio'
