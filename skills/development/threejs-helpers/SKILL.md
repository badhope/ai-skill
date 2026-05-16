---
name: threejs-helpers
version: 1.0.0
description: "Debug and visualization helpers in three.js Core Helpers (AxesHelper, GridHelper, CameraHelper, light helpers, SkeletonHelper, bounding box helpers, PlaneHelper, PolarGridHelper, ArrowHelper) and Addons Helpers (VertexNormalsHelper, VertexTangentsHelper, RectAreaLightHelper, LightProbeHelper, ViewHelper, OctreeHelper, TextureHelper, PositionalAudioHelper, AnimationPathHelper, RapierHelper). Use only for development and editor overlays—not for shipping art; for gizmo-style manipulation use threejs-controls."
author: Fullstack Skills Community
category: development
tags: [threejs-helpers]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

-----------|----------------------|
| Helpers | https://threejs.org/docs/AxesHelper.html |
| Helpers | https://threejs.org/docs/GridHelper.html |
| Helpers | https://threejs.org/docs/CameraHelper.html |
| Helpers | https://threejs.org/docs/SkeletonHelper.html |

## Scope

- **In scope:** Core + Addons helpers for visualization.
- **Out of scope:** Production meshes or shipping art (**threejs-geometries**, **threejs-lights**); orbit/transform gizmo behavior (**threejs-controls**); editor UX parity with DCC tools; physics debug beyond helper stubs.

## Common pitfalls and best practices

- Too many helpers obscures view—toggle per subsystem.
- Wrong attachment parent misaligns helper transforms.
- Helpers inherit scene graph transforms—parent under a debug group to batch hide/show.
- Some helpers duplicate geometry cost; strip in production or use `#ifdef DEBUG` style flags.
- `CameraHelper` for shadow cameras must reference `light.shadow.camera`, not the main view camera.

## Documentation and version

Helpers are listed under [Helpers](https://threejs.org/docs/#Helpers) (core) and **Addons → Helpers** in [three.js docs](https://threejs.org/docs/). They are for **debug** only; production meshes and lighting should use real geometry/lights (**threejs-geometries**, **threejs-lights**).

## Agent response checklist

When answering under this skill, prefer responses that:

1. Link the helper class (`AxesHelper`, `CameraHelper`, …) being used.
2. State that helpers are not shipping art—strip or gate behind debug flags.
3. Pair shadow/light helpers with **threejs-lights** tuning workflows.
4. Mention performance cost when many helpers are enabled.
5. Import paths follow **threejs-dev-setup** addon conventions.

## References

- Manual (debug workflow context): https://threejs.org/manual/
- Docs index (Helpers group): https://threejs.org/docs/#Helpers
- Examples: https://threejs.org/docs/DirectionalLightHelper.html

## Keywords

**English:** helper, debug, axes, grid, skeleton, normals, light helper, three.js

**中文：** 辅助、调试、坐标轴、网格、骨架、法线、Helper、three.js
