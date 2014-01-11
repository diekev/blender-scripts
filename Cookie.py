import bpy
from bpy.props import BoolProperty, FloatProperty

class ObjectsCreationControls(bpy.types.PropertyGroup):
    
    UseCookie = bpy.props.BoolProperty(
        description="Enable use of cookie",
        default=False) 

class AddCookie(bpy.types.Operator):
    mesh = bpy.ops.mesh
    
    mesh.primitive_plane_add()
    bpy.context.object.name = "Cookie"
    bpy.context.object.parent = bpy.data.objects["Spot"]

class Cookie(bpy.types.Panel):
    
    bl_idname = "panel.Cookie"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "data"
    bl_label = "Cookie"
    bl_options = {'DEFAULT_CLOSED'}
      
    @classmethod
    def poll(cls, context):
        return context.lamp 
    
    def draw_header(self, context):
        lamp = context.lamp
        self.layout.prop(lamp, "UseCookie", text="")
    
    def draw(self, context):
        layout = self.layout

def register():
    bpy.utils.register_class(ObjectsCreationControls)
    bpy.utils.register_class(AddCookie)       
    bpy.utils.register_class(Cookie)

def unregister():
    bpy.utils.unregister_class(ObjectsCreationControls)
    bpy.utils.unregister_class(AddCookie)       
    bpy.utils.unregister_class(Cookie)

if __name__ == "__main__":
    register()
