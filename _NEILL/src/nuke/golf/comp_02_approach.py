from comp_00_base import *

###################################################################################################
def comp():
    template_comp   = root + '/' + settings['approach']['comp']
    folders_par     = os.listdir(root)
    for par in folders_par:
        if 'par' in par:
            folders_approach = os.listdir(root + '/' + par)
            for approach in folders_approach:
                if 'approach' in approach:
                    cwd = root + '/' + par + '/' + approach
                    flags = glob.glob(cwd + '/' + '_flag_?')
                    for flag in flags:
                        flag = os.path.basename(flag)
                        flag = flag[1:]
                        for ball in range(1, 4):
                            ball = 'ball_%i' % ball
                            # START HERE ######################################
                            var_name = '%s_%s_%s_%s' % (par, approach, flag, ball)
                            print '#'*80
                            print 'Comping "%s".' % var_name
                            print 'Current working directory : %s' % cwd
                            ###################################################
                            print '\tCopying comp from template.'
                            comp = root + '/comps/approach/' + var_name + '.nk'
                            if not os.path.exists(os.path.dirname(comp)):
                                os.makedirs(os.path.dirname(comp))
                            shutil.copy(template_comp, comp)
                            ##################################################
                            print '\tSetting global comp settings.'
                            nuke.scriptOpen(comp)
                            nuke.frame(1)
                            frames = settings['approach']['frame_range']
                            frames = [int(frames[0]), int(frames[1])]
                            nuke.root()['first_frame'].setValue(frames[0])
                            nuke.root()['last_frame' ].setValue(frames[1])
                            nuke.root()['fps'].setValue(30)
                            out = nuke.toNode('OUT')
                            out['file_type'].setValue('png')
                            vid = root + '/videos/' + date + '/approach/' + var_name + '/' + var_name + '.%04d.png'
                            out['file'].setValue(vid)
                            out['create_directories'].setValue(1)
                            if not os.path.exists(os.path.dirname(vid)):
                                os.makedirs(os.path.dirname(vid))
                            # AUDIO
                            import random
                            audio_file  = root + '/' + settings['audio'] + '/approach/approach_'
                            audio_file += str(random.randint(1, 5)) + '.wav'
                            aud = open(os.path.dirname(vid) + '/aud', 'w')
                            aud.write(audio_file)
                            aud.close()
                            print '\tAUDIO : %s.' % audio_file
                            ###################################################
                            passes = settings['approach']['passes_common']
                            for pas in passes:
                                nod = pas
                                update_path(cwd, nod, pas)
                            ###################################################
                            passes = settings['approach']['passes_vary']
                            for pas in passes:
                                if 'ball' in pas:
                                    num = ball[-1:]
                                    pas = pas[:-1] + num
                                    nod = pas[:-2]
                                    update_path(cwd + '/_' + flag, nod, pas)
                                    # tracer
                                    if not 'shadow' in pas:
                                        update_path(cwd + '/_' + flag, 'tracer', pas + '_tracer')
                                if 'flag' in pas:
                                    num = flag[-1:]
                                    pas = pas[:-1] + num
                                    nod = pas[:-2]
                                    update_path(cwd + '/_' + flag, nod, pas)
                            ###################################################
                            print '\tSaving comp and closing nuke.'
                            nuke.scriptSave(comp)
                            nuke.scriptClose()
                            ###################################################
                            print 'DONE!\n'
                            if settings['single_run']:
                                exit(0)
                            ##################################################
###################################################################################################

###################################################################################################
def submit():
    print 'Sending comp to RenderPal.'
    rpcmd = '"' + os.environ['RP_CMDRC_DIR'] + 'RpRcCmd.exe"'

    for par in range(3, 6):
        frames = settings['approach']['frame_range']
        frames = [int(frames[0]), int(frames[1])]
        list_of_comps = glob.glob(root + '/comps/approach/' + '/par_' + str(par) + '*.nk')
        list_of_comps = ' '.join(list_of_comps)
        list_of_comps = list_of_comps.replace('\\', '/')
        cmd = rpcmd
        cmd += ' -nj_name "%s"' % ('GOLF : COMP - approach' + '_par_' + str(par))
        cmd += ' -nj_tags "VSE"'
        cmd += ' -nj_priority 5'
        cmd += ' -nj_renderer "Nuke v11.2v4/Default version"'
        cmd += ' -nj_preset "H:/_distros/_lumatools/lumatools/_NEILL/src/nuke/golf/presets/golf_preset.rnjprs"'
        cmd += ' -nj_pools "nuke"'
        cmd += ' -frames "%s-%s"' % (frames[0], frames[1])
        cmd += ' -outdir "%s"' % (root + '/videos/' + date + '/approach/')
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
