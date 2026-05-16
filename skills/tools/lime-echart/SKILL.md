---
name: lime-echart
version: 1.0.0
description: "Integrates Apache ECharts into UniApp and UniAppX projects for cross-platform data visualization (H5, mini-programs, native App). Supports line, bar, pie, scatter, radar, gauge, funnel, heatmap, and more chart types. Use when the user needs to create ECharts charts in UniApp/UniAppX or configure interactive data visualizations for mobile and web."
author: Fullstack Skills Community
category: tools
tags: [lime-echart]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

----|------|----------|
| Line | `examples/charts/line-chart.md` | Trends over time |
| Bar | `examples/charts/bar-chart.md` | Category comparison |
| Pie | `examples/charts/pie-chart.md` | Proportions |
| Scatter | `examples/charts/scatter-chart.md` | Correlation |
| Radar | `examples/charts/radar-chart.md` | Multi-dimension comparison |
| Gauge | `examples/charts/gauge-chart.md` | Single metric display |

### API Reference

- `api/component-api.md` - Component properties and attributes
- `api/methods-api.md` - Chart manipulation methods
- `api/events-api.md` - Event handling (click, hover, zoom)
- `api/options-api.md` - Full ECharts options reference

## Best Practices

1. **Dispose on unmount** - Call `chart.dispose()` in `onUnload` to prevent memory leaks
2. **Lazy load charts** - Initialize charts only when they scroll into view
3. **Test cross-platform** - Verify on H5, WeChat mini-program, and native App
4. **Optimize data volume** - Downsample large datasets before rendering on mobile
5. **Use CSS sizing** - Set chart container dimensions via CSS, not inline styles

## Resources

- **Official Plugin**: https://ext.dcloud.net.cn/plugin?id=4899
- **ECharts Docs**: https://echarts.apache.org/

## Keywords

lime-echart, echarts, uniapp, uniappx, chart, visualization, 图表, 折线图, 柱状图, 饼图, data visualization, mobile chart
