# OpenUSD curve example

Source: https://github.com/PixarAnimationStudios/OpenUSD/blob/v25.02/extras/usd/examples/usdGeomExamples/basisCurves.usda

Tag: v25.02. Downloaded 2026-10-19. License: accompanying upstream LICENSE.txt (Apache-2.0 with modification).

Original SHA256: d0b0b0d8afe70fcb7304b8715cf707c41588a20bc719e6a387978186ed4e9155.

The example has five oriented ribbon prims and five unoriented round prims. It covers linear and cubic Bezier centerlines, constant/varying/vertex widths, varying non-unit normals, and zero-width tips. Whitespace may be normalized by repository hooks; geometry is unchanged. It has display colors but no bound surface materials; separate generated fixtures test material binding.

Repository hooks removed trailing whitespace from the asset and license. Checked-in asset SHA256: e605bbdff0e856eca7fd4133979268abd7118236cdc088dd920efcc54f460a67.

## Deliberate twist diagnostic

`twist.usda` is an original Falcor2 fixture (Apache-2.0), with four straight, constant-width controls: a flat ribbon, linear and cubic Bezier ribbons whose authored varying normals turn 360 degrees, and a round curve without normals. The twist uses five normal samples at quarter turns. `tools/usd_ribbons/render_twist.py` renders directional shading and world-space shading normal colors through actual GPU scene traversal. It saves raw linear arrays and a recipe JSON beside the labeled PNG. The GPU regression tests isolate each twisted prim and verify hits, misses, UVs and normal direction throughout the turn.

`joints.usda` is an original Falcor2 fixture (Apache-2.0) for ribbon joint and normal-repair comparisons.

## Textured ribbon comparison

`textured.usda` and `uv_grid.png` are original Falcor2 fixtures (Apache-2.0). The five rows, top to bottom, are:

1. Ribbon with an unconnected UsdUVTexture.st.
2. Ribbon with a reader requesting missing st.
3. Ribbon with the same reader and an explicit (0.25, 0.75) fallback.
4. Ribbon with authored vertex st, interpolated along its centerline.
5. Mesh with full authored UVs, checking texture orientation and color decoding.

The texture is sRGB, repeated, and connected to UsdPreviewSurface emission. With Storm 25.08, the first three rows sample constant (0,0); internal ribbon parameters are not implicit texture coordinates. The explicit reader fallback is ignored for this texture connection in that renderer version. Falcor instead uses the approved RenderMan/Karma convention for missing st: U across width, increasing toward cross(normal,tangent), and V along the spine with equal parameter range per span. Level zero retains control-polygon sampling and advances V equally per polygon edge. Generated coordinates supply ordinary mesh UV tangents. Authored curve st remains constant across each cross-section.

Run Storm using its standalone usdrecord with `--renderer Storm --complexity high --camera /Camera --imageWidth 512 --colorCorrectionMode disabled --disableCameraLight`. Low complexity draws curves as lines. Run `tools/usd_ribbons/render_textured.py` with Falcor's development environment for the matching emission-only orthographic view. Both PNGs contain linear RGB. The comparison is scoped to these Preview Surface networks; it does not establish a general USD requirement or arbitrary primvar-reader fallback support.

Karma 22.0.368 reference scenes are generated with tools/usd_ribbons/generate_uv_references.py. The direct MaterialX texcoord fixture includes unequal-length spans, a full twist, authored st, and a mesh control. tools/usd_ribbons/render_textured.py --show-uv renders the corresponding Falcor UVs directly. The comparison report in .plans/usd-ribbons/references records measured behavior and separates it from shader-reader fallback semantics.
