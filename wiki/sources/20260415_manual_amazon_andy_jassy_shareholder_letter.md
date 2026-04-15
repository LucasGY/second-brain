---
type: source
date_ingested: 2026-04-15
authors: ["Andy Jassy"]
source_url: "https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-2025-letter-to-shareholders"
source_path: "raw/manual/web/amazon-ceo-andy-jassy-2025-letter-to-shareholders.md"
tags: [source, manual, ai_tech]
summary_en: Andy Jassy's 2025 shareholder letter frames [[amazon|Amazon]] as a company that wins by inventing into major inflections, running parallel bets, and rebuilding products such as [[amazon-bedrock|Amazon Bedrock]] and Alexa around AI even at the cost of short-term cash flow pressure.
summary_zh: Andy Jassy 的 2025 年股东信把 [[amazon|Amazon]] 描述为一家通过押注重大拐点、并行推进多条路径，并围绕 AI 重建 [[amazon-bedrock|Amazon Bedrock]] 与 Alexa 等产品来取胜的公司，即使这会带来短期现金流压力。
---
# Amazon CEO Andy Jassy's 2025 Letter to Shareholders

## 📌 TL;DR
This shareholder letter argues that [[amazon|Amazon]] should invest aggressively into disproportionate inflections such as AI, robotics, and broadband, pursue multiple parallel paths when the right answer is unclear, and be willing to rebuild working systems from first principles to capture long-term upside.
这封股东信认为，[[amazon|Amazon]] 应当积极押注 AI、机器人和宽带连接等非对称拐点；在最优解尚不明确时并行推进多条路径；并愿意从第一性原理重建已经有效运行的系统，以换取长期上行空间。

## 🎯 Core Technical Problem
The core problem is how a scaled technology company preserves speed, invention quality, and long-term capital discipline while operating across several simultaneous platform shifts, especially AI infrastructure, logistics automation, and customer-interface reinvention.
核心问题是：一家已经具备巨大规模的科技公司，如何在同时跨越多个平台级变革时，仍然保持速度、发明质量与长期资本纪律，尤其是在 AI 基础设施、物流自动化和客户交互重构这些领域。

The letter is not a pure financial recap; it is an operating blueprint for how [[amazon|Amazon]] intends to manage inflection points without becoming trapped by legacy architectures, local optimization, or short-term free-cash-flow optics.
这封信并不只是财务回顾；它更像是一份运营蓝图，说明 [[amazon|Amazon]] 打算如何管理拐点，避免被旧架构、局部最优或短期自由现金流表象所束缚。

## 💡 Key Takeaways & Innovations
- **Parallel-path execution:** Jassy argues that when the winning mechanism is uncertain, the right comparison is often multiple serious bets versus doing nothing while debating. Same-day fulfillment centers, Prime Air, and Amazon Now are presented as complementary rather than mutually exclusive delivery paths.
  **并行路径执行：** Jassy 认为，当制胜机制尚不明确时，正确的比较对象往往是“同时推进多项严肃尝试”与“在争论中什么都不做”之间的差别。信中把 Same-Day Fulfillment Centers、Prime Air 和 Amazon Now 描述为彼此互补、而非互斥的配送路径。
- **AI as a company-wide multiplier:** AI is framed as a general-purpose force that will reshape every customer experience, accelerate AWS growth, and justify unusually large infrastructure and silicon investment.
  **AI 作为公司级乘数：** 文中把 AI 定位为一种通用型力量，它将重塑每一项客户体验、加速 AWS 增长，并为异常激进的基础设施与芯片投入提供合理性。
- **Rebuild-from-scratch willingness:** The [[amazon-bedrock|Amazon Bedrock]] “Mantle” example shows Amazon treating architectural restart as a strategic capability, not just a rescue tactic, and using its own coding agent tooling to compress redesign time.
  **从零重建的意愿：** [[amazon-bedrock|Amazon Bedrock]] 的 “Mantle” 案例显示，Amazon 把架构级重启视为一种战略能力，而不只是补救手段，并借助自有编码 agent 工具压缩重构周期。
- **Custom silicon as systems leverage:** The letter frames [[aws|AWS]] chips such as Trainium and Graviton not merely as component cost savings but as margin, capacity, and product-control levers across the AI stack.
  **自研芯片作为系统级杠杆：** 文中把 [[aws|AWS]] 的 Trainium 与 Graviton 等芯片，不仅视为器件成本节约，更视为贯穿 AI 栈的利润率、产能与产品控制权杠杆。

## 🛠️ Mechanisms & Architecture
Amazon's operating logic in this letter has a repeatable architecture.
这封信中呈现的 Amazon 运营逻辑具有一种可复用的架构。

