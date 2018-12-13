from comp_00_base import *

###############################################################################
def update_path_local(cwd, nod, pas):
    nod = nuke.toNode(nod)
    seq = cwd + '/' + pas + '/' + pas[6:] + '.%04d.exr'
    print seq
    frameS = 1
    frameE = 1

    files = glob.glob(seq[:-8] + '*')
    if len(files) == 0:
        print '\t\t\tSequence doesn\'t exist.'
        seq = missing_footage
        nod['premultiplied'].setValue(1)
    else:
        frameS = int(files[ 0].split('.')[-2])
        frameE = int(files[-1].split('.')[-2])

    nod['file'].setValue(seq)
    nod['first'    ].setValue(frameS)
    nod['last'     ].setValue(frameE)
    nod['origfirst'].setValue(frameS)
    nod['origlast' ].setValue(frameE)

    print '\t|-----o Updated path for pass - %s' % pas
###############################################################################

###################################################################################################
def comp():
    template_comp   = root + '/' + settings['putt']['comp']
    folders_par     = os.listdir(root)
    for par in folders_par:
        if 'par' in par:
            folders_putt = os.listdir(root + '/' + par)
            for putt in folders_putt:
                if 'putt_' in putt:
                    cwd = root + '/' + par + '/' + putt
                    passes_vary = settings['putt']['passes_vary']
                    for pass_vary in passes_vary:
                        pass_vary = pass_vary[1:]
                        flags = glob.glob(cwd + '/_' + pass_vary + '/flag_?')
                        for flag in flags:
                            flag = os.path.basename(flag)
                            list_of_pos = []
                            pos_folders = glob.glob(cwd + '/_' + pass_vary + '/' + flag + '/pos_?_*')
                            for i in pos_folders:
                                list_of_pos.append(os.path.basename(i)[:5])
                            list_of_pos = set(list_of_pos)
                            list_of_pos = sorted(list_of_pos)
                            for pos in list_of_pos:
                                player_range = settings['players']
                                for player_num in range(player_range[0], player_range[1] + 1):
                                    # START HERE ######################################
                                    player = 'player_%d' % player_num
                                    var_name = '%s_%s_%s_%s_%s_%s' % (par, putt, pass_vary, flag, pos, player)
                                    print '#'*80
                                    print 'Comping "%s".' % var_name
                                    print 'Current working directory : %s' % cwd
                                    ###################################################
                                    print '\tCopying comp from template.'
                                    comp = root + '/comps/putt/' + pass_vary + '/' + var_name + '.nk'
                                    if not os.path.exists(os.path.dirname(comp)):
                                        os.makedirs(os.path.dirname(comp))
                                    shutil.copy(template_comp, comp)
                                    ###################################################
                                    print '\tSetting global comp settings.'
                                    nuke.scriptOpen(comp)
                                    nuke.frame(1)
                                    frames = settings['putt']['frame_range']['_' + pass_vary]
                                    frames = [int(frames[0]), int(frames[1])]
                                    nuke.root()['first_frame'].setValue(frames[0])
                                    nuke.root()['last_frame' ].setValue(frames[1])
                                    nuke.root()['fps'].setValue(30)
                                    out = nuke.toNode('OUT')
                                    out['file_type'].setValue('png')
                                    vid = root + '/videos/' + date + '/putt/' + pass_vary + '/' + var_name + '/' + var_name + '.%04d.png'
                                    out['file'].setValue(vid)
                                    out['create_directories'].setValue(1)
                                    if not os.path.exists(os.path.dirname(vid)):
                                        os.makedirs(os.path.dirname(vid))
                                    if pass_vary == 'lineup':
                                        loop = nuke.toNode('luma_golf_loop')
                                        loop['disable'].setValue(0)
                                        # AUDIO
                                        audio_file = root + '/' + settings['audio'] + '/putt/lineup/putt_lineup.wav'
                                        aud = open(os.path.dirname(vid) + '/aud', 'w')
                                        aud.write(audio_file)
                                        aud.close()
                                        print '\tAUDIO : %s.' % audio_file
                                    if pass_vary == 'swing':
                                        # AUDIO
                                        import random
                                        audio_file = root + '/' + settings['audio'] + '/putt/swing/putt_swing_'
                                        audio_file += str(random.randint(1, 5)) + '.wav'
                                        aud = open(os.path.dirname(vid) + '/aud', 'w')
                                        aud.write(audio_file)
                                        aud.close()
                                        print '\tAUDIO : %s.' % audio_file
                                    ###################################################
                                    passes = settings['putt']['passes_common']
                                    for pas in passes:
                                        nod = pas
                                        update_path(cwd, nod, pas)
                                    ###################################################
                                    passes = settings['putt']['passes_vary']['_' + pass_vary]
                                    for pas in passes:
                                        lcwd = cwd + '/_' + pass_vary + '/' + flag
                                        if 'flag' in pas:
                                            pas = pas[:-1] + flag[-1]
                                            nod = pas[:-2]
                                            update_path(lcwd, nod, pas)
                                        else:
                                            if 'ball' in pas:
                                                pas = pas[:-1] + flag[-1]
                                                nod = pas[:-2]
                                                pas = pos + '_' + pas
                                                update_path_local(lcwd, nod, pas)
                                            else:
                                                pas = pas[:-1] + str(player_num)
                                                nod = pas[:-2]
                                                pas = pos + '_' + pas
                                                update_path_local(lcwd, nod, pas)
                                    # ###################################################
                                    print '\tSaving comp and closing nuke.'
                                    nuke.scriptSave(comp)
                                    nuke.scriptClose()
                                    ###################################################
                                    print 'DONE!\n'
                                    if settings['single_run']:
                                        exit(0)
                                    ###################################################
###################################################################################################

###################################################################################################
def submit():
    print 'Sending comp to RenderPal.'
    rpcmd = '"' + os.environ['RP_CMDRC_DIR'] + 'RpRcCmd.exe"'

    passes_vary = settings['putt']['passes_vary']
    for par in range(3, 6):
        for pass_vary in passes_vary:
            pass_vary = pass_vary[1:]
            frames = settings['putt']['frame_range']['_' + pass_vary]
            frames = [int(frames[0]), int(frames[1])]
            list_of_comps = glob.glob(root + '/comps/putt/' + pass_vary + '/par_' + str(par) + '*.nk')
            list_of_comps = ' '.join(list_of_comps)
            list_of_comps = list_of_comps.replace('\\', '/')
            cmd = rpcmd
            cmd += ' -nj_name "%s"' % ('GOLF : COMP - putt_' + pass_vary + '_par_' + str(par))
            cmd += ' -nj_tags "VSE"'
            cmd += ' -nj_priority 5'
            cmd += ' -nj_renderer "Nuke v11.2v4/Default version"'
            cmd += ' -nj_preset "H:/_distros/_lumatools/lumatools/_NEILL/src/nuke/golf/presets/golf_preset.rnjprs"'
            cmd += ' -nj_pools "nuke"'
            cmd += ' -frames "%s-%s"' % (frames[0], frames[1])
            cmd += ' -outdir "%s"' % (root + '/videos/' + date + '/putt/' + pass_vary + '/')
            cmd += ' %s' % list_of_comps
            print cmd
            os.system('"' + cmd + '"')
###################################################################################################

###################################################################################################
def main():
    if settings['comp'  ]:
        comp()
    if settings['submit']:
        submit()
###################################################################################################
if __name__ == '__main__':
    main()
