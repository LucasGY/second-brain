---
type: concept
title: "Physical AI"
aliases: ["物理AI", "Embodied AI"]
tags: [concept, ai_tech, robotics]
status: seed
first_seen: 2026-05-03
last_updated: 2026-05-03
---

# Core Definition
Physical AI refers to AI systems that interact with the physical world—autonomous vehicles, robots, and manufacturing systems. These applications require real-time processing, deterministic latency, and extreme reliability, creating fundamentally different requirements than cloud-based AI.
> 物理AI指与物理世界交互的AI系统——自动驾驶汽车、机器人和制造系统。这些应用需要实时处理、确定性延迟和极高可靠性，产生与云端AI根本不同的需求。

## 🛠️ Mechanisms & Architecture

### Humanoid Robot Definition

```
Humanoid Robot = Agentic AI + Physical AI

Components:
├── Brain (决策) → AP (Application Processor)
├── Sensing (感知) → 传感器
├── Movement (运动) → 控制
└── Power (供能) → PMIC
```

### Key Requirements vs Cloud AI

| Requirement | Cloud AI | Physical AI |
|-------------|----------|-------------|
| Latency | Can be slow | Must be real-time |
| Reliability | Model can fail | Cannot fail |
| Compute location | Centralized | Edge/distributed |
| Power | Not critical | Critical constraint |

### Automotive Integration

* **Silicon content increase:** ~2x in automotive
* **From single MCU to full stack:** AP + RF + SerDes + CIS + Radar + MCU
* **Car as mobile computing system:** Complete sensor-compute-actuator loop

## 🚀 Implementations & Best Practices

* **Critical constraints:**
  - Real-time latency (<10ms typically)
  - Fault tolerance and safety
  - Power efficiency at edge
  - Deterministic behavior

* ** TSMC's focus:** Physical AI is driving semiconductor demand expansion beyond data centers. Source: [[20260503_feeds_tsmc-2026-tech-seminar|台积电技术研讨会2026]]
  > **关键约束：** 实时延迟（通常<10ms）、容错和安全、边缘功率效率、确定性行为。

## 📚 Source Mentions
* [[20260503_feeds_tsmc-2026-tech-seminar|台积电技术研讨会2026]]

## 🕸️ Relationships

### Related Concepts
[[heterogeneous-inference|异构推理]], [[agentic-workflow|Agentic Workflow]], [[edge-computing|边缘计算]]

### Related Entities
[[tsmc|TSMC]]