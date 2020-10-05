from maya_base import *
import subprocess

try:
    runMaya(app='maya', local=False)
except subprocess.CalledProcessError as e:
    raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))