---
type: concept
title: "HBM"
aliases: ["High Bandwidth Memory", "高带宽内存"]
tags: [concept, semiconductor, memory]
status: seed
first_seen: 2026-05-03
last_updated: 2026-05-03
---

# Core Definition
HBM (High Bandwidth Memory) is a high-performance DRAM interface using 3D stacking and silicon interposers. It provides massive bandwidth (hundreds of GB/s) but is fundamentally non-deterministic due to DRAM refresh operations and dynamic memory controller optimizations, making it incompatible with deterministic compiler approaches.
> HBM（高带宽内存）是一种使用3D堆叠和硅中介层的高性能DRAM接口。它提供巨大带宽（数百GB/s），但由于DRAM刷新操作和动态内存控制器优化，本质上是非确定性的，使其与确定性编译器方案不兼容。

## 🛠️ Mechanisms & Architecture

### Why DRAM is Non-Deterministic

**1. Refresh Operation (tREFI):**
- DRAM cells need periodic refresh to maintain data
- Refresh operation blocks bank access
- Refresh rate dynamically scales with temperature
- Cannot be predicted at compile time

**2. Memory Controller Optimizations:**
* **Batch scheduling:** Groups traffic hitting same page to minimize misses
* **Bank interleaving:** Simultaneously interleaves reads/writes across banks
* **Read/write switching:** Minimizes switching overhead
* All happen dynamically at runtime → unpredictable latency

**3. System-Level Optimizations:**
* Bank address hashing
* Complex page mapping
* Compiler cannot statically determine data locations

### Technical Specs

* **Bandwidth:** 100s of GB/s per stack
* **Stacking:** 3D stacking with TSV (Through-Silicon Via)
* **Integration:** CoWoS enables massive HBM integration (up to 64 HBM in future)

## ⚔️ Contradictions & Evolution

* **Groq's exploration of deterministic DRAM:** They filed a patent for deterministic DRAM design but deemed engineering implementation unrealistic. This is why they chose pure SRAM. Source: [[20260503_feeds_groq-nvidia-arch-analysis|Groq-Nvidia架构分析]]
  > **Groq探索确定性DRAM：** 他们申请了确定性DRAM设计专利，但认为工程实现不现实。这导致他们选择纯SRAM。来源：[[20260503_feeds_groq-nvidia-arch-analysis|Groq-Nvidia架构分析]]

* **Applying deterministic compiler to DRAM:** Would require abandoning most optimization strategies, causing severe degradation of DRAM efficiency and bandwidth.
  > **将确定性编译器应用于DRAM：** 需要放弃大多数优化策略，导致DRAM效率和带宽严重下降。

## 📚 Source Mentions
* [[20260503_feeds_groq-nvidia-arch-analysis|Groq-Nvidia架构分析]]
* [[20260503_feeds_tsmc-2026-tech-seminar|台积电技术研讨会2026]]

## 🕸️ Relationships

### Related Concepts
[[simt|SIMT]], [[heterogeneous-inference|异构推理]], [[sram|SRAM]], [[coWoS]]

### Related Entities
[[nvidia|Nvidia]], [[hynix|SK Hynix]], [[samsung|Samsung]], [[tsmc|TSMC]]