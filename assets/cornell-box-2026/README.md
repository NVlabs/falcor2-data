# Cornell Box 2026

Creator: Jakub Boksansky. Original Cornell Box credits: Cornell University.

Source: https://boksajak.github.io/blog/CornellBox2026

Downloaded on 2026-11-05. The scene, included textures, and environment map
are released under CC0 1.0 Universal; see [LICENSE](LICENSE).

Upstream downloads, preserved without modification:

- [Cornell_Box_2026_Slatted_Pendant.gltf](https://boksajak.github.io/files/cornell_box_2026/Cornell_Box_2026_Slatted_Pendant.gltf)
- [Cornell_Striped_Studio_4K.exr](https://boksajak.github.io/files/cornell_box_2026/Cornell_Striped_Studio_4K.exr)

The scene includes a slatted pendant light, glazed ceramic block, anisotropic
iridescent metal sheet, solid glass block, and normal-mapped walls.

Open `data/scenes/cornell-box-2026.py` in Falcor2 to load the scene with its
environment map, or load the glTF directly to use only its authored lighting.
The glTF and EXR are tracked with Git LFS.

Import notes:

- The scene entry point flips the environment's Z axis and rotates it +90 degrees
  around Y to match the source renders. The EXR itself is unchanged.
- The upstream glTF declares `asset.version` as `6.4`. This is preserved as
  downloaded; Falcor2's glTF importer accepts it.
- Falcor2 repairs 2,527 invalid vertex normals in `Ceramic_Block_Recess` at
  import time. The downloaded geometry is unchanged.

SHA-256 checksums:

```text
4d0a0df4b5eb2ded72187094167c5b505e23e16a7d04bf03dc9bc0dc7f81d13b  Cornell_Box_2026_Slatted_Pendant.gltf
e73fce9dd5ac7039e97d78671b8cee8dbfce4fcd76e168bfc8a2dc20a0e356b2  Cornell_Striped_Studio_4K.exr
```
