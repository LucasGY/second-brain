---
type: entity
title: "Groq"
aliases: ["Groq LPU", "LPU"]
tags: [entity, ai_tech, semiconductor]
first_seen: 2026-05-03
last_updated: 2026-05-03
key_sources: []
---

# Definition
Groq is an AI chip company specializing in deterministic, SRAM-based LPU (Language Processing Unit) architecture. Acquired by Nvidia in 2026. Its compiler-first philosophy is fundamentally incompatible with DRAM-based systems due to the non-deterministic nature of DRAM refresh operations and memory controller optimizations.
> Groq是一家AI芯片公司，专注于基于SRAM的确定性LPU（语言处理单元）架构。2026年被Nvidia收购。其编译器优先哲学与DRAM系统根本不兼容，因为DRAM刷新操作和内存控制器优化的非确定性特性。

## 📅 Evolution Timeline
* **2026-05:** Nvidia acquisition announced. Analysis shows deterministic compiler cannot be applied to HBM-based GPU architecture. Source: [[20260503_feeds_groq-nvidia-arch-analysis|Groq-Nvidia架构分析]]
  > **2026-05：** Nvidia收购宣布。分析显示确定性编译器无法应用于基于HBM的GPU架构。来源：[[20260503_feeds_groq-nvidia-arch-analysis|Groq-Nvidia架构分析]]
* **Pre-acquisition:** Explored deterministic DRAM design but deemed engineering implementation unrealistic. Pivoted to pure SRAM architecture.
  > **收购前：** 探索确定性DRAM设计但认为工程实现不现实。转向纯SRAM架构。

## Strategic / Technical Significance
Groq's SRAM-only architecture provides predictable latency, making it ideal for low-latency decode scenarios. Within Nvidia's ecosystem, it can only function as an independent specialized product line. The VLIW (Very Long Instruction Word) architecture prioritizes compiler control over hardware scheduling.
> Groq的纯SRAM架构提供可预测延迟，使其成为低延迟decode场景的理想选择。在Nvidia生态系统内，它只能作为独立专用产品线存在。VLIW（超长指令字）架构优先编译器控制而非硬件调度。

## 📚 Source Mentions
* [[20260503_feeds_groq-nvidia-arch-analysis|Groq-Nvidia架构分析]]

## 🕸️ Relationships

### Related Entities
[[nvidia|Nvidia]], [[tsmc|TSMC]]

### Related Concepts
[[heterogeneous-inference|异构推理]], [[vliw|VLIW]], [[deterministic-compiler|确定性编译器]], [[sram|SRAM]]