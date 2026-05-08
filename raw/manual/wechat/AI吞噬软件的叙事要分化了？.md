---
title: "AI吞噬软件的叙事要分化了？"
source: "https://mp.weixin.qq.com/s/oMINsySGFcDFXPngj4KmUw"
author:
  - "[[BayesCrest]]"
published:
created: 2026-05-08
description: "分化要开启了？"
tags:
  - "clippings"
---
BayesCrest *2026年5月8日 17:13*

今年一季度，伴随anthropic的模型性能提升与企业端业务的频繁更新，市场上最悲观的主流叙事是AI将吞噬一切软件，在这样的大背景下，微软股票都创下了08年金融危机以来的最大的季度跌幅，作为全球2B软件的绝对霸主，壁垒高如微软也没有逃脱掉AI吞噬叙事的困扰。

一季度软件股被杀，尤其连微软这种全球 2B 软件霸主都出现极端季度跌幅，说明市场当时交易的不是单一公司基本面，而是一个宏大 terminal-risk 叙事：AI agent 会绕过传统软件界面、压缩 seat、压缩 NRR、压缩 terminal multiple。

关于叙事对于股价的影响，我前期已经有很多文章来讨论，具体参见前期的系列文章 [AI、叙事与反身性投资](https://mp.weixin.qq.com/s?__biz=MzU4NDEwNTAyNQ==&mid=2247487107&idx=1&sn=defd36ad23952e13ba30a6aeec733636&scene=21#wechat_redirect) 等。

AI带来的同质化解读与二元倾向，市场变得越来越被叙事与注意力主导，一旦一个板块或者公司有负面叙事，一定会被放大，股价波动的幅度会大幅度偏离历史均值，一季度所有的美股软件公司基本上就处在这样的宏大恢弘的叙事中，anthropic吞噬一切几乎成为传播度最高最高的叙事标签，也基本上成为了市场的一致共识，那就是软件行业的terminal value没了，杀估值、杀逻辑、杀事实。这一点在港股也体现得很明显，被认为AI落后字节的腾讯与阿里股价今年以来就一直十分疲弱。

但是叙事与共识不一定是事情的原貌与真相，也不一定是真理。 [抱团、共识与真相](https://mp.weixin.qq.com/s?__biz=MzU4NDEwNTAyNQ==&mid=2247487299&idx=1&sn=1af1a683b3fa0a55199fc92a89b077bb&scene=21#wechat_redirect) 。

但这不是 “AI kill software” 结束，而是进入AI 分层定价阶段的分岔点。

过去一年半市场的交易逻辑是：

AI agent 出现

→ SaaS terminal value 被怀疑

→ 卖方模型还没下修，价格先杀估值

→ “软件”被一刀切降权

→ SaaS 从 compounder 变成 terminal-risk asset

最近的变化是：AI吞噬软件，将变成AI将软件分层。也就是说，市场不再简单问：软件会不会被 AI 吞噬？

而是开始问：这个软件到底是 AI agent 的替代对象，还是 AI agent 必须依赖的系统、数据、流程、权限、治理和基础设施？近期软件抛售更多是投资者情绪快速迁移，而不是所有公司基本面同时恶化。

---

## 1\. “SaaS 区别对待” 是真正的后验更新

过去市场的粗暴定价是：SaaS = seat-based software = AI 替代风险 = terminal multiple 下修。

现在开始细分为：

![Image](https://mmbiz.qpic.cn/mmbiz_png/eUejUCfotMfXYLmCp7M9icjEodMIVceVBCtdTaydibQXXUQ2N54cChJ3Tc2HibcgOMkG6hBqvZFv6AbG0WuBoQhdjzS8Zn9HVDjUzFT3ru4Vy4/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

应用层里，agent orchestration可能改变 engagement 和 value capture，尤其是依赖 seat/user license 的产品；但在 platform 和 infrastructure 层，AI agent 通常会增加对数据管理、工作负载编排、安全、恢复等能力的需求，这些能力在 UI 之下，不容易被绕过。

AI 不一定 kill software，但会 kill 掉“只靠人类点击 UI + seat 扩张 + 弱系统地位”的旧 SaaS 估值宪法。

---

## 2\. 为什么 2B 业务流 SaaS 可能被错杀？

agent 擅长的是：

- 语言生成
- 代码生成
- 信息检索
- 多步推理
- 低风险自动化

但企业 2B 业务流的核心不是“生成答案”，而是：

- 高可靠
- 低错误率
- 低合规风险
- 低权限风险
- 低运维成本
- 可审计
- 可回滚
- 可追责
- 可接入既有系统

这就是为什么 HR、ERP、ITSM、财务、合规、数据库、监控、安全、备份、数据治理、施工管理、医疗合规等流程，并不会因为一个通用 agent 出现就被轻易替代。

真正的企业任务函数是：

Task Completion

\= 正确结果

× 权限合规

× 数据一致性

× 可审计性

× 异常处理

× 成本可控

× SLA

而不是：Task Completion = agent 生成一段看似正确的文本。

这就是 SaaS 被错杀的核心区域：市场一开始把所有 SaaS 都当成“可被 agent 绕过的 UI”，但有一批 SaaS 其实是 agent 运行所需要的状态机、数据库、权限系统、流程控制层和审计层。

---

## 3\. agent 成本问题，是这轮重估最被低估的变量

agent 跑业务流面临的token 成本可能是人工一步步对话的N倍。因为企业真实 agent 成本不是：model token price

而是：

agent total cost

\= token cost

\+ tool call cost

\+ context retrieval cost

\+ retry cost

\+ verification cost

\+ permission cost

\+ integration cost

\+ monitoring cost

\+ human override cost

\+ mistake/liability cost

\+ maintenance cost

企业自研agent 的问题在于：看起来模型调用便宜，但把它变成可靠企业流程很贵。所以企业最后大概率不是每家公司从零自建 agent，而是采购：专业软件公司提供的 agentic workflow。

原因很简单：

- 专业 SaaS 公司能摊薄研发成本
- 一个 agent workflow 可以卖给几千个客户。
- 它们已经拥有数据结构和 workflow 状态
- agent 不需要重新理解企业流程。
- 它们已经接入权限、审计、合规和历史记录
- 它们可以把 agent 变成产品功能，而不是企业内部实验项目
- 它们可以用 deterministic workflow 降低 token path length，不是纯 LLM 自由漫游。

所以Agent 不会消灭所有 SaaS；agent 会消灭“没有 workflow ownership 的 SaaS”，但会强化“能够把 agent 产品化、流程化、低成本化、合规化的平台型 SaaS”。这就是为什么专业 SaaS 公司仍然可能有价值：它们可以把 agent 产品化、流程化、低成本化、合规化，而不是让企业自己用通用模型拼装一堆脆弱 workflow。

---

## 4\. “AI kill software” 的真正受害者是谁？

我会把高风险软件分成四类。

## 4.1 人力外包型软件 / 服务

这是最直接受损的区域：

- 低端代码外包
- 简单网页/应用开发服务
- 重复性 IT 服务
- 弱差异化实施服务
- 模板化内容/设计/测试服务

这里 AI coding agent 的替代逻辑最直接。

## 4.2 轻量 UI wrapper

如果一个产品只是：

前端 UI

\+ 少量 workflow

\+ 没有 system-of-record

\+ 没有强数据闭环

\+ 没有合规责任

那么 agent 很容易绕过它。

## 4.3 seat-based productivity SaaS

最危险的是：

收入 = 人数 × seat price。如果 AI 让企业少雇人、少开 seat，或者用 agent 完成多人工作，那么原来的 NRR/seat expansion 逻辑会被破坏。

## 4.4 没有 AI product conversion 的旧 SaaS

如果公司只是说 “我们也有 AI”，但没有体现为：

- 付费 attach rate
- ARPU 提升
- retention 改善
- workflow 自动化收入
- gross margin 可控

那就是叙事型 AI，不是收入型 AI。

---

## 5\. 谁可能从这轮 “SaaS 区别对待” 中受益？

第一类：多业务线 workflow platform，比如微软或者NOW等;

第二类：Datadog / observability / infrastructure control plane；

DDOG 这类公司的核心逻辑是：

AI workload 增加

→ 系统复杂度增加

→ logs / metrics / traces / security events 增加

→ observability 和 reliability 需求增加

这类不是 “AI 替代软件”，而是：AI 让软件系统更复杂，所以更需要监控、治理、安全、成本控制和故障定位。

以datadog为例，本季度几乎各个业务线都全面提速，电话会表示AI-native 客户增长显著快于整体；AI-native 中有 22 个年化消费 > $1M、5 个年化消费 > $10M 的客户；并且本季度签下两个全球最大科技公司 AI research divisions 的大单，一个是 7 位数 annualized deal，一个是 8 位数 annualized deal，用于 hyperscale AI training workloads 和 GPU Monitoring。

相当于openai跟anthropic是datadog的前两大AI客户，如果说底层软件可以轻松通过vibe coding来实现，当今执牛耳的两个AI巨头也不会把底层监控的业务交给datadog来做，所以anthropic dario天天鼓吹的AI吞噬论，当前营销叙事的成分更大，很多领域vibe coding无法很好解决。

DDOG 的核心不是前端界面，而是长期生产系统能力。

可以 vibe coding 出来的东西：log dashboard、metrics chart、trace viewer、GPU utilization panel、alert UI、简单 anomaly detector。

但 Datadog 真正的壁垒是：

- 高吞吐 telemetry ingestion
- 高基数 logs / metrics / traces 存储与查询
- 低延迟实时分析
- 跨云、容器、数据库、网络、GPU、LLM、security 的 integration graph
- APM + RUM + Logs + Security + LLM Observability 的统一上下文
- RBAC / audit /
	compliance
- incident response workflow
- on-call 体系
- SLO / alerting
- 成本控制
- 历史数据沉淀
- 全球 SaaS 可用性
- 大量生产事故 edge cases

vibe coding 可以生成 Datadog-like UI，但至少现阶段还完全生成不了 Datadog-like

operational

trust。

这就是 AI 吞噬软件的边界。

## 第三类：数据库 / 数据平台 / data infrastructure

Snowflake、Databricks 这类逻辑在于：agent 没有企业数据就无法完成任务；企业数据越复杂，越需要数据库、治理、向量检索、权限、数据质量和 lineage。

## 第四类：垂直 system-of-record

例如：

- 建筑管理
- 医疗合规
- 生命科学
- 财务审批
- 人力资本管理
- 供应链执行
- 保险理赔
- 法律合规

这些领域的问题不是 agent 能不能写文本，而是能不能在复杂规则下可靠执行。

---

## 6\. 可以开始看多部分 SaaS？

AI吞噬的风险消失了吗？我认为还远没有，不是 “AI 风险消失”，而是市场进入了三阶段后验修复。

## 第一阶段：Negative Attention Saturation

过去一年半，SaaS 的负叙事已经非常充分：

- AI kill software
- AI agent bypasses apps
- seat compression
- terminal multiple
	collapse

当一个叙事过度拥挤后，边际坏消息杀伤力下降。

## 第二阶段：Taxonomy Repair

市场开始意识到：

- 不是所有 SaaS 都是 UI wrapper；
- 不是所有 SaaS 都靠 seat；
- 不是所有 SaaS 都会被 agent 绕过；
- 有些 SaaS 是 agent 的底层运行基础。

这就是 “区别对待”。

## 第三阶段：Short Cover + Multiple Repair

如果某些软件已经跌了 50%–60%，但基本面没有同步恶化，那么只要卖方叙事从AI kills all software变成AI hurts some, helps some，就足以触发明显反弹。软件板块在 2026 年 Q1 出现了极端相对下跌，IGV 当季跌幅超过 24%，个股做空量处于 2016 年以来高位，说明此前已经存在较强 capitulation 状态。

---

## 7\. 不能把这理解为 “SaaS 全面见底”

这是最重要的风险点。

当前正确判断应该是：

- SaaS blanket short 进入危险区；
- 但 SaaS blanket long 也不成立。

现在的机会是：被 AI 一刀切错杀的 system-of-record / workflow-of-record / infra-like SaaS。而不是：所有跌深 SaaS，很多 SaaS 跌了 55%，仍然可能不便宜，因为它们可能是：

- 低价格（暴跌）
- \+ 高 consensus（买卖方预期并没有明显下修）
- \+ 负 narrative（极度负面叙事的状态）
- \+ terminal value 未出清（估值终值并未下修）
- \+ AI revenue proof 不足（AI收入正面证据不足）

---

## 我会用这个框架重新打分 SaaS：AI-Resilient SaaS Score

AI-

Resilient

SaaS Score

\= System-of-Record Ownership

× Workflow Criticality

× Data Integration Moat

×

Compliance

/ Reliability Requirement

× Agent Cost Advantage

× AI Monetization Proof

× Budget Alignment

× Pricing

Slack

\- Seat Deflation Risk

\- UI Wrapper Exposure

\- AI COGS Drag

\- Crowding Risk

关键分层

---

把当前 SaaS 状态定义为从 Negative Attention Rerating，进入 Selective Identity Repair。这不是全面反转，而是分层反转。

可以开始修复的公司类型

1\. 多产品平台

2\. system-of-record

3\. workflow-of-record

4\. 数据 / 安全 / 监控 / 恢复 / 混合云

5\. 垂直高合规业务流

6\. AI 能转化为付费 attach 的公司

仍然危险的公司类型

1\. seat-based 纯应用

2\. 弱系统地位 point solution

3\. 低端代码/服务外包

4\. 没有数据闭环的 productivity tool

5\. AI 功能只停留在 demo

6\. AI COGS 吃掉毛利但无法收费

---

过去一年半，市场交易的是AI吞噬一切软件；现在市场开始交易 “AI区别对待的软件”。软件不再按 SaaS 标签定价，而是按它在 agentic enterprise stack 里的位置定价。

真正的机会不是简单买 SaaS 反弹，而是找：

被错杀的 workflow infrastructure

\+ agent 低成本产品化能力

\+ system-of-record / system-of-action 地位

\+ 价格已经 reset

\+ 叙事开始修复

\+ AI 收入能够验证

我的贝叶斯后验更新是：

P(AI kills all SaaS) ↓↓↓

P(AI kills seat/UI/outsourcing SaaS) 仍高

P(AI strengthens system-of-record / infra SaaS) ↑↑

P(selective SaaS re-rating) ↑

P(blanket SaaS bottom) 仍不高

所以当前最佳表达不是：long SaaS，而是：long AI-

resilient

workflow / infra software，short or avoid AI-fragile seat/UI SaaS，这才是这轮软件分裂之后真正有 alpha 的地方。

全文完。

AI agent · 目录

作者提示: 个人观点，仅供参考

继续滑动看下一个

贝叶斯之美

向上滑动看下一个