from comp_base import *

###################################################################################################
def comp():
    template_comp   = root + '/' + settings['reaction_fairway']['comp']
    folders_par     = os.listdir(root)
    for par in folders_par:
        if 'par' in par:
            folders_reaction = os.listdir(root + '/' + par)
            for reaction in folders_reaction:
                if 'reaction_fairway' in reaction:
                    cwd = root + '/' + par + '/' + reaction
                    for player_num in range(1, 2):  ######## TODO FIX ME! After Wedensday 7
                        # START HERE ######################################
                        player = 'player_%d' % player_num
                        var_name = '%s_%s_%s' % (par, reaction, player)
                        print '#'*80
                        print 'Comping "%s".' % var_name
                        print 'Current working directory : %s' % cwd
                        ###################################################
                        print '\tCopying comp from template.'
                        comp = root + '/comps/reaction_fairway/' + var_name + '.nk'
                        if not os.path.exists(os.path.dirname(comp)):
                            os.makedirs(os.path.dirname(comp))
                        shutil.copy(template_comp, comp)
                        ###################################################
                        print '\tSetting global comp settings.'
                        nuke.scriptOpen(comp)
                        nuke.frame(1)
                        frames = settings['reaction_fairway']['frame_range']
                        frames = [int(frames[0]), int(frames[1])]
                        nuke.root()['first_frame'].setValue(frames[0])
                        nuke.root()['last_frame' ].setValue(frames[1])
                        nuke.root()['fps'].setValue(30)
                        out = nuke.toNode('OUT')
                        vid = root + '/videos/' + date + '/reaction_fairway/' + var_name + '.mov'
                        out['file'].setValue(vid)
                        out['create_directories'].setValue(1)
                        ###################################################
                        passes = settings['reaction_fairway']['passes_common']
                        for pas in passes:
                            nod = pas
                            update_path(cwd, nod, pas)
                        ###################################################
                        passes = settings['reaction_fairway']['passes_vary']
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
def submit():
    print 'Sending comp to RenderPal.'
    rpcmd = '"' + os.environ['RP_CMDRC_DIR'] + 'RpRcCmd.exe"'

    for par in range(3, 6):
        frames = settings['reaction_fairway']['frame_range']
        frames = [int(frames[0]), int(frames[1])]
        list_of_comps = glob.glob(root + '/comps/reaction_fairway/par_' + str(par) + '*.nk')
        list_of_comps = ' '.join(list_of_comps)
        list_of_comps = list_of_comps.replace('\\', '/')
        cmd = rpcmd
        cmd += ' -nj_name "%s"' % ('GOLF : COMP - reaction_fairway_par_' + str(par))
        cmd += ' -nj_tags "VSE"'
        cmd += ' -nj_priority 5'
        cmd += ' -nj_renderer "Nuke v11.2v4/Default version"'
        cmd += ' -nj_pools "nuke"'
        # cmd += ' -nj_paused'
        cmd += ' -frames "%s-%s"' % (frames[0], frames[1])
        cmd += ' -outdir "%s"' % (root + '/videos/' + date + '/reaction_fairway/')
        cmd += ' %s' % list_of_comps
        print cmd
        os.system('"' + cmd + '"')
###################################################################################################

###################################################################################################
def main():
    comp()
    submit()
###################################################################################################
if __name__ == '__main__':
    main()
