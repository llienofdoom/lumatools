import settings.luma_site_settings

import os
import hou

###############################################################################
def buildCmdLine():
    rpcmd = '"' + os.environ['RP_CMDRC_DIR'] + 'RpRcCmd.exe"'
    cmd = rpcmd
    cmd += ' -nj_name "test_job1"'
    cmd += ' -nj_project "TEST_JOB"'
    cmd += ' -nj_tags "luma","mantra","testing"'
    cmd += ' -nj_priority 5'
    cmd += ' -nj_renderer GenerateIFD/16.5.473'
    cmd += ' -nj_splitmode 2,1'
    cmd += ' -nj_pools "mantra"'
    # cmd += ' -nj_dependency'
    cmd += ' -nj_paused'
    cmd += ' -retnjid'
    cmd += ' -rop "/bob/bob"'
    cmd += ' -frames "1-100"'
    cmd += ' filename.hip'

    print cmd
    # njid = os.system('"' + cmd + '"')
    # print njid

###############################################################################
def main():
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
    # TESTING
    # for rop in rop_list:
    if True:
        rop = rop_list[0]
    ## TESTING

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
        buildCmdLine()

    hou.releaseLicense()

###############################################################################
# if __name__ == '__main__':
#     main()

buildCmdLine()
