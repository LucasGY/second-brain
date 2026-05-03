---
type: concept
title: "VLIW"
aliases: ["Very Long Instruction Word", "超长指令字"]
tags: [concept, architecture]
status: seed
first_seen: 2026-05-03
last_updated: 2026-05-03
---

# Core Definition
VLIW (Very Long Instruction Word) is an architecture where the compiler makes all scheduling decisions at compile time, packaging multiple operations into single long instructions. Groq uses VLIW to achieve deterministic latency, but this requires predictable memory access patterns that DRAM cannot provide.
> VLIW（超长指令字）是一种架构，其中编译器在编译时做出所有调度决策，将多个操作打包成单个长指令。Groq使用VLIW实现确定性延迟，但这需要可预测的内存访问模式，而DRAM无法提供。

## 🛠️ Mechanisms & Architecture

### Compiler-First Philosophy

```
Compiler → Static allocation → All resources determined at compile time
                ↓
        Predictable execution
                ↓
       Deterministic latency
```

### VLIW Characteristics

* **All scheduling at compile time:** No runtime hardware scheduling
* **Multiple execution units:** Parallel operations in single instruction
* **Register pressure:** Compiler must manage register allocation
* **Compiler complexity:** Must understand data dependencies, resource constraints

### Why VLIW Works with SRAM

* SRAM refresh is deterministic (no refresh blocking)
* No dynamic memory controller optimizations
* Compiler can predict exact memory access timing
* Cycle-level determinism achievable

## ⚔️ Contradictions & Evolution

* **VLIW was tried and abandoned:** AMD transitioned from TeraScale (VLIW) to GCN (SIMT) because compiler burden became unsustainable for unpredictable workloads. Source: [[20260503_feeds_groq-nvidia-arch-analysis|Groq-Nvidia架构分析]]
  > **VLIW曾被尝试并放弃：** AMD从TeraScale(VLIW)转向GCN(SIMT)，因为不可预测workloads使编译器负担变得无法承受。来源：[[20260503_feeds_groq-nvidia-arch-analysis|Groq-Nvidia架构分析]]

* **Groq's patent exploration:** Groq once filed a patent for deterministic DRAM design but deemed engineering implementation unrealistic. This is why they pivoted to pure SRAM.
  > **Groq的专利探索：** Groq曾申请确定性DRAM设计专利，但认为工程实现不现实。这导致他们转向纯SRAM。

## 📚 Source Mentions
* [[20260503_feeds_groq-nvidia-arch-analysis|Groq-Nvidia架构分析]]

## 🕸️ Relationships

### Related Concepts
[[simt|SIMT]], [[heterogeneous-inference|异构推理]], [[deterministic-compiler|确定性编译器]], [[sram|SRAM]]

### Related Entities
[[groq|Groq]], [[amd|AMD]]