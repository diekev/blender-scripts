bl_info = {
    "name": "Debug Scene",
    "author": "Kévin Dietrich",
    "version": (1, 0),
    "blender": (2, 77, 1),
    "location": "Properties > Scene",
    "description": "Adds a Panel containing operators to debug scene data",
    "warning": "",
    "wiki_url": "",
    "category": "",
    }

import bpy
import os

from bpy.props import EnumProperty
from bpy.props import StringProperty

def depsgraph_debug_mode_items(self, context):
    """EnumProperty callback"""
    enum_items = []

    if context is None:
        return enum_items

    enum_items.append(("GRAPHVIZ","Graphviz",  "", '', 0))
    enum_items.append(("STATS", "Stats", "Report the number of elements in the Dependency Graph", '', 1))
    enum_items.append(("REBUILD", "Rebuild", "", '', 2))

    return enum_items


class DebugDepsgraphOperator(bpy.types.Operator):
    """Outputs a dot file containing the current's scene dependency graph hierarchy"""
    bl_idname = "scene.debug_depsgraph"
    bl_label = "Debug Depsgraph"

    @classmethod
    def poll(cls, context):
        return context.scene is not None

    def execute(self, context):
        scene = context.scene
        debug_mode = scene.depsgraph_debug_mode
        depsgraph = scene.depsgraph

        if (debug_mode == 'GRAPHVIZ'):
            base_name = scene.graphviz_file_path
            dot_filename = base_name + ".dot"
            png_filename = base_name + ".png"

            # Dump depsgraph to a dot file.
            depsgraph.debug_graphviz(dot_filename)
        
            # Call dot to convert to a png file.
            cmd = "dot -Tpng %s -o %s" % (dot_filename, png_filename)
            os.system(cmd)

            # Call xdg-open to open the png file.
            cmd = "xdg-open %s" % (png_filename)
            os.system(cmd)
        elif debug_mode == 'STATS':
           depsgraph.debug_stats()
        elif debug_mode == 'REBUILD':
           depsgraph.debug_rebuild()

        return {'FINISHED'}


class DebugPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Debug"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        debug_mode = scene.depsgraph_debug_mode

        layout.prop(scene, "depsgraph_debug_mode", text="Debug Mode")

        row = layout.row()
        row.active = (debug_mode == 'GRAPHVIZ')
        row.prop(scene, "graphviz_file_path", text="File Path")

        layout.operator("scene.debug_depsgraph")


def register():
    from bpy.types import Scene

    Scene.graphviz_file_path = StringProperty(
            name="File Path",
            subtype='FILE_PATH',
            default="/tmp/depsgraph"
            )

    Scene.depsgraph_debug_mode = EnumProperty(
            items=depsgraph_debug_mode_items,
            )

    bpy.utils.register_class(DebugDepsgraphOperator)
    bpy.utils.register_class(DebugPanel)

def unregister():
    bpy.utils.unregister_class(DebugPanel)
    bpy.utils.unregister_class(DebugDepsgraphOperator)

if __name__ == "__main__":
    register()
