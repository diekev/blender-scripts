import bpy

#create the barndoors objects
class AddBarndoors(bpy.types.Operator):
    mesh = bpy.ops.mesh
    ob = bpy.context.object
     
    mesh.primitive_plane_add()
    ob.name = "Right_Panel"
    ob.parent = bpy.data.objects["Spot"] 
    bpy.ops.transform.translate(value=(2, 0, 0))
    bpy.ops.object.transform_apply(location=True)

    mesh.primitive_plane_add()
    ob.name = "Left_Panel"
    ob.parent = bpy.data.objects["Spot"] 
    bpy.ops.transform.translate(value=(-2, 0, 0))
    bpy.ops.object.transform_apply(location=True)

    mesh.primitive_plane_add()
    ob.name = "Top_Panel"
    ob.parent = bpy.data.objects["Spot"] 
    bpy.ops.transform.translate(value=(0, 2, 0))
    bpy.ops.object.transform_apply(location=True)

    mesh.primitive_plane_add()
    ob.name = "Bottom_Panel"
    ob.parent = bpy.data.objects["Spot"] 
    bpy.ops.transform.translate(value=(0, -2, 0))
    bpy.ops.object.transform_apply(location=True)
    
class AddCookie(bpy.types.Operator):
    mesh = bpy.ops.mesh
    ob = bpy.context.object
    
    mesh.primitive_plane_add()
    ob.name = "Cookie"
    ob.parent = bpy.data.objects["Spot"] 
    
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
    
    def draw(self, context):
        layout = self.layout      
    
class BarnDoors(bpy.types.Panel):
    
    bl_idname = "panel.BarnDoors"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "data"
    bl_label = "Barndoors"
    bl_options = {'DEFAULT_CLOSED'}
    
    @classmethod
    def poll(cls, context):
        lamp = context.lamp
        return (lamp and lamp.type == 'SPOT')
    
    def draw(self, context):
        layout = self.layout
        lamp = context.lamp
        col = layout.column()
        split = layout.split()
        
        col.label(text="Barndoors:")
        
        col = split.column(align=True)  
        col.label(text="Right Panel:")
        col.label(text="Bottom Panel:")
        col.label(text="Left Panel:")
        col.label(text="Top Panel:")
        
        col = split.column(align=True) 
        col.prop(lamp, "spot_size", text="Angle")
        col.prop(lamp, "spot_size", text="Angle")
        col.prop(lamp, "spot_size", text="Angle")
        col.prop(lamp, "spot_size", text="Angle")

def register():
    bpy.utils.register_class(BarnDoors)
    bpy.utils.register_class(Cookie)

def unregister():
    bpy.utils.unregister_class(BarnDoors)
    bpy.utils.unregister_class(Cookie)
    
if __name__ == "__main__":
    register()    
