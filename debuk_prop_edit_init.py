bl_info = {
    "name": "Debuk PropEditInit",
    "description": "Initiates Proportional Editing Radius",
    "author": "Debuk",
    "version": (1, 0, 1),
    'license': 'GPL v3',
    "blender": (2, 80, 0),
    "support": "COMMUNITY",
    "category": "Object"
}

import bpy
from bpy.types import AddonPreferences
from bpy.app.handlers import persistent
from bpy.props import FloatProperty

class DebukPropEditInitAddonPreferences(AddonPreferences):
    bl_idname = __name__
    
    
    def rad_upd(self, context):
        bpy.context.scene.tool_settings.proportional_size = self.prop_edit_radius
    
    prop_edit_radius: FloatProperty(
        name ="Prop Edit radius",
        default=0.1,
        min = 0.01,
        max = 10,
        precision=2,
        update=rad_upd
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "prop_edit_radius")

        
@persistent
def load_handler(dummy):

    addon_prefs = bpy.context.preferences.addons["debuk_prop_edit_init"].preferences
    bpy.context.scene.tool_settings.proportional_size = addon_prefs.prop_edit_radius

def register():
    bpy.utils.register_class(DebukPropEditInitAddonPreferences)
    bpy.app.handlers.load_post.append(load_handler) 

def unregister():
    bpy.app.handlers.load_post.remove(load_handler)
    bpy.utils.register_class(DebukPropEditInitAddonPreferences)