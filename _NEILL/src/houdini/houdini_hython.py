import subprocess
from houdini_base import *

try:
    print runHou(app='hython', local=False, plug_rs=True, plug_mops=True,plug_qlib=True, plug_aelib=True)
except subprocess.CalledProcessError as error:
    exit(0)
