from comp_00_base import *

###################################################################################################
def comp():
    template_comp   = root + '/' + settings['fairway']['comp']
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
                            player_range = settings['players']
                            for player_num in range(player_range[0], player_range[1] + 1):
                                # START HERE ######################################
                                player = 'player_%d' % player_num
                                var_name = '%s_%s_%s_%s_%s' % (par, fairway, pass_vary, flag, player)
                                print '#'*80
                                print 'Comping "%s".' % var_name
                                print 'Current working directory : %s' % cwd
                                ###################################################
                                print '\tCopying comp from template.'
                                comp = root + '/comps/fairway/' + pass_vary + '/' + var_name + '.nk'
                                if not os.path.exists(os.path.dirname(comp)):
                                    os.makedirs(os.path.dirname(comp))
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
                                out['file_type'].setValue('png')
                                vid = root + '/videos/' + date + '/fairway/' + pass_vary + '/' + var_name + '/' + var_name + '.%04d.png'
                                out['file'].setValue(vid)
                                out['create_directories'].setValue(1)
                                if not os.path.exists(os.path.dirname(vid)):
                                    os.makedirs(os.path.dirname(vid))
                                if pass_vary == 'lineup':
                                    loop = nuke.toNode('luma_golf_loop')
                                    loop['disable'].setValue(0)
                                    # AUDIO
                                    audio_file = root + '/' + settings['audio'] + '/fairway/lineup/fairway_lineup.wav'
                                    aud = open(os.path.dirname(vid) + '/aud', 'w')
                                    aud.write(audio_file)
                                    aud.close()
                                    print '\tAUDIO : %s.' % audio_file
                                if pass_vary == 'swing':
                                    # AUDIO
                                    import random
                                    audio_file  = root + '/' + settings['audio'] + '/fairway/swing/fairway_swing_'
                                    audio_file += str(random.randint(1, 5)) + '.wav'
                                    aud = open(os.path.dirname(vid) + '/aud', 'w')
                                    aud.write(audio_file)
                                    aud.close()
                                    print '\tAUDIO : %s.' % audio_file
                                ###################################################
                                passes = settings['fairway']['passes_common']
                                for pas in passes:
                                    if pas == 'flag_?':
                                        pas = flag
                                        nod = pas[:-2]
                                        update_path(cwd, nod, pas)
                                    elif pas == 'flag_shadow_?':
                                        pas = flag.split('_')[0] + '_shadow_' + flag.split('_')[1]
                                        nod = pas[:-2]
                                        update_path(cwd, nod, pas)
                                    else :
                                        nod = pas
                                        update_path(cwd, nod, pas)
                                        if pass_vary == 'lineup':
                                            nod = nuke.toNode('ball')
                                            nod['first'].setValue(1)
                                            nod['last'].setValue(1)
                                            nod['origfirst'].setValue(1)
                                            nod['origlast'].setValue(1)
                                            nod = nuke.toNode('ball_shadow')
                                            nod['first'].setValue(1)
                                            nod['last'].setValue(1)
                                            nod['origfirst'].setValue(1)
                                            nod['origlast'].setValue(1)
                                            nod = nuke.toNode('tracer_merge')
                                            nod['disable'].setValue(1)
                                ###################################################
                                passes = settings['fairway']['passes_vary']['_' + pass_vary]
                                for pas in passes:
                                    pas = pas[:-1] + str(player_num)
                                    nod = pas[:-2]
                                    update_path(cwd + '/_' + pass_vary, nod, pas)
                                ###################################################
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

    passes_vary = settings['fairway']['passes_vary']
    for par in range(3, 6):
        for pass_vary in passes_vary:
            pass_vary = pass_vary[1:]
            frames = settings['fairway']['frame_range']['_' + pass_vary]
            frames = [int(frames[0]), int(frames[1])]
            list_of_comps = glob.glob(root + '/comps/fairway/' + pass_vary + '/par_' + str(par) + '*.nk')
            list_of_comps = ' '.join(list_of_comps)
            list_of_comps = list_of_comps.replace('\\', '/')
            cmd = rpcmd
            cmd += ' -nj_name "%s"' % ('GOLF : COMP - fairway_' + pass_vary + '_par_' + str(par))
            cmd += ' -nj_tags "VSE"'
            cmd += ' -nj_priority 5'
            cmd += ' -nj_renderer "Nuke v11.2v4/Default version"'
            cmd += ' -nj_preset "H:/_distros/_lumatools/lumatools/_NEILL/src/nuke/golf/presets/golf_preset.rnjprs"'
            cmd += ' -nj_pools "nuke"'
            cmd += ' -frames "%s-%s"' % (frames[0], frames[1])
            cmd += ' -outdir "%s"' % (root + '/videos/' + date + '/fairway/' + pass_vary + '/')
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
