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

    from_pydata([(-1.0, -1.0, 0.0), (1.0, -1.0, 0.0), (-1.0, 1.0, 0.0), (1.0, 1.0, 0.0), (-3.17727, 3.17981, -0.04091), (-4.49474, 0.00163, -0.07223), (-3.17925, -3.1775, -0.06124), (-0.0014, -4.4953, -0.01438), (3.17727, -3.17981, 0.04091), (4.49474, -0.00163, 0.07223), (3.17925, 3.1775, 0.06124), (0.0014, 4.4953, 0.01438), (-1.0, 0.0, 0.0), (0.0, -1.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0)],[(12, 0), (13, 1), (14, 3), (15, 2), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9), (11, 10), (4, 11), (12, 2), (13, 0), (14, 1), (15, 3), (2, 4), (11, 15), (3, 10), (14, 9), (5, 12), (0, 6), (7, 13), (1, 8)],[(14, 9, 10, 3), (10, 11, 15, 3), (15, 11, 4, 2), (4, 5, 12, 2), (12, 5, 6, 0), (6, 7, 13, 0), (13, 7, 8, 1), (8, 9, 14, 1)])

    
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
