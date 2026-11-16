# 캐릭터 뷰어

iClone/Character Creator에서 내보낸 FBX 캐릭터를 웹 브라우저(PC·모바일)에서 보는 가벼운 뷰어입니다.

- **기본 포즈**: 캐릭터의 기본 자세(A포즈)
- **애니메이션**: 재생/일시정지, 원하는 위치로 이동, 속도 조절(1x · 0.5x · 0.25x · 2x)
- 드래그로 회전, 두 손가락(휠)으로 확대, 오른쪽 드래그로 이동
- 모바일/저사양 기기는 자동으로 **가벼운 모델**(2.1MB)을 사용, PC는 **고화질**(4.2MB). `?q=hq` / `?q=lq` 로 강제 지정 가능

## 구성
| 경로 | 내용 |
|---|---|
| `viewer/index.html` | 뷰어 (three.js, CDN 사용 / 빌드 불필요) |
| `viewer/models/character_hq.glb` | 캐릭터 고화질 (텍스처 1024px) |
| `viewer/models/character_lq.glb` | 캐릭터 가벼운 버전 (텍스처 512px, 폴리곤 감소) |
| `viewer/models/animation1.glb` | 애니메이션 (뼈대 움직임만) |
| `tools/` | FBX → GLB 변환 스크립트 (Blender + glTF-Transform) |

## 로컬에서 보기
```bash
python -m http.server 8000
```
브라우저에서 http://localhost:8000 접속.

## 모델 다시 변환하기
원본 FBX를 `iCloneExport_FBX/` 에 두고 `bash tools/convert.sh` 실행 (Blender 5.1, `npm i -g @gltf-transform/cli` 필요).
