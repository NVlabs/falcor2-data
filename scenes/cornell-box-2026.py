# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import math

import falcor2 as f2
import slangpy as spy
from falcor2 import pyscene


def orient_environment(scene: f2.Scene) -> None:
    env_map = scene.components.find(type=f2.EnvMapLight)
    assert env_map is not None
    # Match the environment orientation in the source scene's reference renders.
    transform = f2.Transform()
    transform.scale = spy.float3(1, 1, -1)
    transform.rotation_xyz = spy.float3(0, math.radians(90), 0)
    env_map.entity.transform = transform


pyscene.load_asset("../assets/cornell-box-2026/Cornell_Box_2026_Slatted_Pendant.gltf")
pyscene.env.set("../assets/cornell-box-2026/Cornell_Striped_Studio_4K.exr")
pyscene.on_scene_loaded(orient_environment)


if __name__ == "__main__":
    pyscene.preview()
