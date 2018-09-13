import sys, os
import la_utils

opsys    = la_utils.getOs()
settings = la_utils.readSettings()
bin_dir  = settings['location'][opsys]
ffmpeg   = bin_dir + '/ffmpeg'
ffprobe  = bin_dir + '/ffprobe'

###############################################################################
def la_getImageSize(image):
    import json

    cmd  = ffprobe
    cmd += ' -v quiet'
    cmd += ' -print_format json'
    cmd += ' -show_streams'
    cmd += ' %s' % (image)

    cmd_return = la_utils.runCmd(cmd)
    jsn_return = json.loads(cmd_return)
    width  = jsn_return['streams'][0]['width']
    height = jsn_return['streams'][0]['height']
    dim = [int(width), int(height)]
    return dim
###############################################################################
