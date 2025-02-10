# Blender Plugin (example)
import bpy
import requests
import json

class DCC_Panel(bpy.types.Panel):
    bl_label = "DCC Integration"
    bl_idname = "OBJECT_PT_dcc"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tools"

    def draw(self, context):
        layout = self.layout
        obj = context.object

        # Object Selection (using active object)
        if obj:
            layout.label(text=f"Selected: {obj.name}")
        else:
            layout.label(text="No object selected")

        # Transform Controls (example - adapt as needed)
        row = layout.row()
        row.prop(obj, "location")
        # ... similar for rotation and scale

        # Endpoint Dropdown
        endpoints = ["/transform", "/translation", "/rotation", "/scale"]
        layout.prop(context.scene, "dcc_endpoint", text="Endpoint")

        # Submit Button
        layout.operator("object.dcc_submit")

class DCC_Submit(bpy.types.Operator):
    bl_idname = "object.dcc_submit"
    bl_label = "Submit to Server"

    def execute(self, context):
        obj = context.object
        if obj:
            endpoint = context.scene.dcc_endpoint
            transform_data = {
                "position": obj.location[:],
                "rotation": obj.rotation_euler[:],  # Or quaternion if used
                "scale": obj.scale[:],
            }
            try:
                response = requests.post(f"[http://127.0.0.1:5000](https://www.google.com/search?q=http://127.0.0.1:5000){endpoint}", json=transform_data) # Server URL
                print(response.json()) # Handle server response
            except requests.exceptions.RequestException as e:
                print(f"Error sending data: {e}")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(DCC_Panel)
    bpy.utils.register_class(DCC_Submit)
    bpy.types.Scene.dcc_endpoint = bpy.props.EnumProperty(items=[(ep, ep, "") for ep in ["/transform", "/translation", "/rotation", "/scale"]])

def unregister():
    bpy.utils.unregister_class(DCC_Panel)
    bpy.utils.unregister_class(DCC_Submit)
    del bpy.types.Scene.dcc_endpoint

if __name__ == "__main__":
    register()
