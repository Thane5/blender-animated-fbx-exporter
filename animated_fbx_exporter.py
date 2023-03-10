bl_info = {
    "name": "Animated FBX Exporter",
    "author": "Thane5",
    "version": (1, 0),
    "blender": (3, 4, 1),
    "location": "View3D > UI > Animation Export",
    "description": "Export FBX files with and without animations.",
    "warning": "",
    "doc_url": "",
    "category": "Import-Export",
}

import bpy

class FBXExporterPanel(bpy.types.Panel):
    bl_label = "Animated FBX Exporter"
    bl_idname = "VIEW3D_PT_fbx_exporter"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Animation Export"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.prop(context.scene, "fbx_export_folder", text="Path")

        row = layout.row()
        row.operator("export.fbx_export_without_animation", text="Export Without Animations")

        row = layout.row()
        row.operator("export.fbx_export_single_animation", text="Export Only Active Animation")

        row = layout.row()
        row.operator("export.fbx_export_all", text="Export With All Animations")

def get_export_file_path():
    folder_path = bpy.context.scene.fbx_export_folder

    file_name = bpy.context.active_object.name

    return f"{folder_path}/{file_name}.fbx"

def get_export_file_path_with_action():
    folder_path = bpy.context.scene.fbx_export_folder

    current_action_name = bpy.context.active_object.animation_data.action.name
    
    file_name = bpy.context.active_object.name + f"_{current_action_name}"

    return f"{folder_path}/{file_name}.fbx"

class FBXExportWithoutAnimationOperator(bpy.types.Operator):
    bl_idname = "export.fbx_export_without_animation"
    bl_label = "Export Without Animation"

    def execute(self, context):
        bpy.ops.export_scene.fbx(
            filepath=get_export_file_path(),
            use_selection=True,
            bake_anim_use_nla_strips=True,
            bake_anim_use_all_actions=False
        )

        return {'FINISHED'}

class FBXExportSingleAnimationOperator(bpy.types.Operator):
    bl_idname = "export.fbx_export_single_animation"
    bl_label = "Export Single Animation"

    def execute(self, context):
        obj = bpy.context.active_object
        action = obj.animation_data.action

        strip = obj.animation_data.nla_tracks.new()
        strip.strips.new(action.name, int(action.frame_range[0]), action)

        bpy.ops.export_scene.fbx(
            filepath=get_export_file_path_with_action(),
            use_selection=True,
            bake_anim_use_nla_strips=True,
            bake_anim_use_all_actions=False
        )

        obj.animation_data.nla_tracks.remove(strip)

        return {'FINISHED'}


class FBXExportAllOperator(bpy.types.Operator):
    bl_idname = "export.fbx_export_all"
    bl_label = "Export all Animations"

    def execute(self, context):
        bpy.ops.export_scene.fbx(
            filepath=get_export_file_path(),
            use_selection=True,
            bake_anim_use_nla_strips=False,
            bake_anim_use_all_actions=True,
        )

        return {'FINISHED'}
    

def register():
    bpy.utils.register_class(FBXExporterPanel)
    bpy.utils.register_class(FBXExportSingleAnimationOperator)
    bpy.utils.register_class(FBXExportWithoutAnimationOperator)
    bpy.utils.register_class(FBXExportAllOperator)


def unregister():
    bpy.utils.unregister_class(FBXExporterPanel)
    bpy.utils.unregister_class(FBXExportSingleAnimationOperator)
    bpy.utils.unregister_class(FBXExportWithoutAnimationOperator)
    bpy.utils.unregister_class(FBXExportAllOperator)

def draw_panel(self, context):
    layout = self.layout
    layout.operator("export.fbx_export_without_animation", text="Export Without Animation")
    layout.operator("export.fbx_export_single_animation", text="Export Single Animation")
