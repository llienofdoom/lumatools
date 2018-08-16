from env.env_houdini import *

args = ' '.join(sys.argv[1:])

logging.info('Writing Environment to file...')
exe_file = write_exe('houdinicore ' + args, LA_ENV)
logging.info('Done!')

logging.info('Starting Houdini Core.')
logging.info('Using args : %s' % args)

run_exe(LA_ENV, exe_file)
