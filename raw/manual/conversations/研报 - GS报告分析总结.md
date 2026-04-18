---
title: "研报 - GS报告分析总结"
source: "https://chatgpt.com/g/g-p-69e302f10b3c8191a73ff88a7a1cbbb9-yan-bao/c/69e3059a-758c-83ea-93a2-8113cd5c0a04"
---

## 一、正文 10 条结论

### 1）2025 年以来，美国股市相对全球主要市场跑输，全球配置开始“再平衡”

原文开头直接写：自 2025 年初到伊朗战争开始前，美国股市跑输；背后原因包括美元走弱，以及日本、德国财政刺激改善了这些地区的增长前景（PDF p.1, lines 1-8）。

**支撑数据 / 指标**

* **Exhibit 1：主要市场价格表现（美元计价，2025/1/1=100）**
    * S&P 500
    * STOXX Europe 600
    * Topix
    * MSCI AC Asia Pacific ex-Japan

**这些指标怎么计算**

* **价格表现指数（indexed price performance）**  
    公式： $$\text{Indexed Level}_t = \frac{P_t}{P_{0}} \times 100$$ 其中 $P_0$ 是 2025 年 1 月 1 日价格或价格指数水平。
* **美元计价**  
    如果原始指数是本币，则先换成美元： $$P_t^{USD} = P_t^{Local} \times FX_t$$ 再做上面的 100 基准化。
* 这类图看的不是绝对估值，而是**相对涨跌路径**。

**买方解读**

* 这条结论本质是在说：过去十多年“美国例外论”单边交易开始松动，全球资金配置从过度集中美国，转向更均衡的地域分散。

* * *

### 2）科技板块在 2025 年也出现了极罕见的相对跑输

GS 说，科技板块在 DeepSeek 发布后曾明显跑输，市场开始担心科技龙头的护城河；虽然随后因业绩反弹，但截至报告时点，这仍是自 1970 年代初以来最差的几段相对表现之一（PDF p.1, lines 9-14；p.2, lines 1-3）。

**支撑数据 / 指标**

* **Exhibit 2：World Tech 相对 World ex TMT 的收益分布（1973 年以来）**
* **Exhibit 3：Value 相对 Growth 的近期相对收益**

**这些指标怎么计算**

1. **科技相对非科技的相对收益**
    * 最常见做法是先构造相对价格指数： $$\text{RelIndex}_t = \frac{\text{World Tech Index}_t}{\text{World ex TMT Index}_t}$$
    * 再算某一时间段累计相对收益： $$\text{Relative Return}_{t_0 \to t} = \frac{\text{RelIndex}_t}{\text{RelIndex}_{t_0}} - 1$$
    * 图里“Jan~Dec 的历史分布”大概率是：**把每一年从 1 月开始的科技相对非科技累计收益，按月份做历史分布**。
2. **Value vs Growth 相对价格回报** $$\text{Value/Growth Relative Index}_t  
    =  
    \frac{\text{MSCI Value}_t}{\text{MSCI Growth}_t}$$ 指数上升 = Value 跑赢 Growth。

**买方解读**

* 这不是简单的“科技跌了”，而是：
    1. 科技相对非科技显著跑输；
    2. 风格上 Value 重新跑赢 Growth。
* 这说明市场从“确定性成长”转向“便宜、实体、周期/价值”。

* * *

### 3）这种“地域 + 行业 + 风格”的 broadening out，反而给美国和科技带来回补机会

GS 认为，市场的广度扩散已经让此前的落后资产重新有吸引力，尤其是美国市场：**美国盈利没坏，但价格先回调了，导致相对估值不再那么贵**（PDF p.2, lines 5-8；p.3, lines 2-3）。

**支撑数据 / 指标**

* **Exhibit 4：美国 vs 世界其余地区的 PEG ratio 重置**
* 前文的 **Exhibit 1 / 2 / 3** 共同说明“价格先重置”

**核心指标：PEG ratio**

* 报告写得很清楚：  
    **PEG = 12m forward P/E ÷ second 12m forward EPS growth**（PDF p.3, lines 14-15）

**详细计算方式**

1. **12m forward P/E** $$\text{Forward P/E} = \frac{\text{Current Price or Index Level}}{\text{Next 12M Consensus EPS}}$$
2. **second 12m forward EPS growth**
    
    * 这在卖方策略里通常指“未来第 2 个 12 个月区间的 EPS 增速”，可近似理解为：
    
    $$g_{2nd12m} = \frac{\text{EPS}_{12-24m}}{\text{EPS}_{0-12m}} - 1$$
    
    * 若用财年口径近似：
    
    $$g_{FY2} = \frac{EPS_{FY2}}{EPS_{FY1}} - 1$$
3. **PEG**
    
    * 若增速用“百分数”表示，通常写成：
    
    $$PEG = \frac{Forward\ P/E}{100 \times g}$$ 例如 20x P/E、10% growth，则 PEG = 2.0。

