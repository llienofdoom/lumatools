# import subprocess
from env.env_houdini import *

logging.info('Writing Environment to file...')
exe_file = write_exe()
logging.info('Done!')

logging.info('Starting Houdini FX.')
