import logging
import platform
import os
import sys
import time
import subprocess

# Setup Logging ###############################################################
logging.basicConfig(
    # filename='neill.log',
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
        exe_file.write('start %s\n' % cmd)
    else:
        exe_file.write('%s\n' % cmd)
    exe_file.close()
    return exe_file_path
###############################################################################
def run_exe(env, exe):
    print_env(env)
    if os_win:
        # pass
        subprocess.call([exe], shell=True)
    else:
        # pass
        subprocess.call(['/bin/sh', exe], shell=True)
    os.remove(exe)
# Setup global env ############################################################
LA_ENV = {}
if os_win:
    LA_ENV['ROOT'] = 'H:'
if os_cyg:
    LA_ENV['ROOT'] = '/mnt/h'
LA_ENV['SETTINGS'] = LA_ENV['ROOT'] + '/_distros/_lumatools/lumatools/_TESTING_NEILL/settings'
# OCIO
LA_ENV['OCIO'] = LA_ENV['ROOT'] + '/SITE/ocio/nuke-default/config.ocio'
