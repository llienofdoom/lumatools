import os, sys
import shutil
import glob
import la_utils
import nuke

opsys    = la_utils.getOs()
settings = la_utils.readSettings()
root            = settings['root']
missing_footage = root + '/' + settings['standin']

###############################################################################
def update_path(cwd, nod, pas):
    nod = nuke.toNode(nod)
    seq = cwd + '/' + pas + '/' + pas + '.%04d.exr'
    frameS = 1
    frameE = 1

    files = glob.glob(seq[:-8] + '*')
    if len(files) == 0:
        print '\t\t\tSequence doesn\'t exist.'
        seq = missing_footage
        nod['premultiplied'].setValue(1)
    else:
        frameS = int(files[ 0].split('.')[-2])
        frameE = int(files[-1].split('.')[-2])

    nod['file'].setValue(seq)
    nod['first'    ].setValue(frameS)
    nod['last'     ].setValue(frameE)
    nod['origfirst'].setValue(frameS)
    nod['origlast' ].setValue(frameE)

    print '\t|-----o Updated path for pass - %s' % pas
###############################################################################
