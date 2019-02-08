import la_utils

cmd  = 'python'
cmd += ' H:/_distros/Nuke11.3v1/pythonextensions/site-packages/foundry/frameserver/nuke/runframeserver.py'
# cmd += ' --useInteractiveLicense'
cmd += ' --numworkers=2'
cmd += ' --nukeworkerthreads=4'
cmd += ' --nukeworkermemory=16192'
cmd += ' --workerconnecturl=tcp://192.168.35.195:5560'
cmd += ' --nukepath=H:/_distros/Nuke11.3v1/Nuke11.3.exe'
print cmd
la_utils.runCmd(cmd)