* **PEG 下行**有两种可能：
    1. 估值下降更快；
    2. 增长预期没怎么掉。  
        这正是 GS 想表达的“价格重置快于基本面恶化”。

**买方解读**

* 这是全篇最关键的桥：  
    **价格下来了，但盈利预期还没塌，所以美国/科技从“高估成长”变成“相对便宜成长”。**

* * *

### 4）科技板块本身也出现了估值机会：其 PEG 已低于全球大盘

GS 说，科技相对预期增长的估值，已经跌到**低于全球整体市场**；软件和硬件拆开看，PEG 都不高（PDF p.3, lines 5-12；附录 p.15, lines 5-35）。

**支撑数据 / 指标**

* **Exhibit 5：MSCI AC World IT 的 PEG 低于 MSCI AC World**
* **Exhibit 24：Software & Services、Hardware & Equipment 的 PEG 拆分**
* **Exhibit 6：基于历史盈利的“回看型”PEG 也已极低**

**这些指标怎么计算**

1. **前瞻 PEG**  
    同上： $$PEG_{fwd} = \frac{12m\ forward\ P/E}{2nd\ 12m\ forward\ EPS\ growth}$$
2. **“Look-back PEG” / trailing PEG**  
    报告直接写：  
    **P/E divided by 3y EPS CAGR**（PDF p.4, lines 42-43, 70-73） $$PEG_{trail} = \frac{Current\ P/E}{3Y\ EPS\ CAGR}$$ 其中 $$3Y\ EPS\ CAGR = \left(\frac{EPS_t}{EPS_{t-3}}\right)^{1/3} - 1$$

**买方解读**

* 前瞻 PEG 低，说明**未来增长还在，但价格便宜了**。
* 回看 PEG 也低，说明市场已经把很多坏消息提前 price-in。
* GS 还特别提醒：分母的共识增速可能未来会下修，所以 PEG 也可能回升；但至少截至报告时点，**价格的悲观已经比盈利预期走得更快**。

* * *

### 5）科技变弱的原因主要有三类：高资本开支、AI 颠覆风险、以及虚拟世界向物理世界再耦合

这是正文最长的一部分（PDF p.4, lines 6-8；p.5, lines 1-14；p.6, lines 2-13；p.7, lines 3-18）。

#### 5A. Hyperscaler capex 飙升，引发“回报率下降”担忧

**支撑数据 / 指标**

* **Exhibit 7：Hyperscaler capex / CFO 快速上升**
* **Exhibit 8：净负债/权益上升，但仍低**

**计算方式**

1. **Capex as % of cash flow from operations** $$\frac{CAPEX}{CFO} \times 100\%$$
    
    * Hyperscaler 通常是选定的大型云/AI 基建公司聚合。
    * 若做聚合：
    
    $$\frac{\sum CAPEX_i}{\sum CFO_i}$$
2. **Net debt to equity** $$\text{Net Debt / Equity}  
    =  
    \frac{Short\ Debt + Long\ Debt - Cash\&Equivalents}{Book\ Equity}  
    \times 100\%$$

**买方解读**

* 市场担心 AI 基建投入像历史上的铁路、互联网骨干网一样，**先有大规模资本投入，但投资回报未必由出钱的人拿走**。
* 但 GS 也留了一个缓冲：虽然杠杆上来了，**科技板块杠杆水平仍不高**，这不是典型资产负债表危机。

#### 5B. 市场开始担心“谁会成为 AI 时代的 Kodak/Polaroid”

**支撑数据 / 指标**

* **Exhibit 9：AI hyperscalers 的股价相关性下降**
* **Exhibit 10、11：Kodak / Polaroid 的历史股价崩塌**
* **Exhibit 12：软件和科技板块 forward P/E premium 大幅回落**

**计算方式**

1. **3m realised average pairwise correlation**
    
    * 取 AMZN、GOOGL、META、MSFT、ORCL 的日收益率；
    * 用过去约 3 个月（常见是 63 个交易日）计算任意两两相关系数；
    * 再求平均：
    
    $$\bar{\rho}_t  
    =  
    \frac{2}{N(N-1)}  
    \sum_{i<j}\rho(r_i,r_j)$$
2. **Stock price indexed to its maximum** $$\text{Index to Peak}_t = \frac{P_t}{\max(P)} \times 100$$ 用来显示从历史高点回撤了多少。
3. **Software / Tech 相对 ex-TMT 的估值溢价** $$\text{Premium}_t = \left(\frac{PE_{Sector,t}}{PE_{World\ exTMT,t}} - 1\right)\times 100\%$$ 若为负，则是 discount。

**买方解读**

* 相关性下行 = 市场不再把 AI 受益股当成一整个篮子买，而是开始区分赢家和输家。
* 软件板块从溢价到接近市场平均倍数，说明市场在抬高风险溢价、下调终值假设。

#### 5C. 科技成长越来越依赖“物理基础设施”，旧经济迎来 HALO effect

