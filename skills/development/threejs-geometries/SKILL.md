---
name: threejs-geometries
version: 1.0.0
description: "three.js geometry authoring: BufferGeometry, typed BufferAttribute and interleaved layouts, InstancedBufferGeometry, primitive Geometries (box/sphere/torus/etc.), ExtrudeGeometry and Shape/Path/Curve from Extras, WireframeGeometry, and addon geometries such as TextGeometry, DecalGeometry, RoundedBoxGeometry. Use when building custom buffer geometries, extruding shapes, or using primitive geometry constructors; for animation morph targets see threejs-animation; for merging buffers see BufferGeometryUtils addon."
author: Fullstack Skills Community
category: development
tags: [threejs-geometries]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

-----------|----------------------|
| Core | https://threejs.org/docs/BufferGeometry.html |
| Geometries | https://threejs.org/docs/BoxGeometry.html |
| Extrude | https://threejs.org/docs/ExtrudeGeometry.html |
| Shape | https://threejs.org/docs/Shape.html |

## Scope

- **In scope:** Core geometries, buffer core, curve/shape/extrusion workflows, selected addon geometries.
- **Out of scope:** Physics collision mesh baking; full CAD import pipelines.

## Common pitfalls and best practices

- Missing normals break lighting; compute or import consistently.
- Wrong winding order flips faces—check side/culling.
- Huge attribute counts need LOD or simplification (modifiers in addons—mention only if user asks).

## Documentation and version

Primitives and `BufferGeometry` live under [Geometries](https://threejs.org/docs/#Geometries) and [BufferGeometry](https://threejs.org/docs/BufferGeometry.html) in [three.js docs](https://threejs.org/docs/). Curve, `Shape`, and extrusion APIs appear under **Extras** and **Geometries**—Addons **Curves** / **Geometries** document NURBS and text meshes; link those instead of copying long signatures.

## Agent response checklist

When answering under this skill, prefer responses that:

1. Link `BufferGeometry`, a primitive, or `ExtrudeGeometry` / `Shape` as appropriate.
2. Point **instancing** usage to **threejs-objects** for `InstancedMesh` patterns.
3. Point morph targets and tracks to **threejs-animation** when deformation is time-driven.
4. Reference `BufferGeometryUtils` (Addons **Utils**) only by name + docs link when merging/splitting.
5. Emphasize `dispose()` when replacing large custom buffers.

## References

- https://threejs.org/docs/#Geometries
- https://threejs.org/docs/BufferGeometry.html
- https://threejs.org/docs/ExtrudeGeometry.html

## Keywords

**English:** buffergeometry, extrude, shape, path, curve, primitives, instancing, three.js

**中文：** 几何体、BufferGeometry、挤出、Shape、曲线、实例化、three.js
