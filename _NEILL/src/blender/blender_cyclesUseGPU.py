import bpy
bpy.context.user_preferences.addons['cycles'].preferences.compute_device_type = 'CUDA'
size = len(bpy.context.user_preferences.addons['cycles'].preferences.devices)
for device in range(0, size):
    name   = bpy.context.user_preferences.addons['cycles'].preferences.devices[device].name
    in_use = bpy.context.user_preferences.addons['cycles'].preferences.devices[device].use
    print('Current = %s = %s' % (name, in_use))
    bpy.context.user_preferences.addons['cycles'].preferences.devices[device].use = True
    bpy.ops.wm.save_userpref()
