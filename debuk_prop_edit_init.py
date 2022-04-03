bl_info = {
    "name": "Debuk PropEditInit",
    "description": "Initiates Proportional Editing Radius",
    "author": "Debuk",
    "version": (1, 0, 0),
    'license': 'GPL v3',
    "blender": (2, 80, 0),
    "support": "COMMUNITY",
    "category": "Object"
}

import bpy
from bpy.app.handlers import persistent


@persistent
def load_handler(dummy):
    bpy.context.scene.tool_settings.proportional_size = 0.1


def register():
    bpy.app.handlers.load_post.append(load_handler) 


def unregister():
    bpy.app.handlers.load_post.remove(load_handler)
