from comp_base import *

###################################################################################################
def reaction_comp():
    template_comp   = root + '/' + settings['reaction']['comp']
    folders_par     = os.listdir(root)
    for par in folders_par:
        if 'par' in par:
            folders_reaction = os.listdir(root + '/' + par)
            for reaction in folders_reaction:
                if 'reaction_' in reaction:
                    cwd = root + '/' + par + '/' + reaction
                    passes_vary = settings['reaction']['passes_vary']
                    for pass_vary in passes_vary:
                        for player_num in range(1, 7):
                            # START HERE ######################################
                            player = 'player_%d' % player_num
                            var_name = '%s_%s_%s_%s' % (par, reaction, pass_vary, player)
                            print '#'*80
                            print 'Comping "%s".' % var_name
                            print 'Current working directory : %s' % cwd
                            ###################################################
                            print '\tCopying comp from template.'
                            comp = root + '/comps/reaction/' + pass_vary + '/' + var_name + '.nk'
                            if not os.path.exists(os.path.dirname(comp)):
                                os.makedirs(os.path.dirname(comp))
                            shutil.copy(template_comp, comp)
                            ###################################################
                            print '\tSetting global comp settings.'
                            nuke.scriptOpen(comp)
                            nuke.frame(1)
                            frames = settings['reaction']['frame_range'][pass_vary]
                            frames = [int(frames[0]), int(frames[1])]
                            nuke.root()['first_frame'].setValue(frames[0])
                            nuke.root()['last_frame' ].setValue(frames[1])
                            nuke.root()['fps'].setValue(30)
                            out = nuke.toNode('OUT')
                            vid = root + '/videos/reaction/' + pass_vary + '/' + var_name + '.mov'
                            out['file'].setValue(vid)
                            out['create_directories'].setValue(1)
                            ###################################################
                            passes = settings['reaction']['passes_common']
                            for pas in passes:
                                nod = pas
                                update_path(cwd, nod, pas)
                            ###################################################
                            passes = settings['reaction']['passes_vary'][pass_vary]
                            for pas in passes:
                                pas = pas[:-1] + str(player_num)
                                nod = pas[:-2]
                                update_path(cwd, nod, pas)
                            ###################################################
                            print '\tSaving comp and closing nuke.'
                            nuke.scriptSave(comp)
                            nuke.scriptClose()
                            ###################################################
                            print 'DONE!\n'
                            ###################################################
###################################################################################################

###################################################################################################
def reaction_submit():
    print 'Sending comp to RenderPal.'
    rpcmd = '"' + os.environ['RP_CMDRC_DIR'] + 'RpRcCmd.exe"'

    passes_vary = settings['reaction']['passes_vary']
    for par in range(3, 6):
        for pass_vary in passes_vary:
            frames = settings['reaction']['frame_range'][pass_vary]
            frames = [int(frames[0]), int(frames[1])]
            list_of_comps = glob.glob(root + '/comps/reaction/' + pass_vary + '/par_' + str(par) + '*.nk')
            list_of_comps = ' '.join(list_of_comps)
            list_of_comps = list_of_comps.replace('\\', '/')
            cmd = rpcmd
            cmd += ' -nj_name "%s"' % ('GOLF : COMP - reaction_' + pass_vary + '_par_' + str(par))
            cmd += ' -nj_tags "VSE"'
            cmd += ' -nj_priority 5'
            cmd += ' -nj_renderer "Nuke v11.2v4/Default version"'
            cmd += ' -nj_pools "nuke"'
            cmd += ' -nj_paused'
            cmd += ' -frames "%s-%s"' % (frames[0], frames[1])
            cmd += ' -outdir "%s"' % (root + '/videos/reaction/' + pass_vary + '/')
            cmd += ' %s' % list_of_comps
            # tmp_path = os.environ['TEMP'] + '/la_golf_comp_fairway.cmd'
            # tmp_file = open(tmp_path, 'w')
            # tmp_file.write(cmd)
            # tmp_file.close()
            # os.system(tmp_path)
            print cmd
            os.system('"' + cmd + '"')
###################################################################################################

###################################################################################################
def main():
    choice = int(raw_input('Choose wisely : [ (1) Generate comps | (2) Submit to RenderPal | (3) All ] : '))
    if   choice == 1:
        reaction_comp()
    elif choice == 2:
        reaction_submit()
    else:
        reaction_comp()
        reaction_submit()
###################################################################################################
if __name__ == '__main__':
    main()
