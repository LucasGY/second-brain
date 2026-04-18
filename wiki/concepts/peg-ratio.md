---
type: concept
title: "PEG Ratio"
aliases: ["Price/Earnings to Growth", "P/E-to-Growth"]
tags: [concept, finance, strategy]
status: seed
first_seen: 2026-04-18
last_updated: 2026-04-18
summary_en: PEG Ratio is a valuation framework that scales a price/earnings multiple by earnings growth, helping compare whether a growth asset is expensive or cheap relative to its expected expansion rate.
summary_zh: PEG Ratio（市盈增长比）是一种用盈利增长对市盈率进行缩放的估值框架，用于比较成长型资产相对于预期增速是昂贵还是便宜。
---

# Core Definition
[[peg-ratio|PEG Ratio]] is a relative-valuation measure that divides a P/E multiple by an earnings-growth rate so that investors can compare whether different growth assets are being priced richly or cheaply for their expected expansion.
[[peg-ratio|PEG Ratio]] 是一种相对估值指标，它用盈利增长率去缩放市盈率，从而帮助投资者比较不同成长型资产是否被高估或低估。

## 🛠️ Mechanisms & Architecture
- **Forward PEG:** The standard formulation in strategy work is forward P/E divided by a forward earnings-growth rate, often the “second 12-month forward EPS growth” to avoid mixing near-term base effects with the valuation multiple. Source: [[20260418_manual_gs_technology_value_opportunity|GS Global Strategy Views: The Technology Value Opportunity]]
  **前瞻 PEG：** 策略研究中最常见的写法是“前瞻 P/E ÷ 前瞻盈利增速”，并经常使用“第二个 12 个月 EPS 增速”作为分母，以避免短期基数效应干扰估值倍数。来源：[[20260418_manual_gs_technology_value_opportunity|GS Global Strategy Views: The Technology Value Opportunity]]
- **Trailing or look-back PEG:** A variant divides current P/E by historical earnings CAGR, which shows how much valuation investors are paying relative to realized growth rather than consensus growth.
  **回看型 PEG：** 另一种变体是“当前 P/E ÷ 历史盈利 CAGR”，它反映市场针对“已实现增长”而非一致预期增长支付了多少估值。
- **Interpretation:** A lower PEG can mean a stock or sector became cheaper, growth expectations improved, or both; therefore it must be interpreted together with revisions, ROE, and rate sensitivity.
  **解读方式：** 更低的 PEG 可能意味着价格下跌、增长预期上调，或两者兼有；因此必须结合盈利修正、ROE 和利率敏感性一起看。

## ⚔️ Contradictions & Evolution
- PEG looks objective, but its denominator is often the weakest input because analyst growth estimates adjust more slowly than market prices; a “cheap” PEG can disappear if estimates are later cut.
  PEG 看似客观，但它最脆弱的部分往往是分母，因为分析师增长预测通常比市场价格调整更慢；如果之后盈利预期被下修，看起来“便宜”的 PEG 也可能迅速消失。
- In [[20260418_manual_gs_technology_value_opportunity|GS Global Strategy Views: The Technology Value Opportunity]], the low PEG for global tech is used to argue valuation reset; the counter-risk is that growth expectations may simply be lagging the drawdown.
  在 [[20260418_manual_gs_technology_value_opportunity|GS Global Strategy Views: The Technology Value Opportunity]] 中，全球科技板块的低 PEG 被用来支持“估值已重置”的判断；相反的风险在于，增长预期只是滞后于价格下跌。

## 🚀 Implementations & Best Practices
- Use PEG mainly for comparing growth-heavy sectors or companies where plain P/E overstates cheapness or expensiveness.
  PEG 最适合用于比较成长占主导的行业或公司，因为单独看 P/E 往往会夸大“贵”或“便宜”的判断。
- Pair PEG with earnings revisions, balance-sheet strength, and cash-flow durability before treating it as an allocation signal.
  在把 PEG 当作配置依据之前，应同时检查盈利修正、资产负债表强弱和现金流持续性。
- Avoid using PEG mechanically across highly cyclical businesses whose growth rates swing with the cycle.
  不应把 PEG 机械地用于高度周期性行业，因为这类公司的增长率会随着周期剧烈波动。

## 📚 Source Mentions
- [[20260418_manual_gs_technology_value_opportunity|GS Global Strategy Views: The Technology Value Opportunity]]

## 🕸️ Relationships

### Related Concepts
[[technology-sector-rotation|Technology Sector Rotation]], [[ai-infrastructure-spending|AI Infrastructure Spending]]

### Related Entities
[[goldman-sachs|Goldman Sachs]]
