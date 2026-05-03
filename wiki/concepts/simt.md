---
type: concept
title: "SIMT"
aliases: ["Single Instruction Multiple Thread", "单指令多线程"]
tags: [concept, architecture, gpu]
status: seed
first_seen: 2026-05-03
last_updated: 2026-05-03
---

# Core Definition
SIMT (Single Instruction Multiple Thread) is the fundamental execution model used in modern GPUs, where groups of threads (warps) execute the same instruction on different data. Hardware warp schedulers dynamically switch between warps to hide memory latency, making it incompatible with deterministic compiler approaches.
> SIMT（单指令多线程）是现代GPU使用的基本执行模型，其中线程组（warps）在不同数据上执行相同指令。硬件warp调度器动态切换warps以隐藏内存延迟，使其与确定性编译器方案不兼容。

## 🛠️ Mechanisms & Architecture

### Warp Scheduling

```
Memory stall detected → Hardware switch to ready warp → Continue execution
                                ↑
                    Warp #1 waiting on memory
                    Warp #2 ready to execute
                    Warp #3 ready to execute
```

### Key Properties

* **Thread-level parallelism:** Hardware manages thousands of concurrent threads
* **Latency hiding:** Statistical multiplexing of execution
* **Register file size:** Must be large enough to hold context for all warps
* **SIMD underlying:** Actually executes same instruction on multiple data elements

### Why SIMT Exists

**Fundamental premise:** Memory latency is unpredictable, therefore you need massive concurrent threads to statistically saturate the pipeline.
> **基本前提：** 内存延迟不可预测，因此需要大量并发线程统计饱和pipeline。

## ⚔️ Contradictions & Evolution

* **VLIW vs SIMT:** These architectures offer diametrically opposed answers to runtime non-determinism. Groq eradicates uncertainty at compile time; Nvidia masks it via warp switching. Source: [[20260503_feeds_groq-nvidia-arch-analysis|Groq-Nvidia架构分析]]
  > **VLIW vs SIMT：** 这些架构对运行时非确定性给出完全对立的答案。Groq在编译时消除不确定性；Nvidia通过warp切换掩盖它。来源：[[20260503_feeds_groq-nvidia-arch-analysis|Groq-Nvidia架构分析]]

* **AMD's TeraScale to GCN transition:** Historical case study showing VLIW → SIMT migration occurred because VLIW compiler burden became too severe for unpredictable workloads.
  > **AMD的TeraScale到GCN转变：** 历史案例研究显示VLIW→SIMT迁移发生，因为不可预测workloads使VLIW编译器负担变得太重。

## 📚 Source Mentions
* [[20260503_feeds_groq-nvidia-arch-analysis|Groq-Nvidia架构分析]]

## 🕸️ Relationships

### Related Concepts
[[vliw|VLIW]], [[heterogeneous-inference|异构推理]], [[nvidia-architecture|Nvidia架构]]

### Related Entities
[[nvidia|Nvidia]], [[amd|AMD]]