**支撑数据 / 指标**

* **Exhibit 13：CAPEX/Sales 与 P/E premium 的 3 年滚动相关性**
* 文中解释数据中心、能源供应商、资本密集型旧经济被重新估值（PDF p.7, lines 3-18）

**计算方式**

1. **CAPEX/Sales** $$\frac{CAPEX}{Sales}$$
2. **P/E premium vs market** $$\left(\frac{PE_{Sector}}{PE_{Market}} - 1\right)\times 100\%$$
3. **3-year rolling correlation**
    
    * 用滚动 36 个月样本：
    
    $$Corr_t = Corr\big((CAPEX/Sales)_{t-35:t},\ Premium_{t-35:t}\big)$$

**买方解读**

* 当 AI 从“纯软件故事”变成“电力 + 数据中心 + 制造 + 设备”的故事，旧经济的资产稀缺性重新被看见。
* 这解释了为什么 **Energy 的估值跟着 capex 上升而抬升，科技反而去估值**。

* * *

### 6）尽管如此，科技现在已经变成“增长还强、估值已低”的机会

GS 的第 6 条是全篇最直接的投资结论：**科技板块的增长还在，但估值已不贵**（PDF p.8, lines 2-8）。

**支撑数据 / 指标**

* **Exhibit 14：美国科技 Hyperscalers 的估值溢价已接近普通市场**
* **Exhibit 15：全球 IT 的 forward P/E 低于可选消费、必选消费、工业等板块**

**计算方式**

1. **Top 5 vs Other 495 的 forward P/E** $$Forward\ P/E = \frac{Price}{NTM\ EPS}$$ 对组合/篮子做聚合，通常用： $$\frac{\sum Market\ Cap_i}{\sum NTM\ Earnings_i}$$
2. **“相对历史 20 年”的行业估值位置**
    * 当前值：当前 12m forward P/E
    * 历史参照：过去 20 年每月 forward P/E 分布
    * 图中的 median / interquartile / 10th-90th percentile 都是分布统计量

**买方解读**

* 这不是说科技绝对便宜到极端，而是说：  
    **放在全球行业横向比较和自身历史纵向比较里，IT 已经不再是高不可攀的板块。**

* * *

### 7）科技盈利质量并没有坏：ROE 仍高，EPS 修正还最强

GS 认为，市场对 capex 和回报率的担忧有道理，但**盈利能力和盈利趋势都没有同步恶化**（PDF p.9, lines 3-5；p.10, lines 1-10；p.11, lines 1-8）。

**支撑数据 / 指标**

* **Exhibit 16：US TMT 的 P/B 与 ROE 关系**
* **Exhibit 17：IT 的 YTD EPS revisions 最强**
* **Exhibit 18：价格表现与 FY2 EPS 变化出现罕见背离**
* 文中文字：
    * S&P 500 本季度 EPS 同比 +12%
    * 连续第 6 个季度双位数增长
    * IT 行业 EPS +44%
    * 贡献了 Q1 2026E 指数 EPS 增长的 87%
    * AI 投资支出大致贡献今年 S&P EPS 增长的 40%（PDF p.11, lines 1-8）

**计算方式**

