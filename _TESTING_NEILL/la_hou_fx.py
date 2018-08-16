import subprocess, os
from env.env_houdini import *

logging.info('Writing Environment to file...')
exe_file = write_exe('houdinifx', LA_ENV)
logging.info('Done!')

logging.info('Starting Houdini FX.')
print_env(LA_ENV)
if os_win:
    # pass
    subprocess.call([exe_file], shell=True)
else:
    # pass
    subprocess.call(['/bin/sh', exe_file], shell=True)

os.remove(exe_file)
