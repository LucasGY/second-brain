---
type: analysis
title: New Zealand RV PRV Citizenship Annotated Flowchart HTML Source
slug: "20260517_mcp_new-zealand-rv-prv-citizenship-annotated-flowchart-html-source"
title_en: "New Zealand RV PRV Citizenship Annotated Flowchart HTML Source"
title_zh: "新西兰 RV、PRV 与入籍 Annotated Flowchart HTML 源码版"
aliases:
- 新西兰 RV、PRV 与入籍 Annotated Flowchart HTML 源码版
date_created: '2026-05-17'
last_updated: '2026-05-17'
source: MCP conversation capture
tags:
- immigration
- new-zealand
- rv
- prv
- citizenship
- html-source
- annotated-flowchart
- obsidian
- custom-frames
- second-brain
summary_en: The actual standalone HTML source for the New Zealand RV to PRV to citizenship
  annotated flowchart. This note exists because the previous second-brain page stored
  only the design/specification, not the HTML source itself.
summary_zh: 新西兰 RV 到 PRV 再到入籍 annotated flowchart 的独立 HTML 源码版。创建本页是因为上一版 second-brain
  页面只保存了设计说明，没有把 HTML 源码本身放入第二大脑。
artifact_html: "20260517_mcp_new-zealand-rv-prv-citizenship-annotated-flowchart-html-source.html"
---

# New Zealand RV PRV Citizenship Annotated Flowchart HTML Source
> 新西兰 RV、PRV 与入籍 Annotated Flowchart HTML 源码版

## HTML Artifact
Open the HTML artifact below. The iframe works as a direct fallback; the Custom Frames block is kept for desktop setups where the plugin transforms `custom-frames` code blocks.
> 在下方打开 HTML artifact。`iframe` 是直接备用方案；Custom Frames 代码块保留给桌面端插件能转换 `custom-frames` 代码块的场景。

<iframe src="https://www.lucasgou.cloud/second-brain-html/20260517_mcp_new-zealand-rv-prv-citizenship-annotated-flowchart-html-source.html" style="width:100%;height:760px;border:1px solid #d0d7de;border-radius:8px;background:#fff;" loading="lazy"></iframe>

If the iframe is hidden by your Obsidian client, open the direct artifact URL.
> 如果你的 Obsidian 客户端隐藏了 iframe，请打开直接 artifact 链接。

```custom-frames
frame: Second Brain HTML
style: height: 760px;
urlSuffix: /20260517_mcp_new-zealand-rv-prv-citizenship-annotated-flowchart-html-source.html
```

Direct artifact URL: https://www.lucasgou.cloud/second-brain-html/20260517_mcp_new-zealand-rv-prv-citizenship-annotated-flowchart-html-source.html
> 直接访问 artifact：https://www.lucasgou.cloud/second-brain-html/20260517_mcp_new-zealand-rv-prv-citizenship-annotated-flowchart-html-source.html

## Summary
The actual standalone HTML source for the New Zealand RV to PRV to citizenship annotated flowchart. This note exists because the previous second-brain page stored only the design/specification, not the HTML source itself.
> 新西兰 RV 到 PRV 再到入籍 annotated flowchart 的独立 HTML 源码版。创建本页是因为上一版 second-brain 页面只保存了设计说明，没有把 HTML 源码本身放入第二大脑。

## Knowledge
# New Zealand RV → PRV → Citizenship Annotated Flowchart HTML Source

This note stores the actual standalone HTML source, not just the design specification. Copy the code block below into a file named `nz-rv-prv-citizenship-flowchart.html`, or use it as the source for an Obsidian Custom Frames/local HTML artifact.

## What this HTML contains

- TL;DR number cards: 2y, 184, 240, 1350.
- Annotated flowchart layout.
- Flow nodes for RV start, PRV 2-year threshold, PRV 184/184 test, PRV possible point, citizenship 240/1350 test, and citizenship possible point.
- Right-side style explanation panel using native `<details>` blocks instead of JavaScript.
- Timeline, backward-counting table, FAQ, and official-source reminders.