1. **ROE** $$ROE = \frac{Net\ Income_{TTM}}{Average\ Shareholders' Equity}$$ 也可用预期净利润 / 期初期末平均净资产。
2. **Price-to-Book** $$P/B = \frac{Market\ Cap}{Book\ Equity}$$
3. **YTD EPS revisions** $$Revision_{YTD}  
    =  
    \left(  
    \frac{Consensus\ EPS_{today}}{Consensus\ EPS_{start\ of\ year}} - 1  
    \right)\times 100\%$$ 图里分别看 2026、2027 两个盈利年度。
4. **3m change in price (3mma)**
    
    * 图没写完整算法，常见还原是：
    
    $$\Delta P_{3m,t} = \frac{P_t}{P_{t-3m}} - 1$$ 再做 3 个月移动平均平滑： $$3MMA_t = \frac{1}{3}\sum_{k=0}^{2}\Delta P_{3m,t-k}$$
5. **3m change in FY2 EPS** $$\Delta EPS^{FY2}_{3m,t}  
    =  
    \frac{EPS^{FY2}_{cons,t}}{EPS^{FY2}_{cons,t-3m}} - 1$$
6. **某板块对指数 EPS 增长的贡献**
    
    * 正确做法不是直接看增速，而是看**盈利增量**：
    
    $$Contribution_i  
    =  
    \frac{\Delta EPS\ Dollars_i}{\Delta EPS\ Dollars_{Index}}$$ 例如 IT 贡献 87%，意味着 IT 的盈利增量占指数总盈利增量的 87%。
7. **AI 投资对指数 EPS 增长的贡献** $$Share_{AI}  
    =  
    \frac{\Delta EPS\ Dollars_{AI\ infra\ or\ AI\ cloud}}{\Delta EPS\ Dollars_{S\&P500}}$$

**买方解读**

* 这是全篇最强的“反市场定价”证据：  
    **价格已经明显弱于盈利。**
* 换句话说，科技板块不是盈利先崩、股价后跌，而更像是**风险溢价先抬升，股价先修正**。

* * *

### 8）科技并不处在泡沫中，因为估值远低于历史泡沫期

GS 明确反驳“AI=泡沫”的简单类比（PDF p.12, lines 2-9）。

**支撑数据 / 指标**

* **Exhibit 21：当下 Mag 7 vs 2000 年科技泡沫龙头 vs 1989 日本泡沫 vs 1973 Nifty Fifty**
* 关键数值：
    * 2026 Mag 7 aggregate：**24m fwd P/E 20.1x，24m fwd EV/Sales 4.8x**
    * 2000 科技泡沫龙头 aggregate：**52.0x，8.2x**
    * 1989 日本泡沫 aggregate：**67.0x P/E**
    * 1973 Nifty 50 aggregate：**34.3x P/E**（PDF p.13, lines 11-168）

**计算方式**

1. **24m forward P/E** $$\frac{Price}{EPS_{24m\ forward}}$$ 或对组合： $$\frac{\sum Market\ Cap}{\sum Earnings_{24m\ forward}}$$
2. **EV/Sales** $$EV/Sales = \frac{Enterprise\ Value}{Sales}$$ 其中 $$EV = Market\ Cap + Debt + Preferred + Minority\ Interest - Cash$$
3. **Market weight** $$Weight_i = \frac{Market\ Cap_i}{Total\ Market\ Cap_{Index}}$$

**买方解读**

* GS 的意思不是“完全没泡沫成分”，而是：  
    **如果只看估值高度，今天远没到 2000/1989 那种极端。**
* 所以更合理的框架是“去拥挤 + 再定价”，不是“全面泡沫破裂”。

* * *

### 9）另一个反泡沫证据：股权融资发行潮还没有出现

GS 说，泡沫往往伴随大量 IPO/增发；但当前美国科技股权融资显著低于 1999-2000 年（PDF p.13, lines 2-9）。

**支撑数据 / 指标**

* **Exhibit 22：欧洲电信 1990s capex boom 伴随股权融资潮**
* **Exhibit 23：美国 TMT 1990s 与现在的 IPO/二级发行数量对比**
* 文中直接提到：2000 年科技泡沫破裂前一年，美国 IPO 大约 **500 家**，而当前只有其零头（PDF p.13, lines 3-5）

**计算方式**

* **Number of IPOs and secondary offerings on a 12-month sum basis** $$IssuanceCount_t = \sum_{m=t-11}^{t} \#(IPO_m + Secondary_m)$$ 即滚动 12 个月发行笔数。

**买方解读**

* 这说明目前更像是**二级市场估值重排**，而不是典型泡沫后期的一级市场疯狂供给。
* 但 GS 也提醒：今年可能有一波 mega-cap tech IPO，这会带来**板块内部分化**，不是整个科技板块必须继续跑输的理由。

* * *

### 10）伊朗战争反而提高了科技的相对吸引力：它可能变成“类防御”

GS 最后一条结论是宏观层面的：伊朗战争使市场先计入更高通胀和更高利率，这短期压制了长久期科技股；但如果霍尔木兹海峡冲击持续，市场叙事可能从“通胀冲击”转成“增长冲击”，届时利率上行受限，而科技现金流对经济增长又相对不敏感，因此科技未来几个月可能变得更防御（PDF p.14, lines 2-10）。

**支撑数据 / 指标**

* 这一段主要是**宏观逻辑推演**，不是用单独新图表验证。
* 前文已经用长久期估值压缩（Exhibit 12）、盈利韧性（Exhibit 16-19）做了铺垫。

**这些指标怎么理解**

1. **长久期股票对利率更敏感**
    
    * DCF 角度：
    
    $$PV = \sum_{t=1}^{\infty}\frac{FCF_t}{(1+r)^t}$$ 科技股更多价值来自远期现金流，所以折现率 $r$ 上升时估值更敏感。
2. **若宏观从“更高通胀”转向“更低增长”**
    * 长端收益率未必继续升；
    * 科技由于现金流与周期相关性相对更低，可能相对防御。

**买方解读**

* GS 在这里其实给了一个战术层面的看多理由：  
    **短期压制科技的宏观变量，未来可能反而转向支撑科技。**

* * *

## 二、附录补充的第 11 条观察

### 11）软件估值波动比硬件更大，但两者的 PEG 都已经不高

附录只放了一张图（PDF p.15, lines 5-35）：

**支撑数据 / 指标**

* **Exhibit 24：MSCI AC World Software & Services、Hardware & Equipment、AC World 的 PEG 对比**

**计算方式**

* 仍然是： $$PEG = \frac{12m\ forward\ P/E}{2nd\ 12m\ forward\ EPS\ growth}$$

**买方解读**

* 软件的估值弹性更大，所以在 AI disruption 叙事下被打得更狠；
* 但 GS 的结论不是回避软件，而是说：**软件和硬件都已经进入“可谈估值”的区间。**

* * *

## 三、把全篇压缩成 4 个真正重要的投资结论

如果从买方角度做二次提炼，这份报告其实只在反复证明 4 件事：

### 1. 美国和科技都经历了“过度拥挤交易”的回撤

证据是：

* 美国跑输全球（Exhibit 1）
* 科技跑输非科技（Exhibit 2）
* Value 跑赢 Growth（Exhibit 3）

### 2. 但这次回撤更像“估值重置”，不是“盈利崩塌”

证据是：

* 美国/科技 PEG 显著回落（Exhibit 4/5/6）
* Hyperscaler 溢价回落（Exhibit 14）
* IT 行业相对历史并不贵（Exhibit 15）

### 3. 市场担心的风险都是真风险，但大多已被价格提前反映

证据是：

* capex/CFO 飙升（Exhibit 7）
* 资产负债表承压但不危险（Exhibit 8）
* 相关性下降、分化上升（Exhibit 9）
* 软件/科技估值溢价塌缩（Exhibit 12）
* 旧经济因 HALO effect 获得重估（Exhibit 13）

### 4. 所以科技现在的投资逻辑是“低估值的优质增长”，不是“无脑追高”

证据是：

* ROE 仍高（Exhibit 16）
* EPS revision 最强（Exhibit 17）
* 盈利与股价出现历史性背离（Exhibit 18）
* AI 投资仍在驱动指数盈利增长（Exhibit 19）
* 估值不像泡沫，发行也不像泡沫（Exhibit 21/22/23）

* * *

## 四、最值得你在实盘里盯的 8 个核心指标

如果你是买方，读完这篇最该跟踪的是这 8 个：

1. **科技板块 forward PEG**  
    看“价格重置是否快于增长预期下修”。
2. **Hyperscaler CAPEX / CFO**  
    看 AI 投资是否进入边际回报下降区间。
3. **净负债 / 权益**  
    看高投入是否开始实质伤害资产负债表。
4. **软件 vs ex-TMT 的 P/E premium**  
    看 AI disruption 风险是否仍在抬升。
5. **Top 5 vs Other 495 的 forward P/E gap**  
    看龙头拥挤度是否继续消化。
6. **IT 的 EPS revisions 与 FY2 EPS 变化**  
    看基本面有没有真的转坏。
7. **IT 对 S&P 500 EPS 增长的贡献**  
    看指数盈利是否仍由 AI/科技驱动。
8. **IPO / secondary issuance 的 12m rolling count**  
    看是否开始出现泡沫后期常见的供给冲击。

* * *

## 五、我的最终判断

站在买方角度，这篇报告的结论可以概括成一句话：

**GS 不是在说“科技风险消失了”，而是在说“科技风险被市场重新定价后，估值已经降到足以补偿这些风险，而盈利和资本回报并未同步塌陷，因此出现了 technology value opportunity”。**

如果你愿意，我可以下一步把这份报告进一步整理成一张更适合买方投委会使用的表：  
**“结论—证据—交易含义—对应风险点”**。

* * *


| 结论 | 证据 | 交易含义 | 对应风险点 |
| --- | --- | --- | --- |
| **1. 2025年以来，全球权益从“美国单边领先”转向更均衡的 broadening-out** | **Exhibit 1**：S&P 500 自 2025/1/1 以来跑输 STOXX Europe 600、Topix、MSCI AC Asia Pacific ex-Japan；报告归因于**美元走弱**、**日本/德国财政刺激**改善相对增长预期 | 过去几年“超配美国、低配非美”的拥挤交易已松动；美国资产不再只能靠叙事溢价支撑，未来需要回到**盈利与估值匹配** | 若美国增长重新显著领先、美元转强、欧洲/日本财政刺激落空，则 broadening-out 可能逆转 |
| **2. 科技板块经历了过去50年罕见的相对跑输** | **Exhibit 2**：World Tech 相对 World ex TMT 的表现处于 1973 年以来极弱区间；**Exhibit 3**：MSCI Value 相对 Growth 明显走强 | 风格上从“长久期成长”切向“价值/实体资产”；科技板块的超额收益预期已大幅降温，拥挤度得到释放 | 若 AI 再次出现强催化、利率快速回落、科技盈利显著超预期，市场可能重新追逐 Growth，Value 轮动中断 |
| **3. 美国市场的相对估值已明显重置，不再像此前那样昂贵** | **Exhibit 4**：美国相对世界其余地区的 **PEG ratio** 已回落并“re-set”；同时美国盈利维持韧性、价格先修正 | 对美国市场应从“高估值风险”转向“精选回补”；尤其是那些**盈利没有被破坏、但估值已回落**的板块/龙头 | 若美国未来 12-24 个月盈利预期下修，当前 PEG 改善可能只是“估值便宜的幻觉” |
| **4. 科技板块已出现“盈利没坏、估值先跌”的 value opportunity** | **Exhibit 5**：MSCI AC World IT 的 **forward PEG** 已低于全球大盘；**Exhibit 6**：基于 **P/E ÷ 3Y EPS CAGR** 的回看型 PEG 也接近历史低位；**Exhibit 24**：软件、硬件拆开看 PEG 都不高 | 这是全篇最重要的交易信号：科技不再只是“贵的成长”，而是开始进入**有估值保护的成长**区间；可考虑逢低增加对高质量科技的配置 | 最大风险是分母错觉：若未来共识 EPS 增速被大幅下修，PEG 会重新抬升；即“现在便宜”可能是因为市场还没来得及砍盈利 |
| **5. 科技跑输的第一层原因，是 Hyperscaler 资本开支激增引发 ROI 担忧** | **Exhibit 7**：Hyperscaler **CAPEX / CFO** 快速抬升；**Exhibit 8**：科技板块 **Net debt / equity** 上升，但整体仍不高 | 交易上不能简单“无脑买所有 AI 受益股”，而应更重视**资本开支纪律、现金流转化、融资能力**；优选能把 capex 变成收入/利润的公司 | 若 AI 基建回报明显低于预期，市场会继续压缩高 capex 科技股估值；若融资环境收紧，现金流弱的公司将承压更大 |
| **6. 科技跑输的第二层原因，是 AI disruption 风险上升，市场开始区分赢家与输家** | **Exhibit 9**：AI hyperscalers 间的 3m pairwise correlation 下降；**Exhibit 10/11**：Kodak、Polaroid 的历史案例；**Exhibit 12**：Software/Tech 相对 ex-TMT 的 forward P/E premium 急剧收缩 | 交易层面应从“板块配置”转向“板块内分化交易”：更偏好**真正受益于 AI 的上游算力/基础设施/少数平台型公司**，回避可能被替代的软件和中间层商业模式 | 如果 AI 商业化进展低于预期，则“受益股”也会被杀估值；若市场对 disruption 的担忧继续发酵，软件估值仍可能进一步下修 |
| **7. 科技跑输的第三层原因，是 AI 投资把增长机会外溢到旧经济，形成 HALO effect** | **Exhibit 13**：能源等旧经济行业里，**CAPEX/Sales 与 P/E premium** 的相关性显著改善；报告强调数据中心、电力、设备、制造等受益 | 不应把 AI 交易只理解为“买软件/大模型”；更合理的是做**AI 资本开支扩散链条**：电力、设备、工业、部分资源品、半导体上游 | 若 AI 基建投资放缓，HALO effect 会减弱；此外，旧经济板块盈利弹性通常更依赖周期，若宏观转弱，估值修复持续性可能不足 |
| **8. 尽管市场担心 capex 和竞争，科技的盈利质量并没有坏** | **Exhibit 16**：US TMT 的 **ROE** 仍高；**Exhibit 17**：IT 的 **EPS revisions** 年初以来最强；**Exhibit 18**：价格与 FY2 EPS 变化出现明显背离；**Exhibit 19**：AI 投资约贡献 2026 年 S&P 500 EPS 增长的 40%，IT 预计贡献 Q1 2026E 指数 EPS 增量的 87% | 这意味着当前科技板块的核心矛盾不是“基本面塌了”，而是“风险溢价抬高了”；若盈利继续兑现，估值修复空间存在 | 若未来几个季度科技 EPS revision 转负，报告的核心前提就会被削弱；尤其要盯住云收入、AI monetization、毛利率和 capex 指引 |
| **9. 当前科技并不像历史大泡沫期那样贵** | **Exhibit 21**：2026 年 Mag 7 aggregate **24m fwd P/E 20.1x、EV/Sales 4.8x**，明显低于 2000 年科技泡沫龙头、1989 日本泡沫、1973 Nifty Fifty | 投委会层面可降低“AI=2000年泡沫翻版”的先验偏见；更适合用**精选、分层配置**而非系统性回避科技 | 虽然整体不算极端泡沫，但个别子行业/个股仍可能很贵；若利率大幅上行、AI 盈利兑现慢于预期，局部泡沫仍会出清 |
| **10. 当前也缺少典型泡沫后期常见的一级市场供给洪峰** | **Exhibit 22/23**：无论欧洲电信 1990s 还是美国 TMT 1990s，泡沫后期都伴随 IPO/增发潮；而当前美国科技股权融资明显温和，远低于 1999-2000 年 | 这支持“当前更像二级市场重定价，而非泡沫末端崩塌”；对科技板块不应一刀切回避，更应做**板块内精选** | 若 2026 年出现一波 mega-cap tech IPO / secondary issuance，可能形成新的流动性分流和估值压力，尤其压制高估值子板块 |
| **11. 伊朗战争带来的宏观冲击，短期压制科技，但中期反而可能提升其防御属性** | 报告认为，目前市场先计入的是**更高通胀/更高利率**，这压制长久期科技；但若霍尔木兹海峡扰动持续，叙事可能转向**增长冲击**，届时科技因现金流相对不敏感、且更受益于利率回落，可能体现防御性 | 若地缘风险延续，科技未必只是“高 beta 受损方”，反而可能在后半程成为相对防御配置；交易上可把科技视作**成长中的防御** | 若油价冲击演变成更持久的高通胀，长端利率持续上行，则科技估值仍会承压；报告这一判断依赖“增长冲击最终压过通胀冲击” |


* * *


## 一张表：哪些指标可以衡量这 3 个部分

1. 美股的价值处于中性或者低估的范围；
2. 科技的价值处于中性或者低估的范围；
3. 可以横向对比相对于其他几个泡沫时期的指标。

| 目标 | 指标 | 图表/口径 | 怎么用来判断”中性或低估” | 报告给出的当前信号 |
| --- | --- | --- | --- | --- |
| **1. 美股价值处于中性或低估范围** | **US vs AC World ex-US 的 PEG ratio** | **Exhibit 4**；PEG = **12m fwd P/E ÷ second 12m fwd EPS growth** | 这是全篇判断美股”没那么贵了”的核心指标。若美股 PEG 相对非美明显回落，说明美股估值已被增长消化，不再是高溢价状态 | GS 直接写 **”The US equity market no longer looks so expensive on a relative basis”**，并称 **”The PEG ratio between the US and the rest of the world has re-set”**。 |
| **1. 美股价值处于中性或低估范围** | **相对价格回撤 + 盈利仍强** | 文本 + **Exhibit 1** | 如果价格先修正、盈利还没坏，往往意味着估值压缩，美股更接近中性 | 报告写美国市场**经历了 correction，但 earnings remained strong**。 |
| **1. 美股价值处于中性或低估范围** | **Value vs Growth 相对收益** | **Exhibit 3** | 当 Value 持续跑赢 Growth，通常说明市场在消化此前成长溢价；对美股整体意味着”贵的部分在被去估值” | GS 用这张图说明过去一段时间发生了**价值风格重估**。 |
| **1. 美股价值处于中性或低估范围** | **相对全球主要市场的表现** | **Exhibit 1**：S&P 500 vs Europe/Japan/APxJ | 美股若在盈利未坏前提下相对全球跑输，通常说明其相对估值在被消化 | 报告开头就强调 2025 年以来美股**相对其他主要市场跑输**。 |
| **2. 科技价值处于中性或低估范围** | **科技 vs 全球市场的 forward PEG** | **Exhibit 5**；PEG = **12m fwd P/E ÷ second 12m fwd EPS growth** | 这是报告判断”科技有 value opportunity”的第一核心指标。若科技 PEG 低于全球大盘，说明市场给予的价格不足以反映其预期增长 | GS 明确写：科技板块估值相对预期增长，**已低于全球 aggregate market**。 |
| **2. 科技价值处于中性或低估范围** | **科技的 trailing / look-back PEG** | **Exhibit 6**；**P/E ÷ 3y EPS CAGR** | 用历史盈利增长去校验当前估值。如果该指标压到历史低位，说明市场已经明显悲观定价 | 报告写科技的 look-back PEG 已低到**接近 2003-05 科技泡沫破裂后低点**。 |
| **2. 科技价值处于中性或低估范围** | **Top 5 Hyperscalers vs Other 495 的 forward P/E 溢价** | **Exhibit 14**；S&P 500 12m forward P/E | 如果龙头科技相对市场其余部分的溢价压缩到接近正常水平，说明拥挤交易已释放，估值回归中性 | GS 写：美国科技 Hyperscalers 的估值溢价**已降到接近市场其他部分**。 |
| **2. 科技价值处于中性或低估范围** | **全球 IT 行业横向行业比较：12m forward P/E** | **Exhibit 15**；Global sectors, 12m forward P/Es relative to last 20 years | 横向看 IT 是否还比消费、工业等行业贵；纵向看是否处在自身历史较低分位 | GS 直接写：全球 IT 的 P/E **低于 consumer discretionary、consumer staples、industrials**，且相对历史的估值溢价也明显下来了。 |
| **2. 科技价值处于中性或低估范围** | **P/B vs ROE** | **Exhibit 16**；US TMT valuations vs ROE | 这是”质量调整后估值”的典型指标。若 ROE 仍高、但 P/B 已回到长期关系线附近，通常意味着不贵 | GS 说：尽管 capex 上行，但 **ROE has remained high**，且板块估值**已经不再高于其与 ROE 的长期关系**。 |
| **2. 科技价值处于中性或低估范围** | **EPS revisions** | **Exhibit 17**；IT 的 2026/2027 EPS revisions | 估值便宜必须配合盈利韧性。如果盈利修正仍强，而价格已经跌，往往意味着被错杀或至少有修复空间 | GS 写 IT 的 earnings revisions **比任何其他板块更正面**。 |
| **2. 科技价值处于中性或低估范围** | **价格 vs FY2 EPS 变化的背离** | **Exhibit 18**；3m change in Price vs 3m change in FY2 EPS | 如果 EPS 预期没明显走坏，但价格先跌，往往说明是风险溢价抬升而非基本面塌陷，这正是价值机会常见来源 | GS 说这造成了 **record gap between performance and underlying earnings growth**。 |
| **2. 科技价值处于中性或低估范围** | **Software / Hardware 分拆 PEG** | **Exhibit 24** | 用来判断”科技便宜”是不是只集中在一个子行业。若软件和硬件都不高，则板块层面机会更广泛 | GS 在正文里点明：**software 和 hardware 两边的 PEG 都低**。 |
| **3. 横向对比相对于其他几个泡沫时期** | **24m forward P/E** | **Exhibit 21**：2026 Mag 7 vs 2000 科技泡沫龙头 | 这是最直接的泡沫横向比较指标。若当前核心龙头的 24m fwd P/E 明显低于历史泡沫龙头，则说明当前估值高度没到当年泡沫级别 | Mag 7 aggregate **20.1x**，而 2000 tech bubble leaders aggregate **52.0x**。 |
| **3. 横向对比相对于其他几个泡沫时期** | **24m forward EV/Sales** | **Exhibit 21** | 当盈利受周期/会计扰动时，EV/Sales 能补充看”为收入付了多高倍数” | Mag 7 aggregate **4.8x**，2000 tech bubble leaders aggregate **8.2x**。 |
| **3. 横向对比相对于其他几个泡沫时期** | **与 1989 日本泡沫、1973 Nifty Fifty 的 P/E 对比** | **Exhibit 21** | 用来避免只拿 2000 科技泡沫做单一比较，能横向看”不同类型泡沫”的估值高度 | 报告说当前主要龙头的估值**不到日本 80 年代末泡沫的一半**，也显著低于 Nifty Fifty。 |
| **3. 横向对比相对于其他几个泡沫时期** | **市场集中度 / Market weight** | **Exhibit 21** | 泡沫不仅看贵不贵，还看集中度。当前 Mag 7 权重大，说明拥挤度高，但不代表估值一定泡沫化 | Mag 7 aggregate market weight **33.7%**，高于 2000 tech bubble leaders 的 **19.0%**。这说明当前是**高集中度，但不一定高估值**。 |
| **3. 横向对比相对于其他几个泡沫时期** | **IPO + Secondary issuance（12个月滚动）** | **Exhibit 22/23** | 泡沫后期常见特征是一级市场融资供给爆发。若发行潮没出现，则更像二级市场重定价，不像泡沫末端 | 报告说 tech bubble burst 前一年美国约有 **500 个 IPO**，而当前只是其一小部分；并明确说目前股权融资**相对 subdued**。 |
| **3. 横向对比相对于其他几个泡沫时期** | **估值与基本面是否脱钩** | **Exhibit 16、18** | 历史泡沫常见”估值远离盈利质量、价格远离盈利趋势”。若当前是反过来的——盈利强、价格弱——则更不像泡沫顶 | 这篇报告恰恰在强调：现在科技是**盈利强但价格弱**，与典型泡沫末期的”价格冲太快”不同。 |

* * *

## 如果你只想保留“最核心、最够用”的指标

我会建议压缩成下面这 **7 个主指标**：

### A. 判断“美股整体是否回到中性”

1. **US vs AC World ex-US PEG**
2. **美股相对全球主要市场的价格回撤 + 盈利是否仍强**

### B. 判断“科技是否进入中性/低估”

3. **Tech vs AC World 的 forward PEG**
4. **Tech look-back PEG（P/E ÷ 3Y EPS CAGR）**
5. **Hyperscaler vs 其他 495 的 forward P/E 溢价**
6. **IT 行业 forward P/E 的横向行业比较 + 历史分位**
7. **P/B vs ROE + EPS revisions + Price/EPS 背离**

### C. 判断“相对历史泡沫是否仍偏低”

8. **24m fwd P/E**
9. **24m fwd EV/Sales**
10. **IPO / secondary issuance 的 12M rolling count**

* * *


如果按“判断力”排序，这篇报告最有用的其实是下面三组：

### 1）判断美股“不再贵”

* **US vs ex-US PEG reset**
* **价格已修正、盈利未明显坏**

### 2）判断科技“已进入价值区间”

* **Tech PEG < Global Market PEG**
* **Look-back PEG 接近历史低位**
* **Hyperscaler 溢价显著收敛**
* **IT relative-to-history 不贵**
* **ROE 仍高、EPS revision 仍强**

### 3）判断“还不像泡沫末期”

* **24m fwd P/E / EV/Sales 远低于 2000、1989、1973**
* **一级市场融资潮未出现**

* * *

