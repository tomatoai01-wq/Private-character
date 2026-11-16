#!/usr/bin/env bash
# FBX → 웹용 GLB 변환 (Blender 5.1 + glTF-Transform 필요: npm i -g @gltf-transform/cli)
# 사용: bash tools/convert.sh
set -e
cd "$(dirname "$0")/.."
B="/c/Program Files/Blender Foundation/Blender 5.1/blender.exe"
SRC=iCloneExport_FBX; OUT=viewer/models; TMP=$(mktemp -d)
"$B" -b --factory-startup -P tools/fbx_to_glb.py -- "$SRC/캐릭터.fbx" "$TMP/char.glb" char
"$B" -b --factory-startup -P tools/fbx_to_glb.py -- "$SRC/애니메이션1.fbx" "$TMP/anim.glb" anim
C="--compress meshopt --texture-compress webp --join false --flatten false --instance false --palette false"
gltf-transform optimize "$TMP/char.glb" "$OUT/character_hq.glb" $C --texture-size 1024 --simplify false
gltf-transform optimize "$TMP/char.glb" "$OUT/character_lq.glb" $C --texture-size 512 --simplify true --simplify-error 0.001 --simplify-ratio 0.5
gltf-transform optimize "$TMP/anim.glb" "$OUT/animation1.glb" $C
