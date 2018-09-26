import sys
from houdini_base import *

args = sys.argv[1:]

# Check if running from houdini or commandline
running_in_houdini = False
if '_hou' in sys.modules:
    running_in_houdini = True

print running_in_houdini
print args

raw_input('YEAH!')
