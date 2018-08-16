from env.env_houdini import *

logging.info('Writing Environment to file...')
exe_file = write_exe('houdinifx', LA_ENV)
logging.info('Done!')

logging.info('Starting Houdini FX.')

run_exe(LA_ENV, exe_file)
