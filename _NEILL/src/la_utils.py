###############################################################################
class console_colours:
    reset   = '\033[0m '
    red     = '\033[31m'
    green   = '\033[32m'
    yellow  = '\033[33m'
    blue    = '\033[34m'
    magenta = '\033[35m'
    cyan    = '\033[36m'
    white   = '\033[37m'

    b_red     = '\033[91m'
    b_green   = '\033[92m'
    b_yellow  = '\033[93m'
    b_blue    = '\033[94m'
    b_magenta = '\033[95m'
    b_cyan    = '\033[96m'
    b_white   = '\033[97m'

###############################################################################

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
    import subprocess, os
    cmd = cmd.split()
    if environ is None:
        return subprocess.check_output(cmd, shell=False)
    else:
        # Add default env to to process
        for key in os.environ:
            if key != 'PATH':
                environ[key] = os.environ[key]
            if key == 'PATH':
                environ['PATH'] += os.environ['PATH']
        # for i, j in environ.items():
        #     print i, j
        return subprocess.check_output(cmd, env=environ, shell=True, stderr=subprocess.STDOUT)
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

###############################################################################
def copyFolder(src, dst):
    import subprocess
    opsys = getOs()
    if opsys == 'win':
        cmd = 'robocopy %s %s /mir' % (src, dst)
        subprocess.call(cmd, shell=False)
    if opsys == 'lin':
        cmd = 'mkdir -p %s; rsync -avz --progress %s/ %s/' % (dst, src, dst)
        subprocess.call(cmd, shell=True)
    if opsys == 'mac':
        print 'NOT IMPLEMENTED YET!'
    if opsys == 'cyg':
        print 'NOT IMPLEMENTED YET!'
###############################################################################
