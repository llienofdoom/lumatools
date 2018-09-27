#####################################################################
# H:\_distros\hfs.windows-x86_64_16.5.473\bin\hython.exe
# H:\_distros\_lumatools\lumatools\luma_houdiniHythonRender.py
# -h X:\_studiotools\TMP\HQ\mantra_test\mantra_test_103.hip
# -r "/out/rop_hm_base"
# -fs 1
# -fe 10
#####################################################################

import _CURRENT.settings.luma_site_settings
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

f  = int(sys.argv[6])
print "Setting frame to %d" % (f)

# Set progress output
rop.parm('vm_verbose').set(3)
rop.parm('vm_alfprogress').set(1)

# RENDER
print "Starting to render...",
rop.render()
print "DONE!"

quit()
