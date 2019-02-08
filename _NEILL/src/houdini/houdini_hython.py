import sys
from houdini_base import *

# args = sys.argv[1:]
# print args
# args = ''.join(args)
# args = 'hython ' + args
# print args

runHou(app='hython', local=False, plug_rs=True, plug_mops=True,plug_qlib=True, plug_aelib=True)
