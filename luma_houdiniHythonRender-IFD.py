import sys, os

# change slashes to forward
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

# RENDER
print "Starting to render...",
rop.render(frame_range=(fs, fe))
print "DONE!"

quit()
