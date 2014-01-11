import bpy

class ResetCamera(bpy.types.Operator):
    bl_idname = 'reset.camera_as_active'
    bl_label = "Reset Camera"

    bpy.data.scenes["Scene"].camera = bpy.data.objects["Camera"]
    
class SelectResetView(bpy.types.Panel):
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "data"
    bl_label = "Look Through Selected"
    bl_options = {'DEFAULT_CLOSED'} 
    
    @classmethod
    def poll(cls, context):
        lamp = context.lamp
        return (lamp)
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        
        row.operator("view3d.object_as_camera", text = 'Look Through Selected')
        row.operator("reset.camera_as_active", text = 'Reset Camera')
        
def register():
    bpy.utils.register_module(__name__)
    
def unregister():
    bpy.utils.unregister_module(__name__)
    
if __name__ == "__main__":
    register()