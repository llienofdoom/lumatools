###############################################################################
class console_colours:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
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

###############################################################################
def copyFolder(src, dst):
    import subprocess
    opsys = getOs()
    if opsys == 'win':
        cmd = 'robocopy %s %s /mir' % (src, dst)
        subprocess.call(cmd, shell=False)
    if opsys == 'lin':
        print src
        print dst
        cmd = 'mkdir -p %s; cp -r %s %s' % (dst, src, dst)
        print cmd
        subprocess.call(cmd, shell=False)
    if opsys == 'mac':
        print 'NOT IMPLEMENTED YET!'
    if opsys == 'cyg':
        print 'NOT IMPLEMENTED YET!'
###############################################################################
