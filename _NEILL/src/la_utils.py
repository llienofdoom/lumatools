
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
def runCmd(cmd):
    import subprocess
    cmd = cmd.split()
    subprocess.call(cmd, shell=False)
###############################################################################
