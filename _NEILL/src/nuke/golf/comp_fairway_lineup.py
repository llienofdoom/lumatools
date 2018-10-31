from comp_base import *

# TODO: STANDARDIZE THIS!!!
template = settings['lineup']['template_comp']

path_root     = settings['path_root']
folders_par = os.listdir(path_root)
for par in folders_par:
    if 'par' in par:
        folders_fairway_loops = os.listdir(path_root + os.sep + par)
        for fairway_loop in folders_fairway_loops:
            if 'fairway_' in fairway_loop:
                cwd = path_root + '/' + par + '/' + fairway_loop
                folders_passes = os.listdir(path_root + os.sep + par + os.sep + fairway_loop)
                print cwd
                print folders_passes





                if len(folders_passes) > 0:
                    comp = cwd + '/' + fairway_loop + '.nk'
                    vid = ''
                    frame_range = []
                    print '\nCurrently processing %s.' % comp
                    shutil.copy(template, comp)
                    nuke.scriptOpen(comp)
                    passes = settings['fairway_loop']['passes']
                    # Where the magic happens! ##########################################
                    for node in nuke.allNodes(recurseGroups=True):
                        if node.Class() == 'Read':
                            if node.fullName() in passes:
                                # print node.fullName(), ':', node['file'].value()
                                path = cwd + '/' + node.fullName() + '/' + node.fullName() + '.%04d.exr'
                                if len(frame_range) == 0:
                                    list_of_files = glob.glob( path[:-8] + '????.*' )
                                    first = int(list_of_files[0].split('.')[4])
                                    last  = int(list_of_files[-1].split('.')[4])
                                    frame_range.append(first)
                                    frame_range.append(last)
                                    nuke.root()['first_frame'].setValue(frame_range[0])
                                    nuke.root()['last_frame' ].setValue(frame_range[1])
                                    nuke.root()['fps'].setValue(30)
                                    out = nuke.toNode('OUT')
                                    vid = path_root + '/' + course + '/' + fairway_loop + '.mov'
                                    out['file'].setValue(vid)
                                    # out['file_type'].setValue(6)
                                    # out['meta_codec'].setValue('avc1')
                                    # out['mov32_fps'].setValue(30)
                                    audio = settings['audio'] + '/' '%s_%s.wav' % (course, fairway_loop)
                                    out['mov64_audiofile'].setValue(audio)
                                    out['create_directories'].setValue(1)
                                node['file'].setValue(path)
                                node['first'].setValue(frame_range[0])
                                node['last' ].setValue(frame_range[1])
                    #####################################################################
                    nuke.scriptSave(comp)
                    # nuke.execute('OUT', frame_range[0], frame_range[1])
                    nuke.scriptClose()
                    rpcmd = '"' + os.environ['RP_CMDRC_DIR'] + 'RpRcCmd.exe"'
                    cmd = rpcmd
                    cmd += ' -nj_name "%s"' % ( 'GOLF : ' + fairway_loop + '.nk' )
                    cmd += ' -nj_tags "VSE"'
                    cmd += ' -nj_priority 5'
                    cmd += ' -nj_renderer "Nuke v11.2v4/Default version"'
                    cmd += ' -nj_preset "H:\\_distros\\_lumatools\\lumatools\\_NEILL\\src\\nuke\\golf\\golf_convert.rnjprs"'
                    cmd += ' -nj_pools "nuke"'
                    cmd += ' -nj_paused'
                    cmd += ' -frames "%s-%s"' % (frame_range[0], frame_range[1])
                    cmd += ' -outfile "%s"' % vid
                    cmd += ' %s' % comp
                    print cmd
                    njid = os.system('"' + cmd + '"')
                    frame_range = []
