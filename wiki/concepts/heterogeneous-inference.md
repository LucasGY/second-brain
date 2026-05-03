---
type: concept
title: "Heterogeneous Inference"
aliases: ["异构推理", "Heterogeneous Compute"]
tags: [concept, ai_tech, architecture]
status: seed
first_seen: 2026-05-03
last_updated: 2026-05-03
---

# Core Definition
Heterogeneous inference refers to the architectural approach of using different processing units for different inference tasks based on their specific requirements. Different hardware architectures excel at different operations: SRAM-based designs (like Groq's LPU) for low-latency decode, HBM-based GPUs for high-throughput batch processing.
> 异构推理指根据不同推理任务的具体需求使用不同处理单元的架构方法。不同硬件架构擅长不同操作：基于SRAM的设计（如Groq的LPU）适合低延迟decode，基于HBM的GPU适合高吞吐量批处理。

## 🛠️ Mechanisms & Architecture

### Memory-Bound vs Compute-Bound Workloads

**Memory-Bound (e.g., Token Generation/Decode):**
- Access patterns are predictable
- Low arithmetic intensity
- SRAM provides deterministic latency
- Compiler can optimize statically

**Compute-Bound (e.g., Training/Large Batch Inference):**
- High arithmetic intensity
- Require massive parallelism
- HBM provides high bandwidth
- Hardware scheduling masks latency

### Key Architectural Trade-offs

| Architecture | Latency | Throughput | Determinism | Best For |
|--------------|---------|------------|-------------|----------|
| Groq LPU (SRAM) | Ultra-low | Medium | 100% deterministic | Token decode |
| Nvidia GPU (HBM) | Variable | Very high | Hardware-masked | Batch processing |

### Compiler Approaches

**Compiler-First (Groq):**
- All scheduling decisions at compile time
- Zero runtime overhead
- Requires predictable memory access
- VLIW (Very Long Instruction Word) architecture

**Hardware-First (Nvidia):**
- Runtime warp scheduling
- Hardware manages latency masking
- SIMT (Single Instruction Multiple Thread)
- Works with unpredictable memory

## ⚔️ Contradictions & Evolution

* **Groq vs Nvidia Philosophy:** Groq's deterministic compiler approach is fundamentally incompatible with DRAM-based systems due to refresh operations and dynamic memory controller optimizations. Source: [[20260503_feeds_groq-nvidia-arch-analysis|Groq-Nvidia架构分析]]
  > **Groq vs Nvidia哲学：** Groq的确定性编译器方案与DRAM系统根本不兼容，因为刷新操作和动态内存控制器优化。来源：[[20260503_feeds_groq-nvidia-arch-analysis|Groq-Nvidia架构分析]]

* **Historical Lesson (AMD):** AMD's transition from TeraScale (VLIW) to GCN (SIMT) demonstrated that when workloads become less predictable, VLIW compiler burden becomes too severe; scheduling authority must return to hardware.
  > **历史教训（AMD）：** AMD从TeraScale(VLIW)到GCN(SIMT)的转变表明，当workloads变得不可预测时，VLIW编译器负担变得太重；调度权限必须交回硬件。

## 🚀 Implementations & Best Practices

* **Leading Implementations:** [[groq|Groq LPU]] for low-latency decode, [[nvidia|Nvidia GPU]] for high-throughput batch
  > **主要实现：** [[groq|Groq LPU]]用于低延迟decode，[[nvidia|Nvidia GPU]]用于高吞吐量批处理

* **Engineering Considerations:**
  - Match architecture to workload characteristics
  - Consider heterogeneous setup for optimal cost/performance
  - Monitor memory vs compute bottlenecks

## 📚 Source Mentions
* [[20260503_feeds_groq-nvidia-arch-analysis|Groq-Nvidia架构分析]]
* [[20260503_feeds_tsmc-2026-tech-seminar|台积电技术研讨会2026]]

## 🕸️ Relationships

### Related Concepts
[[simt|SIMT]], [[vliw|VLIW]], [[deterministic-compiler|确定性编译器]], [[hbm|HBM]], [[sram|SRAM]]

### Related Entities
[[nvidia|Nvidia]], [[groq|Groq]], [[tsmc|TSMC]]