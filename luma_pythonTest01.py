import luma_site_settings
import hou

hou.hipFile.load("X:/_studiotools/TMP/HQ/mantra_test/mantra_test_103.hip")

rop_out = hou.node("/out/OUT")
rop_children = rop_out.inputs()
for child in rop_children:
    print child.path()
    print child.name()


