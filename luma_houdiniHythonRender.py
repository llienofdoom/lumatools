import sys

hou.hipFile.load(sys.argv[1])
rop = hou.node(sys.argv[2])
fs  = sys.argv[3]
fe  = sys.argv[4]
rop.render(frame_range=(fs,fe))
quit()
