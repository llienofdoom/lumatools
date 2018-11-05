from comp_base import *

root            = settings['root']
template_comp   = root + '/' + settings['fairway']['comp']
missing_footage = root + '/' + settings['standin']
folders_par     = os.listdir(root)

for par in folders_par:
    if 'par' in par:
        folders_fairway = os.listdir(root + '/' + par)
        for fairway in folders_fairway:
            if 'fairway_' in fairway:
                cwd = root + '/' + par + '/' + fairway
                flags = glob.glob(cwd + '/' + 'flag_?')
                for flag in flags:
                    flag = os.path.basename(flag)
                    passes_vary = settings['fairway']['passes_vary']
                    for pass_vary in passes_vary:
                        pass_vary = pass_vary[1:]
                        for player_num in range(1, 7):
                            # START HERE ######################################
                            player = 'player_%d' % player_num
                            var_name = '%s_%s_%s_%s_%s' % (par, fairway, pass_vary, flag, player)
                            print '#'*80
                            print 'Comping "%s".' % var_name
                            print 'Current working directory : %s' % cwd
                            ###################################################
                            print '\tCopying comp from template.'
                            comp = root + '/comps/' + var_name + '.nk'
                            shutil.copy(template_comp, comp)
                            ###################################################
                            print '\tSetting global comp settings.'
                            nuke.scriptOpen(comp)
                            nuke.frame(1)
                            frames = settings['fairway']['frame_range']['_' + pass_vary]
                            frames = [int(frames[0]), int(frames[1])]
                            nuke.root()['first_frame'].setValue(frames[0])
                            nuke.root()['last_frame' ].setValue(frames[1])
                            nuke.root()['fps'].setValue(30)
                            out = nuke.toNode('OUT')
                            vid = root + '/videos/' + var_name + '.mov'
                            out['file'].setValue(vid)
                            out['create_directories'].setValue(1)
                            if pass_vary == 'lineup':
                                loop = nuke.toNode('luma_golf_loop')
                                loop['disable'].setValue(0)


#############################################################################################################
                            ###################################################
                            passes_common = settings['fairway']['passes_common']
                            for current_pass in passes_common:
                                node     = ''
                                sequence = ''
                                if current_pass == 'flag_?':
                                    current_pass = flag
                                    node = nuke.toNode(current_pass[:-2])
                                    sequence = cwd + '/' + current_pass + '/' + current_pass + '.%04d.exr'
                                elif current_pass == 'flag_shadow_?':
                                    current_pass = flag.split('_')[0] + '_shadow_' + flag.split('_')[1]
                                    node = nuke.toNode(current_pass[:-2])
                                    sequence = cwd + '/' + current_pass + '/' + current_pass + '.%04d.exr'
                                elif (current_pass == 'sky') or (current_pass == 'plate') :
                                    node = nuke.toNode(current_pass)
                                    sequence = cwd + '/' + current_pass + '/' + current_pass + '.0001.exr'
                                else :
                                    node = nuke.toNode(current_pass)
                                    sequence = cwd + '/' + current_pass + '/' + current_pass + '.%04d.exr'
                                path_check = sequence[:-8] + '%04d.exr' % frames[0]
                                if not (os.path.exists(path_check)):
                                    print '\t\t\tSequence doesn\'t exist.'
                                    sequence = missing_footage
                                    node['premultiplied'].setValue(1)
                                else:
                                    node_frameS = int(glob.glob(sequence[:-8] + '*')[0].split('.')[-2])
                                    node_frameE = int(glob.glob(sequence[:-8] + '*')[-1].split('.')[-2])
                                node['file'].setValue(sequence)
                                node['first'].setValue(frames[0])
                                node['last'].setValue(frames[1])
                                print '\t|-----o Updated path for common pass   - %s' % current_pass
                            ###################################################
                            player_cm     = player.split('_')[0] + '_cm_'     + player.split('_')[1]
                            player_shadow = player.split('_')[0] + '_shadow_' + player.split('_')[1]
                            ###################################################
                            node = nuke.toNode('player')
                            sequence = cwd + '/' + player + '/' + player + '.%04d.exr'
                            path_check = sequence[:-8] + '%04d.exr' % frames[0]
                            if not (os.path.exists(path_check)):
                                print '\t\t\tSequence doesn\'t exist.'
                                sequence = missing_footage
                                node['premultiplied'].setValue(1)
                            node['file'].setValue(sequence)
                            node['first'].setValue(frames[0])
                            node['last'].setValue(frames[1])
                            print '\t|-----o Updated path for player        - %s' % player
                            ###################################################
                            node = nuke.toNode('player_cm')
                            sequence = cwd + '/' + player_cm + '/' + player_cm + '.%04d.exr'
                            path_check = sequence[:-8] + '%04d.exr' % frames[0]
                            if not (os.path.exists(path_check)):
                                print '\t\t\tSequence doesn\'t exist.'
                                sequence = missing_footage
                                node['premultiplied'].setValue(1)
                            node['file'].setValue(sequence)
                            node['first'].setValue(frames[0])
                            node['last'].setValue(frames[1])
                            print '\t|-----o Updated path for player_cm     - %s' % player_cm
                            ###################################################
                            node = nuke.toNode('player_shadow')
                            sequence = cwd + '/' + player_shadow + '/' + player_shadow + '.%04d.exr'
                            path_check = sequence[:-8] + '%04d.exr' % frames[0]
                            if not (os.path.exists(path_check)):
                                print '\t\t\tSequence doesn\'t exist.'
                                sequence = missing_footage
                                node['premultiplied'].setValue(1)
                            node['file'].setValue(sequence)
                            node['first'].setValue(frames[0])
                            node['last'].setValue(frames[1])
                            print '\t|-----o Updated path for player_shadow - %s' % player_shadow

#############################################################################################################

                            ###################################################
                            print '\tSaving comp and closing nuke.'
                            nuke.scriptSave(comp)
                            nuke.scriptClose()
                            exit(0)
                            ###################################################
                            print '\tSending comp to RenderPal.'
                            # TODO ############################################
                            ###################################################
                            print '\tCleaning up.'
                            # TODO ############################################
                            print 'DONE!\n'
                            ###################################################




                #     rpcmd = '"' + os.environ['RP_CMDRC_DIR'] + 'RpRcCmd.exe"'
                #     cmd = rpcmd
                #     cmd += ' -nj_name "%s"' % ( 'GOLF : ' + fairway_loop + '.nk' )
                #     cmd += ' -nj_tags "VSE"'
                #     cmd += ' -nj_priority 5'
                #     cmd += ' -nj_renderer "Nuke v11.2v4/Default version"'
                #     cmd += ' -nj_preset "H:\\_distros\\_lumatools\\lumatools\\_NEILL\\src\\nuke\\golf\\golf_convert.rnjprs"'
                #     cmd += ' -nj_pools "nuke"'
                #     cmd += ' -nj_paused'
                #     cmd += ' -frames "%s-%s"' % (frame_range[0], frame_range[1])
                #     cmd += ' -outfile "%s"' % vid
                #     cmd += ' %s' % comp
                #     print cmd
                #     njid = os.system('"' + cmd + '"')
                #     frame_range = []
