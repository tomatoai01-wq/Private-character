import bpy, sys
argv = sys.argv[sys.argv.index("--")+1:]
src, dst, mode = argv
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.fbx(filepath=src)
arm=[o for o in bpy.data.objects if o.type=="ARMATURE"][0]
meshes=[o for o in bpy.data.objects if o.type=="MESH"]
if mode=="char":
    for o in meshes:
        if o.data.shape_keys:
            o.shape_key_clear()
        o.animation_data_clear()
    arm.animation_data_clear()
    for a in list(bpy.data.actions): bpy.data.actions.remove(a)
    # material report
    for m in bpy.data.materials:
        if not m.use_nodes: continue
        b=next((n for n in m.node_tree.nodes if n.type=="BSDF_PRINCIPLED"),None)
        if b:
            al=b.inputs["Alpha"]
            print("MAT",m.name,"alpha_linked",al.is_linked,"alpha",al.default_value)
    bpy.ops.export_scene.gltf(filepath=dst, export_format='GLB', export_animations=False,
        export_morph=False, export_skins=True, export_image_format='AUTO', export_yup=True)
else:
    for o in meshes: bpy.data.objects.remove(o, do_unlink=True)
    for a in list(bpy.data.actions):
        if not a.name.startswith("Armature"): bpy.data.actions.remove(a)
    act=arm.animation_data.action
    act.name="Animation1"
    sc=bpy.context.scene
    sc.frame_start=int(act.frame_range[0]); sc.frame_end=int(act.frame_range[1])
    bpy.ops.export_scene.gltf(filepath=dst, export_format='GLB', export_animations=True,
        export_animation_mode='ACTIONS', export_frame_step=2, export_force_sampling=True,
        export_morph=False, export_skins=True, export_yup=True, export_def_bones=False)