## Standalone HTML source

```html
<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>新西兰 RV → PRV → 国籍 Annotated Flowchart</title>
<style>
:root{--bg:#f6f7f9;--paper:#fff;--ink:#111827;--muted:#667085;--line:#d8dee8;--blue:#2563eb;--blue2:#eff6ff;--green:#059669;--green2:#ecfdf5;--amber:#d97706;--amber2:#fffbeb;--red:#dc2626;--red2:#fef2f2;--purple:#7c3aed;--purple2:#f5f3ff;--shadow:0 18px 45px rgba(15,23,42,.08);--radius:22px;--sans:-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans SC","PingFang SC","Microsoft YaHei",Arial,sans-serif;--mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}*{box-sizing:border-box}body{margin:0;background:radial-gradient(circle at 10% 0,rgba(37,99,235,.1),transparent 30rem),radial-gradient(circle at 90% 0,rgba(124,58,237,.09),transparent 28rem),var(--bg);color:var(--ink);font-family:var(--sans);line-height:1.55}main{max-width:1180px;margin:auto;padding:34px 18px 56px}.hero,.section{background:rgba(255,255,255,.94);border:1px solid var(--line);border-radius:28px;box-shadow:var(--shadow);padding:28px;margin-bottom:24px}.hero{display:grid;grid-template-columns:1.4fr 360px;gap:24px}.eyebrow{font:800 12px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}h1{margin:.3rem 0 1rem;font-size:clamp(32px,5vw,56px);line-height:1.04;letter-spacing:-.055em}h2{margin:0 0 14px;font-size:26px;letter-spacing:-.035em}.lead{font-size:18px;color:#374151;max-width:760px}.stats{display:grid;gap:10px}.stat{display:grid;grid-template-columns:76px 1fr;gap:12px;align-items:center;border-top:1px solid var(--line);padding:12px 0}.stat:first-child{border-top:0}.stat b{font-size:29px;color:var(--blue);letter-spacing:-.05em}.stat span{font-size:13px;color:var(--muted)}.legend{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:18px}.pill{border:1px solid var(--line);border-radius:99px;padding:5px 9px;background:white;font-size:13px;color:var(--muted)}.grid{display:grid;grid-template-columns:minmax(0,1fr) 360px;gap:18px;align-items:start}.flow{border:1px solid var(--line);border-radius:24px;background:#fbfdff;padding:20px;display:grid;gap:10px;overflow-x:auto}.row{display:grid;grid-template-columns:1fr 44px 1fr;gap:10px;align-items:center}.single{grid-template-columns:1fr;max-width:440px;margin:auto}.node{display:block;border:2px solid var(--line);border-radius:16px;background:white;padding:14px 15px;min-height:90px;box-shadow:0 8px 18px rgba(15,23,42,.05);text-decoration:none;color:inherit}.node:hover{border-color:var(--blue);background:var(--blue2)}.process{border-color:#93c5fd}.decision{border-style:dashed;border-color:#fbbf24;background:var(--amber2)}.pass{border-color:#86efac;background:var(--green2)}.fail{border-color:#fca5a5;background:var(--red2)}.end{border-color:#c4b5fd;background:var(--purple2)}.type{display:block;font:700 12px var(--mono);color:var(--muted);margin-bottom:5px}.title{font-weight:900;font-size:15px;line-height:1.25}.meta{display:block;margin-top:6px;color:var(--muted);font-size:12px}.arrow,.down{text-align:center;color:#94a3b8;font-weight:900;font-size:23px}.panel{position:sticky;top:18px;border:1px solid var(--line);border-radius:24px;background:white;padding:20px;box-shadow:0 12px 28px rgba(15,23,42,.07)}details{border:1px solid var(--line);border-radius:16px;background:#fbfdff;padding:13px 15px;margin-bottom:10px}summary{cursor:pointer;font-weight:900}details p,details li{color:#374151}.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.card{border:1px solid var(--line);border-radius:18px;padding:18px;background:#fbfdff}.card h3{margin:0 0 8px}.card p{margin:0;color:#374151}.timeline{display:grid;gap:12px}.titem{display:grid;grid-template-columns:190px 1fr;gap:14px;border:1px solid var(--line);border-radius:18px;padding:14px;background:#fbfdff}.date{font:900 14px var(--mono);color:var(--blue)}table{width:100%;border-collapse:collapse;border-radius:16px;overflow:hidden;box-shadow:0 0 0 1px var(--line)}th,td{border:1px solid var(--line);padding:12px;text-align:left;vertical-align:top}th{background:#f8fafc}td{background:white;color:#374151}.refs{color:var(--muted);font-size:13px}@media(max-width:980px){.hero,.grid,.cards{grid-template-columns:1fr}.panel{position:static}.titem{grid-template-columns:1fr}}@media(max-width:720px){main{padding:20px 12px 42px}.row,.single{grid-template-columns:1fr;max-width:none}.arrow{transform:rotate(90deg)}}
</style>
</head>
<body>
<main>
<header class="hero">
<section>
<div class="eyebrow">Annotated Flowchart · RV → PRV → Citizenship</div>
<h1>新西兰 RV 到 PRV 再到入籍：点击式判断流程</h1>
<p class="lead">这不是正文镜像，而是一张结构化决策图：左侧看流程，右侧看节点解释、风险和下一步。</p>
</section>
<aside class="stats">
<div class="stat"><b>2y</b><span>PRV 通常先看 resident 身份是否满 2 年。</span></div>
<div class="stat"><b>184</b><span>PRV 居住路径：申请日前两个 12 个月区间各 184+ 天。</span></div>
<div class="stat"><b>240</b><span>入籍：5 年窗口内每个 12 个月区间 240+ 天。</span></div>
<div class="stat"><b>1350</b><span>入籍：5 年合计 1,350+ resident days。</span></div>
</aside>
</header>
<section class="section">
<h2>主流程图</h2>
<div class="legend"><span class="pill">process</span><span class="pill">decision</span><span class="pill">pass path</span><span class="pill">fail path</span><span class="pill">terminal</span></div>
<div class="grid">
<div class="flow">
<div class="row single"><a class="node process" href="#start"><span class="type">process · 起点</span><span class="title">拿到 Resident Visa / 开始 resident 身份</span><span class="meta">境内批签 vs 境外批签，起算点不同</span></a></div><div class="down">↓</div>
<div class="row single"><a class="node decision" href="#two-years"><span class="type">decision · PRV 第一道门槛</span><span class="title">resident 身份是否已经满 2 年？</span><span class="meta">不是第二年住够 184 天就自动满足</span></a></div><div class="down">↓</div>
<div class="row"><a class="node fail" href="#wait"><span class="type">fail path · 否</span><span class="title">继续等待 2 年周年日</span><span class="meta">同时继续累计在新西兰天数</span></a><div class="arrow">→</div><a class="node decision" href="#prv184"><span class="type">decision · PRV commitment</span><span class="title">申请日前两个 12 个月区间是否各有 184+ 天？</span><span class="meta">从实际 PRV 申请日往前倒推</span></a></div><div class="down">↓</div>
<div class="row"><a class="node fail" href="#delay-prv"><span class="type">fail path · 否</span><span class="title">推迟 PRV 或研究其他 commitment 路径</span><span class="meta">税务居民、投资、生意、established base 等</span></a><div class="arrow">→</div><a class="node pass" href="#possible-prv"><span class="type">pass path · 是</span><span class="title">可能达到 PRV 申请节点</span><span class="meta">仍需满足身份、条件、材料要求</span></a></div><div class="down">↓</div>
<div class="row single"><a class="node process" href="#keep"><span class="type">process · 继续累计</span><span class="title">继续累计入籍用 resident days</span><span class="meta">PRV 通常不重置入籍 5 年计时</span></a></div><div class="down">↓</div>
<div class="row single"><a class="node decision" href="#citizenship"><span class="type">decision · citizenship presence</span><span class="title">过去 5 年是否每个 12 个月 240+ 天，且总计 1,350+ 天？</span><span class="meta">从国籍申请日往前倒推</span></a></div><div class="down">↓</div>
<div class="row"><a class="node fail" href="#delay-cit"><span class="type">fail path · 否</span><span class="title">继续累计 presence</span><span class="meta">长期离境会推迟申请点</span></a><div class="arrow">→</div><a class="node end" href="#possible-cit"><span class="type">terminal · 可能申请</span><span class="title">可能达到 citizenship by grant 申请节点</span><span class="meta">还要看品行、英语、意图和 ceremony</span></a></div>
</div>
<aside class="panel">
<h2>节点解释</h2>
<details id="start" open><summary>起点：RV / resident 身份</summary><p>记录 RV 批签日，以及首次以 resident 身份实际在新西兰的日期。境内获批通常从批签日算；境外获批常要看首次以 resident 身份入境。</p></details>
<details id="two-years"><summary>PRV 2 年门槛</summary><p>PRV 不是第二年住满 184 天就自动触发。通常还要 resident 身份已经满 2 年。</p></details>
<details id="wait"><summary>如果未满 2 年</summary><p>继续等待 2 年周年日，同时注意 travel conditions 和出入境计划。</p></details>
<details id="prv184"><summary>PRV 184 / 184</summary><p>从 PRV 申请日往前倒推 24 个月，每个 12 个月区间都要有 184+ 天在新西兰以 resident 身份居住。</p></details>
<details id="delay-prv"><summary>PRV 不满足 184/184</summary><p>可以推迟申请，或研究税务居民、投资、生意、established base 等其他 commitment 路径。</p></details>
<details id="possible-prv"><summary>可能申请 PRV</summary><p>如果 resident 满 2 年且两个 184 天区间满足，PRV 时间点通常比较稳。PRV 重要原因之一是 travel conditions 更稳定。</p></details>
<details id="keep"><summary>继续累计入籍天数</summary><p>PRV 通常不重置入籍 5 年计时。RV/resident 时间如果符合要求，通常可以计入。</p></details>
<details id="citizenship"><summary>入籍 240 × 5 + 1350</summary><p>从国籍申请日往前倒推 5 年：每个 12 个月区间 240+ 天，5 年合计 1,350+ 天。</p></details>
<details id="delay-cit"><summary>入籍天数不够</summary><p>继续累计 presence，并从新的申请日重新倒推 5 年。长期离境会推迟申请点。</p></details>
<details id="possible-cit"><summary>可能申请入籍</summary><p>居住天数只是入籍的一部分，还要看身份、品行、英语、继续居住意图和 ceremony。</p></details>
</aside>
</div>
</section>
<section class="section"><h2>规则卡片</h2><div class="cards"><div class="card"><h3>PRV：2 年门槛</h3><p>通常需要连续持有 resident visa 至少 2 年。</p></div><div class="card"><h3>PRV：184 / 184</h3><p>申请日前立即过去 2 年，每个 12 个月区间 184+ 天。</p></div><div class="card"><h3>国籍：240 × 5 + 1350</h3><p>每个 12 个月区间 240+ 天，5 年合计 1,350+ 天。</p></div></div></section>
<section class="section"><h2>示例时间线：2024-07-01 境内拿 RV</h2><div class="timeline"><div class="titem"><div class="date">2024-07-01</div><div><b>RV 获批</b><p>resident 计时开始。</p></div></div><div class="titem"><div class="date">2024-07-01 → 2025-06-30</div><div><b>PRV 第一个 12 个月区间</b><p>目标 184+ 天。</p></div></div><div class="titem"><div class="date">2025-07-01 → 2026-06-30</div><div><b>PRV 第二个 12 个月区间</b><p>目标 184+ 天。</p></div></div><div class="titem"><div class="date">2026-07-01</div><div><b>可能达到 PRV 申请点</b><p>前提是 resident 满 2 年且两个 184 天区间满足。</p></div></div><div class="titem"><div class="date">2024-07-01 → 2029-06-30</div><div><b>入籍 5 年窗口</b><p>每个 12 个月 240+ 天，5 年合计 1,350+ 天。</p></div></div><div class="titem"><div class="date">约 2029-07-01</div><div><b>可能达到入籍申请点</b><p>还要满足其他入籍要求。</p></div></div></div></section>
<section class="section"><h2>倒推检查表</h2><table><thead><tr><th>申请</th><th>倒推窗口</th><th>通过标准</th><th>常见问题</th></tr></thead><tbody><tr><td><b>PRV</b></td><td>从 PRV 申请日往前 24 个月。</td><td>两个 12 个月区间各 184+ 天，并且 resident 满 2 年。</td><td>住满第二年 184 天，但 2 年周年日未到。</td></tr><tr><td><b>Citizenship</b></td><td>从国籍申请日往前 5 年。</td><td>每个 12 个月 240+ 天，合计 1,350+ 天。</td><td>总天数够，但某个 12 个月区间低于 240 天。</td></tr></tbody></table></section>
<section class="section"><h2>FAQ</h2><details open><summary>国籍是从 RV 还是 PRV 开始算？</summary><p>通常不是从 PRV 重新算。RV/resident 时间如果符合要求，通常可以计入。</p></details><details><summary>为什么 PRV 仍然重要？</summary><p>因为 RV 通常带 travel conditions；PRV 通常带 indefinite travel conditions，离境返回更稳定。</p></details><details><summary>不满足 PRV 184/184 怎么办？</summary><p>可以推迟申请，或研究税务居民、投资、生意、established base 等 commitment 路径。</p></details></section>
<section class="section"><h2>官方依据提示</h2><ul class="refs"><li>Immigration New Zealand — Permanent Resident Visa.</li><li>Immigration New Zealand — Showing your commitment to New Zealand for permanent residence.</li><li>New Zealand Government — Presence in NZ requirements for citizenship.</li></ul></section>
</main>
</body>
</html>
```

