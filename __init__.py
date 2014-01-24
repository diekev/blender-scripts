import bpy

from . ui import *
from . barndoors import *
from . cookie import *
from . selectview import *


def register():
    bpy.utils.register_class(ObjectsCreationControls)
    bpy.utils.register_class(BarnDoors)
    bpy.utils.register_class(AddCookie)       
    bpy.utils.register_class(Cookie)
    bpy.utils.register_class(SelectResetView)

def unregister():
    bpy.utils.unregister_class(ObjectsCreationControls)
    bpy.utils.unregister_class(BarnDoors)
    bpy.utils.unregister_class(AddCookie)       
    bpy.utils.unregister_class(Cookie)
    bpy.utils.unregister_class(SelectResetView)
        
if __name__ == "__main__":
    register()  