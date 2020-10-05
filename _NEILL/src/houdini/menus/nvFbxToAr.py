import os
import hou

def nvFbxToAr(root_node):
    for child in root_node.children():
        node_type = child.type().name()
        if node_type == 'geo':
            orig_mat_path = child.parm('shop_materialpath').eval()
            if orig_mat_path != '':
                print 'OBJ  = ' + child.name()
                print 'MAT  = ' + orig_mat_path
                orig_mat = hou.node(orig_mat_path)
                old_path = os.path.dirname(orig_mat_path)
                old_name = os.path.basename(orig_mat_path)
                new_path = old_path + '_ARNOLD'
                new_name = 'sdr_ar_' + old_name
                print 'MATn = ' + new_path + '/' + new_name
                new_matnet = None
                new_mat    = None
                if hou.node(new_path) == None:
                    print 'New Arnold matnet not found, creating...'
                    new_matnet = root_node.createNode('matnet', os.path.basename(new_path))
                else:
                    print 'New Arnold matnet found, skipping creation...'
                    new_matnet = hou.node(new_path)
                if hou.node(new_path + '/' + new_name) == None:
                    print 'New Arnold Material not found, creating...'
                    new_mat = new_matnet.createNode('arnold_materialbuilder', new_name)
                    output  = new_mat.children()[0]
                    surface = new_mat.createNode('arnold::standard_surface')
                    output.setInput(0, surface, 0)
                    # make other nodes and set values
                    orig_parms = orig_mat.parms()
                    for parm in orig_parms:
                        default = parm.isAtDefault()
                        if not default:
                            print '  * ' + parm.name() + ' : ' + str(parm.eval())
                            if 'basecolorr'         in parm.name():
                                surface.parm('base_colorr').set(parm.eval())
                                print '    - updated.'
                            if 'basecolorg'         in parm.name():
                                surface.parm('base_colorg').set(parm.eval())
                                print '    - updated.'
                            if 'basecolorb'         in parm.name():
                                surface.parm('base_colorb').set(parm.eval())
                                print '    - updated.'
                            if 'rough'              in parm.name():
                                surface.parm('specular_roughness').set(parm.eval())
                                print '    - updated.'
                            if 'basecolor_texture'  in parm.name():
                                basecolor_texture = new_mat.createNode('arnold::image', 'image_basecolor')
                                basecolor_texture.parm('filename').set(parm.eval())
                                surface.setInput(1, basecolor_texture, 0)
                                print '    - updated.'
                            if 'baseNormal_texture' in parm.name():
                                normal_texture = new_mat.createNode('arnold::image', 'image_normal')
                                normal_texture.parm('filename').set(parm.eval())
                                normal_node = new_mat.createNode('arnold::normal_map', 'normal_map')
                                normal_node.setInput(0, normal_texture, 0)
                                surface.setInput(39, normal_node, 0)
                                print '    - updated.'
                    new_mat.layoutChildren()
                else:
                    print 'New Arnold Material found, skipping.'
                    new_mat = hou.node(new_path + '/' + new_name)
                print 'Setting new material path on object...'
                print child.parm('shop_materialpath').eval() + ' to ' + new_mat.path(),
                child.parm('shop_materialpath').set(new_mat.path())
                print ' updated.'
                child.parm('vm_overridedetail').set(True)
                print 'Ignoring shop_materialpath attr.'
                print '*'*50
                new_matnet.layoutChildren()

root_node = hou.selectedNodes()[0]
nvFbxToAr(root_node)
