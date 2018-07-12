import settings.luma_site_settings

import os
import hou

# Load scene file
hou.hipFile.load("X:/_studiotools/TMP/HQ/mantra_test/mantra_test_103.hip")

# Get list of ROPS to submit
rop_list = []

rop_out = hou.node("/out/OUT")
rop_children = rop_out.inputAncestors()
for child in rop_children:
    type = child.type().name()
    if type == 'ifd':
        rop_list.append(child)

# iterate over ROPS and GO!
for rop in rop_list:
    print rop.path(),
    # get ifd file name
    parm_diskFile = hou.parm(rop.path() + '/soho_diskfile').unexpandedString()
    print '\t' + parm_diskFile,
    # get image file name
    parm_outputPicture = hou.parm(rop.path() + '/vm_picture').unexpandedString()
    print '\t' +  parm_outputPicture,
    # get frame range
    parm_frameStart = int(hou.evalParm(rop.path() + '/f1'))
    parm_frameEnd   = int(hou.evalParm(rop.path() + '/f2'))
    print '\t' +  str(parm_frameStart), str(parm_frameEnd)

hou.releaseLicense()
