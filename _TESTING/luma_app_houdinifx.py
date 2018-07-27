import sys, os
import settings.luma_site_settings

for i in sys.path:
    print i


os.system( os.environ["HFS"] + "/bin/houdinifx.exe")
