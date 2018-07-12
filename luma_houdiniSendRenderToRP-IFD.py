import settings.luma_site_settings

import os
import hou

hou.hipFile.load("X:/_studiotools/TMP/HQ/mantra_test/mantra_test_103.hip")

rop_list = []

rop_out = hou.node("/out/OUT")
rop_children = rop_out.inputAncestors()
for child in rop_children:
    type = child.type().name()
    if type == 'ifd':
        rop_list.append(child)

print rop_list
print os.environ["HIPNAME"]
