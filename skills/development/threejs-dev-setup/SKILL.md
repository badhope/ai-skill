---
name: threejs-dev-setup
version: 1.0.0
description: "Bootstrap and toolchain guidance for three.js applications using npm, Vite/Webpack/Rollup, bare ESM import maps, and TypeScript. Covers canonical import paths for three core versus three/addons/ (examples/jsm re-exports), version alignment with threejs.org docs, and fixing module not found for loaders and controls. Use when scaffolding a new 3D project, migrating bundler, or debugging resolution of addons; do not use for rendering API details (see threejs-renderers) or asset loading logic (see threejs-loaders)."
author: Fullstack Skills Community
category: development
tags: [threejs-dev-setup]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

-----------|----------------------|
| Manual (getting started) | https://threejs.org/manual/ |
| Docs index | https://threejs.org/docs/ |
| Package / install context | https://www.npmjs.com/package/three |

## Scope

- **In scope:** npm/install, bundlers, import maps, TypeScript basics for three, addon import paths, minimal verification snippet.
- **Out of scope:** WebGL theory, full render target or post stack (threejs-renderers, threejs-postprocessing), physics, deployment beyond "build runs".

## Common pitfalls and best practices

- Mixing multiple `three` copies in one page breaks singletons; dedupe with bundler aliases.
- Importing addons from deep `node_modules/.../examples/jsm` paths is fragile; prefer package exports `three/addons/...` when available.
- Always match **r152+** style color management docs when giving snippet defaults (output color space)—point to threejs-renderers/textures for details.
- SSR frameworks need dynamic import or client-only components for WebGL context.

## Documentation and version

Toolchain and import paths follow the **three** npm package version the user installs. The [Manual](https://threejs.org/manual/) and [docs](https://threejs.org/docs/) are updated with the library; addon paths (`three/addons/...`) must match the package layout for that release—when in doubt, cite the version number and the exact import line from the current docs.

## Agent response checklist

When answering under this skill, prefer responses that:

1. Name the bundler or runtime (Vite, Webpack, bare ESM, `importmap`) and the intended `three` version.
2. Link https://threejs.org/manual/ and/or https://threejs.org/docs/ for authoritative setup context.
3. Distinguish **threejs-dev-setup** (resolution) from **threejs-renderers** (runtime API) failures.
4. Never assume global script tags unless the user explicitly uses CDN/no-bundler HTML.
5. Recommend deduplicating `three` in `package.json` / lockfile when duplicate singleton issues appear.

## Keywords

**English:** three.js, vite, webpack, rollup, import map, typescript, npm, three/addons, examples jsm, module resolution, scaffold

**中文：** three.js 安装、构建、importmap、模块解析、three/addons、脚手架、Vite、Webpack
