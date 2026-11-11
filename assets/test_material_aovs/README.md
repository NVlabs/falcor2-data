# Paired marble material AOV assets

`marble_blue_veins.mtlx` and `marble_blue_veins.mdl` are paired rendering fixtures used by Falcor2's material AOV
image tests on the ASWF shader ball. Both expose the same blue-vein mask. Keep them together when changing the
comparison; small code-generation regression graphs remain beside their tests in the Falcor2 source repository.

The MDL file was generated using MaterialX GenMDL from the upstream
`resources/Materials/Examples/StandardSurface/standard_surface_marble_solid.mtlx`, with Falcor amendments described
in its header. It requires the MaterialX MDL library supplied by Falcor2's `external/MaterialX` dependency.

These files were relocated from Falcor2 commit `82b7ae929` without changing their contents.

The paired fixtures are distributed under Apache-2.0. See `LICENSE` for the
license text; MaterialX's upstream license is also retained in Falcor2's
`external/MaterialX/LICENSE`.
