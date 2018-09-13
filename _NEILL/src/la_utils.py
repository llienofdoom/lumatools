
###############################################################################
def readSettings():
    import json
    settings = json.load( open('_settings.json', 'r') )
    return settings
###############################################################################

###############################################################################
def getOs():
    import platform

    if 'windows' in platform.system().lower():
        return 'win'
    if 'cygwin' in platform.system().lower():
        return 'cyg'
    if 'linux'  in platform.system().lower():
        return 'lin'
    if 'darwin' in platform.system().lower():
        return 'mac'
###############################################################################

###############################################################################
def runCmd(cmd, environ=None):
    import subprocess
    cmd = cmd.split()
    if environ is None:
        return subprocess.check_output(cmd, shell=False)
    else:
        return subprocess.check_output(cmd, env=environ, shell=False)
###############################################################################

###############################################################################
def print_error(text):
    import os
    print ''
    print os.path.realpath(__file__)
    print '#' * 80
    print ''
    raw_input(text)
    exit(0)
###############################################################################