## Obsidian usage

- Option A: copy the code block into an `.html` file inside the vault and embed it through Custom Frames.
- Option B: use it as a local attachment opened from Obsidian.
- Option C: keep this note as the source-of-truth HTML snippet and update the actual artifact from it.
> # 新西兰 RV → PRV → 入籍 Annotated Flowchart HTML 源码版
>
> 这篇笔记保存的是**实际 HTML 源码本身**，不是设计说明。把上面的代码块复制到 `nz-rv-prv-citizenship-flowchart.html`，即可作为独立 HTML 文件使用，也可以通过 Obsidian Custom Frames 嵌入。
>
> ## 这次修正了什么
>
> - 不再只是保存“应该怎么设计”的说明。
> - 第二大脑里现在有完整可复制的 HTML 源码。
> - HTML 是独立文件格式，包含 CSS 和页面结构。
> - 为了在第二大脑里更安全地保存，使用原生 `<details>` 做节点解释，没有使用 JavaScript。
>
> ## 使用方式
>
> 1. 在第二大脑中打开本页。
> 2. 复制英文部分的 `Standalone HTML source` 代码块。
> 3. 保存为 `.html` 文件。
> 4. 在 Obsidian Custom Frames 中指向该文件或本地服务器地址。
>
> ## 对应主题
>
> 这份 HTML 展示的是新西兰 RV → PRV → 入籍的 annotated flowchart：
>
> - RV 起点。
> - PRV 2 年门槛。
> - PRV 两个 12 个月区间各 184 天。
> - PRV 不满足时的其他 commitment 路径。
> - PRV 后继续累计入籍天数。
> - 入籍 5 年、每个 12 个月 240 天、总计 1,350 天。
> - 常见误区与示例时间线。

## Related
[[20260517_mcp_new-zealand-rv-prv-citizenship-annotated-flowchart-html]], [[20260517_mcp_new-zealand-rv-to-prv-to-citizenship-complete-guide]]
> 相关页面：[[20260517_mcp_new-zealand-rv-prv-citizenship-annotated-flowchart-html]], [[20260517_mcp_new-zealand-rv-to-prv-to-citizenship-complete-guide]]