- **Detect the inflection:** Leadership identifies a shift that is large enough to reorganize customer behavior or industry economics, such as AI adoption, fulfillment speed, or rural connectivity.
  **识别拐点：** 管理层先识别那些足以重组客户行为或行业经济结构的变化，例如 AI 普及、配送速度跃迁或农村连接性改善。
- **Build several paths in parallel:** Rather than waiting for certainty, Amazon launches multiple implementations that address the same customer outcome from different constraints and time horizons.
  **并行构建多条路径：** Amazon 不会等到确定性出现后再行动，而是针对同一客户结果，同时启动多种实现路径，以覆盖不同约束条件与时间尺度。
- **Exploit shared infrastructure:** These paths are designed to reinforce each other, such as drones using same-day nodes as launch substrates or AI services leveraging adjacent AWS data and security primitives.
  **利用共享基础设施：** 这些路径被设计为彼此增强，例如无人机以 same-day 节点作为起飞基座，或 AI 服务复用 AWS 周边的数据与安全能力。
- **Invest ahead of visible monetization:** The company accepts capex and short-term FCF pressure when demand signals and customer commitments indicate that installed capacity will be absorbed later.
  **在收入可见之前先投资：** 当需求信号与客户承诺足以表明新增能力将被吸收时，公司愿意承受资本开支与短期自由现金流压力。
- **Restart architecture when scale changes the problem:** If a fast-growing service outgrows its original design, Amazon may split out a small, highly capable team to rebuild a new core while the legacy service stays live.
  **当规模改变问题本质时重启架构：** 如果一项快速增长的服务超出了原始设计边界，Amazon 会拆出一支小而强的团队，在老系统继续运行的同时重建新的核心。

The Bedrock-to-Mantle example is the clearest technical mechanism in the letter: a separable team of six engineers rebuilt the inference engine in 76 days, turning architectural reset into a speed advantage rather than a drag on the live service.
Bedrock 到 Mantle 的案例，是这封信里最清晰的技术机制：一支可分离的六人团队在 76 天内重建了推理引擎，把架构重置从线上服务的负担，转化为速度优势。

## 👻 Implicit Assumptions & Limitations
The letter assumes [[amazon|Amazon]] can continue to finance unusually large AI capex without losing strategic flexibility elsewhere in the business.
这封信隐含地假设：[[amazon|Amazon]] 能够持续为异常高额的 AI 资本开支提供资金，同时不损失公司在其他业务上的战略灵活性。

It also assumes that scale advantages in security, infrastructure adjacency, and custom silicon will remain durable enough for [[aws|AWS]] to capture a disproportionate share of enterprise AI workloads.
它还假设：在安全性、基础设施邻接性与自研芯片方面形成的规模优势，足以保持长期耐久性，让 [[aws|AWS]] 拿下不成比例的企业级 AI 工作负载份额。

A major limitation is that most evidence is management-asserted rather than independently audited inside the note itself, so the document is strongest as a statement of Amazon's operating doctrine, not as a neutral proof of each quantitative claim.
一个主要局限在于：文中的大多数证据都来自管理层自述，而不是在信件内部完成独立审计，因此这份文档更适合作为 Amazon 运营理念的陈述，而不是对每项量化断言的中立证明。

## 🔗 Actionability / Integration
This source is highly reusable as a strategic reference for [[inflection-management|Inflection Management]], especially around parallel bets, willingness to restart architectures, and the coupling between infrastructure control and product speed.
这个来源非常适合作为 [[inflection-management|Inflection Management]] 的战略参考，尤其适用于理解并行押注、重启架构的意愿，以及基础设施控制权与产品速度之间的耦合关系。

It also materially updates the wiki's understanding of [[amazon|Amazon]], [[andy-jassy|Andy Jassy]], [[aws|AWS]], and [[amazon-bedrock|Amazon Bedrock]] by giving a first-party description of how these entities fit together inside Amazon's current AI-led operating model.
它也实质性更新了 wiki 对 [[amazon|Amazon]]、[[andy-jassy|Andy Jassy]]、[[aws|AWS]] 与 [[amazon-bedrock|Amazon Bedrock]] 的理解，因为它提供了一手视角，说明这些实体在 Amazon 当前由 AI 驱动的运营模型中如何彼此配合。

## 🕸️ Knowledge Graph
**Extracted Entities:** [[amazon|Amazon]], [[andy-jassy|Andy Jassy]], [[aws|AWS]], [[amazon-bedrock|Amazon Bedrock]]
**提取出的实体：** [[amazon|Amazon]], [[andy-jassy|Andy Jassy]], [[aws|AWS]], [[amazon-bedrock|Amazon Bedrock]]

**Related Concepts:** [[inflection-management|Inflection Management]]
**相关概念：** [[inflection-management|Inflection Management]]
