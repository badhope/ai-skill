---
name: stitch-remotion
version: 1.0.0
description: "Generate walkthrough videos from Stitch projects using Remotion. Use when the user wants a video demo, walkthrough, or presentation of Stitch-designed screens. Retrieves screenshots via Stitch MCP, builds a Remotion composition with transitions (fade, slide), zoom animations, and text overlays per screen."
author: Fullstack Skills Community
category: tools
tags: [stitch-remotion]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

----|----------|
| Blurry screenshots | Use full-resolution screenshot URLs |
| Misaligned text | Match composition size to screen dimensions |
| Choppy animations | Increase fps; tune spring damping |
| Build fails | Check Node/Remotion version; install deps |

## Keywords

**English:** Stitch, Remotion, walkthrough, video, screenshots, transitions.  
**中文关键词：** Stitch、Remotion、走查视频、转场。

## References

- [Remotion docs](https://www.remotion.dev/docs/)
- [Remotion transitions](https://www.remotion.dev/docs/transitions)
- [Remotion Skills](https://github.com/remotion-dev/remotion/tree/main/packages/skills) — animation, composition patterns, performance; install with `npx skills add remotion-dev/skills`.
- [Remotion MCP](https://www.remotion.dev/docs/ai/mcp) — programmatic render and preview.
- [Stitch MCP](https://stitch.withgoogle.com/docs/mcp/guide/)
- [Examples](examples/usage.md)
- [Screens Manifest Example](examples/screens.json)
- Full templates in [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills).
