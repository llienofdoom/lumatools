import os, sys
import shutil
import glob
import la_utils
import nuke

opsys    = la_utils.getOs()
settings = la_utils.readSettings()

template = settings['fairway_loop']['template_comp']
frame_range = []

path_root     = settings['path_root']
folders_courses = os.listdir(path_root)
for course in folders_courses:
    if 'course' in course:
        folders_fairway_loops = os.listdir(path_root + os.sep + course)
        for fairway_loop in folders_fairway_loops:
            if 'fairway_loop' in fairway_loop:
                cwd = path_root + '/' + course + '/' + fairway_loop
                folders_passes = os.listdir(path_root + os.sep + course + os.sep + fairway_loop)
                if len(folders_passes) > 0:
                    comp = cwd + '/' + fairway_loop + '.nk'
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
                                    first = int(list_of_files[0].split('.')[1])
                                    last  = int(list_of_files[-1].split('.')[1])
                                    frame_range.append(first)
                                    frame_range.append(last)
                                    nuke.root()['first_frame'].setValue(frame_range[0])
                                    nuke.root()['last_frame' ].setValue(frame_range[1])
                                    nuke.root()['fps'].setValue(30)

                                node['file'].setValue(path)

                    #####################################################################
                    nuke.scriptSave(comp)
                    nuke.scriptClose()


                # else:
                #     print 'Skipping %s. Empty.\n' % cwd

# nuke.execute( nodeName, firstFrame, lastFrame )