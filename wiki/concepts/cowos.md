---
type: concept
title: "CoWoS"
aliases: ["Chip on Wafer on Substrate", "基板上晶圆上芯片"]
tags: [concept, semiconductor, packaging]
status: seed
first_seen: 2026-05-03
last_updated: 2026-05-03
---

# Core Definition
CoWoS (Chip on Wafer on Substrate) is TSMC's advanced packaging technology that integrates multiple chips and High Bandwidth Memory (HBM) on a silicon interposer. It enables massive die-to-die bandwidth and is critical for AI accelerator scaling beyond reticle limits.
> CoWoS（基板上晶圆上芯片）是台积电的先进封装技术，在硅中介层上集成多个芯片和高带宽内存（HBM）。它实现大规模芯片间带宽，对AI加速器超越光罩限制的扩展至关重要。

## 🛠️ Mechanisms & Architecture

### CoWoS Scaling Roadmap

| Year | Reticle Size | HBM Count | Yield/Status |
|------|--------------|-----------|--------------|
| 2026 | 5.5-reticle | - | >98% yield |
| 2028 | 14-reticle | 20 HBM | Target |
| 2029+ | >14-reticle | 24 HBM | Planned |

### Technical Advantages

* **Interposer-based integration:** Silicon interposer provides ultra-high-density wiring
* **HBM integration:** Multiple HBM stacks co-located with compute dies
* **Beyond reticle limits:** Enables system-level integration larger than single die

### System-Level Metrics (2024-2029)

* **Compute transistor increase:** 48x within single CoWoS
* **HBM bandwidth increase:** 34x
* **Key insight:** Moore's Law doesn't disappear, it becomes system engineering

## 🚀 Implementations & Best Practices

* **Critical for:** AI accelerators (Nvidia, AMD), HPC, large language model training
  > **关键应用：** AI加速器（Nvidia、AMD）、HPC、大语言模型训练

* **Engineering Considerations:**
  - Thermal management at multi-reticle scale
  - Power delivery through interposer
  - Yield challenges at larger formats

## 📚 Source Mentions
* [[20260503_feeds_tsmc-2026-tech-seminar|台积电技术研讨会2026]]

## 🕸️ Relationships

### Related Concepts
[[soic|SoIC]], [[hbm|HBM]], [[sow|System-on-Wafer]], [[silicon-photonics|硅光子]], [[heterogeneous-inference|异构推理]]

### Related Entities
[[tsmc|TSMC]], [[nvidia|Nvidia]], [[hynix|SK Hynix]]