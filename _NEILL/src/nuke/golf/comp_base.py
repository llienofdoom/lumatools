import os, sys
import shutil
import glob
import la_utils
import nuke

opsys    = la_utils.getOs()
settings = la_utils.readSettings()


def update_path(node, seq):
    node = ''
    seq  = ''