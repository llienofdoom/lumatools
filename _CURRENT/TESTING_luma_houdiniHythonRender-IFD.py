#####################################################################
# H:\_distros\hfs.windows-x86_64_16.5.473\bin\hython.exe
# H:\_distros\_lumatools\lumatools\luma_houdiniHythonRender.py
# -h X:\_studiotools\TMP\HQ\mantra_test\mantra_test_103.hip
# -r "/out/rop_hm_base"
# -fs 1
# -fe 10
#####################################################################

import settings.TESTING_luma_site_settings
import sys, os
import hou

# Change slashes to forward - fucking windows...
hipfile = sys.argv[2].replace('\\','/')
print hipfile

print "Loading file %s" % (hipfile)
hou.hipFile.load(hipfile)
print "Loaded!"

rop = hou.node(sys.argv[4])
print "Using ROP \"%s\"" % (rop.path())

fs  = int(sys.argv[6])
fe  = int(sys.argv[8])
print "Setting frame range to %d - %d" % (fs, fe)

# Set progress output
rop.parm('vm_verbose').set(3)
rop.parm('vm_alfprogress').set(1)

# RENDER
print "Starting to render...",
rop.render(frame_range=(fs, fe))
print "DONE!"

quit()
