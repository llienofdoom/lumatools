import sys, os

# SETUP #######################################################################
VERSION_HOUDINI  = "16.5.473"
VERSION_REDSHIFT = "2.5.72"
VERSION_REDSHIFT_PLUGIN = "16.5.473"
###############################################################################

# Houdini Setup ###############################################################
os.environ["HFS"]   = "H:/_distros/hfs.windows-x86_64_" + VERSION_HOUDINI
os.environ["PATH"]  = os.environ['HFS'] + "/bin;" + os.environ["PATH"]
os.environ["HSITE"] = "H:/SITE"
os.environ["HOUDINI_SPLASH_FILE"] = os.environ["HSITE"] + "/houdini16.5/pic/houdinisplash1.png"
# os.environ["HOUDINI_SPLASH_MESSAGE"] = "luma animation 2018"
os.environ["HOUDINI_EXTERNAL_HELP_BROWSER"] = "1"
os.environ["HOUDINI_WINDOW_CONSOLE"] = "1"
os.environ["HOUDINI_BUFFEREDSAVE"] = "1"

sys.path.append(os.environ['HFS'] + "/houdini/python%d.%dlibs" % sys.version_info[:2])
os.environ['HOUDINI_SCRIPT_LICENSE'] = 'hescape'
# import hou
###############################################################################

# Houdini MOPS Setup ##########################################################
os.environ["MOPS"] = os.environ["HSITE"] + "/houdini16.5/MOPS"
os.environ["HOUDINI_OTLSCAN_PATH"] = os.environ["MOPS"] + "/otls;@/otls"
###############################################################################

# Houdini qLib Setup ##########################################################
os.environ["QLIB"] = os.environ["HSITE"] + "/houdini16.5/qLib"
os.environ["QOTL"] = os.environ["QLIB"] + "/otls"

os.environ["HOUDINI_OTLSCAN_PATH"] += ";" + os.environ["QOTL"] + "/base"
os.environ["HOUDINI_OTLSCAN_PATH"] += ";" + os.environ["QOTL"] + "/future"
os.environ["HOUDINI_OTLSCAN_PATH"] += ";" + os.environ["QOTL"] + "/experimental"
os.environ["HOUDINI_MENU_PATH"] = os.environ["QLIB"] + "/menu;&"
os.environ["HOUDINI_PATH"] = os.environ["QLIB"] + "$HOUDINI_PATH;&"
###############################################################################

# Redshift Setup ##############################################################
os.environ["REDSHIFT_COREDATAPATH"] = "H:/_distros/Redshift-" + VERSION_REDSHIFT
os.environ["HOUDINI_DSO_ERROR"] = "2"
os.environ["PATH"] = "H:/_distros/Redshift-" + VERSION_REDSHIFT + "/bin;" + os.environ["PATH"]
os.environ["HOUDINI_PATH"] = "H:/_distros/Redshift-" + VERSION_REDSHIFT + "/Plugins/Houdini/" + VERSION_REDSHIFT_PLUGIN + ";&"
###############################################################################

# OCIO Setup ##################################################################
# os.environ["OCIO"] = os.environ["HSITE"] + "/ocio/spi-anim/config.ocio"
