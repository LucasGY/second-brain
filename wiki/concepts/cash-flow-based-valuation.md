---
type: concept
title: "Cash-Flow-Based Valuation"
aliases: ["现金流估值", "Dividend Multiple", "Shareholder Cash Flow Valuation", "股息倍数"]
tags: [concept, finance]
status: seed
first_seen: 2026-06-29
last_updated: 2026-06-29
summary_en: "Cash-Flow-Based Valuation values shareholder-deliverable cash flows with explicit assumptions for payout, growth, and required return instead of mechanically applying PE multiples."
summary_zh: "现金流估值通过显式假设派现、增长和要求回报率来给可兑现给股东的现金流估值，而不是机械套用 PE 倍数。"
---

# Core Definition
Cash-Flow-Based Valuation values shareholder-deliverable cash flows with explicit assumptions for payout, growth, and required return instead of mechanically applying PE multiples to accounting net income. Source: [[20260629_manual_shareholder-free-cash-flow-all-cash-is-equal|Re-examining “All cash is equal” through Shareholder Free Cash Flow]]
> 现金流估值通过显式假设派现、增长和要求回报率来给可兑现给股东的现金流估值，而不是把 PE 倍数机械地套到会计净利润上。来源：[[20260629_manual_shareholder-free-cash-flow-all-cash-is-equal|从股东自由现金流角度重审 All cash is equal]]

## 🛠️ Mechanisms & Architecture
The simplest zero-growth form is `Value = Shareholder Cash Flow / r`, which means the valuation multiple equals `1 / required return` when growth is zero.
> 最简单的零增长形式是 `价值 = 股东现金流 / r`，这意味着当增长为零时，估值倍数等于 `1 / 要求回报率`。

The growing-perpetuity form is `Fair market value = Shareholder Cash Flow × (1 + g) / (r - g)`, where `g` is long-term shareholder cash-flow growth and `r` is the investor’s required return.
> 永续增长形式是 `合理市值 = 股东现金流 × (1 + g) / (r - g)`，其中 `g` 是股东现金流长期增长率，`r` 是投资者要求回报率。

```mermaid
flowchart TD
    SCF[Shareholder Cash Flow<br/>股东现金流] --> ZERO[Zero-growth value = SCF / r<br/>零增长价值 = SCF / r]
    SCF --> GROW[Growing value = SCF × (1+g)/(r-g)<br/>永续增长价值 = SCF × (1+g)/(r-g)]
    PE[PE = Market Cap / Net Income<br/>市盈率 = 市值 / 净利润] --> PDR[P/Dividend = PE / Payout Ratio<br/>股息倍数 = PE / 股利支付率]
    YIELD[Dividend Yield = Dividends / Market Cap<br/>股息率 = 分红 / 市值] --> PDR2[P/Dividend = 1 / Dividend Yield<br/>股息倍数 = 1 / 股息率]
```

* **Dividend multiple:** `Market cap / dividends = 1 / dividend yield`, so a 4.2% dividend yield implies a roughly `1 / 0.042 = 23.8x` dividend multiple. Source: [[20260629_manual_shareholder-free-cash-flow-all-cash-is-equal|Re-examining “All cash is equal”]]
  > **股息倍数：** `市值 / 分红 = 1 / 股息率`，因此 4.2% 股息率隐含约 `1 / 0.042 = 23.8 倍` 股息倍数。来源：[[20260629_manual_shareholder-free-cash-flow-all-cash-is-equal|重审 All cash is equal]]
* **PE bridge:** `Dividend multiple = PE / dividend payout ratio`, so a company can have a sub-10 PE and a 20–30x dividend multiple if it pays out only part of earnings.
  > **PE 桥梁：** `股息倍数 = PE / 股利支付率`，因此如果公司只分配部分利润，它可以同时拥有低于 10 倍的 PE 和 20–30 倍股息倍数。
* **Sensitivity:** The denominator `r - g` is the most sensitive part of the growing-perpetuity model; small changes in long-term growth or required return can cause large valuation changes.
  > **敏感性：** `r - g` 是永续增长模型最敏感的部分；长期增长率或要求回报率的小变化，可能造成估值的大幅变化。

## ⚔️ Contradictions & Evolution
No contradiction was found in the existing wiki; this page formalizes a valuation bridge between PE, payout ratios, dividend yield, and shareholder cash-flow discounting.
> 既有 wiki 中未发现冲突；本页形式化了 PE、派现率、股息率和股东现金流折现之间的估值桥梁。

## 🚀 Implementations & Best Practices
Use cash-flow-based valuation when the investment question is about mature companies, capital return, trapped cash, or market-level valuation gaps caused by payout differences.
> 当投资问题涉及成熟企业、资本回报、受困现金，或由派现差异造成的市场估值差距时，应使用现金流估值。

Separate the valuation of current distributable cash flow from the valuation of retained capital that can earn high returns; high-ROIC reinvestment should not be penalized merely because it is not paid out immediately.
> 应区分当前可分配现金流的估值与能够获得高回报的留存资本估值；高 ROIC 再投资不应仅因没有立刻派现而被惩罚。

## 📚 Source Mentions
* [[20260629_manual_shareholder-free-cash-flow-all-cash-is-equal|Re-examining “All cash is equal” through Shareholder Free Cash Flow]]

## 🕸️ Relationships

### Related Concepts
[[shareholder-free-cash-flow|Shareholder Free Cash Flow]], [[shareholder-cash-flow-conversion-efficiency|Shareholder Cash Flow Conversion Efficiency]]
> [[shareholder-free-cash-flow|股东自由现金流]]、[[shareholder-cash-flow-conversion-efficiency|股东现金流兑现效率]]

### Related Entities
[[industrial-and-commercial-bank-of-china|Industrial and Commercial Bank of China]], [[coca-cola|Coca-Cola]], [[wuliangye|Wuliangye]]
> [[industrial-and-commercial-bank-of-china|工商银行]]、[[coca-cola|可口可乐]]、[[wuliangye|五粮液]]
