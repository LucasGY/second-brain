---
title: "一文看懂：Hermes Agent与OpenClaw全维度对比"
author: "Draco正在VibeCoding"
publishTime: "2026-04-08"
source: "https://mp.weixin.qq.com/s/JWHBaFVvLE8S1t5jRXQxrg"
coverImage: "https://mmbiz.qpic.cn/mmbiz_jpg/0m9F5vC1OGiaHnbVk3d0licJ8sSRur6UtSun7ZOvE4hbGgMkEQgvY4msic8Z30IV61H9pMUViascKgVEDfyuhTpAIXAWdBWoE8UdIeicM28icsUJU/0?wx_fmt=jpeg"
---

# 一文看懂：Hermes Agent与OpenClaw全维度对比

中推圈终于在今天开始集中讨论Hermes Agent了，大概率未来几天国内AI/Agent头部和腰部媒体、自媒体也会开始对Hermes Agent进行集中报道；然后，maybe，又是一波类似于OpenClaw的FOMO潮流，大家会把“养虾不如养马” 挂在嘴边（OpenClaw是🦞；Hermes是“爱马🐴仕”嘛），直到下一个龙虾或下一个爱马仕的出现。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0m9F5vC1OGiamA6ZZ2iaA7XMHLYDscgE7ZqwNXfHQCblS3AL2UDcVKxg5PE2Bsb4s19NZKmTIwuOMNIhrue81zzwa5NGpMWsAN4PZy5T1x0icQ/640?wx_fmt=jpeg&from=appmsg)

我已经高强度使用Hermes Agent 10天左右，并且在上周将龙虾军团主力切到了Hermes Agent，飞书群里还有2000位热烈讨论Hermes的同学，最常遇到的问题是：

一、对比Hermes Agent和OpenClaw  
二、Hermes究竟有什么优势  
三、发展趋势  
四、文档资源  
五、社群资源

下面就来回答这五个问题。

* * *

# 一、Hermes Agent vs OpenClaw full-table comparison

> 以下内容是我让GPT-5.4在Extra High模式下跑了1个小时，将今天最新版Hermes Agent和OpenClaw的source code放在一起做了apple2apple的客观比较，未携带我的主观评价：

## 拜万恶的公众号编辑器所赐，表格没办法所在一屏宽度内完整展示，劳烦大家左右滑动表格：

## 1\. 一句话总览

| 结论维度 | Hermes Agent | OpenClaw | Comments |
| --- | --- | --- | --- |
| 主要Language | Python | Typescript |  |
| 产品姿态 | 以单个 Python Agent 为核心，向外扩出 messaging、ACP、MCP、cron、skills | 以本地 Gateway / Control Plane 为中心，把 Pi Agent、channels、plugins、sessions、nodes、ACP 统一编排 | Hermes 更像“自进化工作型 Agent”；<br>OpenClaw 更像“本地 AI 操作系统 / control plane” |
| 架构复杂度 | 中等，主干清晰，容易通读 | 高，层次多，子系统多，扩展面宽 | OpenClaw 更重、更广；<br>Hermes 更集中 |
| 系统重点 | Agent loop、procedural memory、轻量整合 | Gateway、multi-agent routing、插件生态、模型与账户编排 | 两者目标不同，不是简单的谁替代谁 |
## 2\. 宏观定位与系统边界

| 维度 | Hermes Agent | OpenClaw | Comments |
| --- | --- | --- | --- |
| 主体对象<br>\| `AIAgent`<br>是系统中心，`run_agent.py` 直接承载核心会话循环<br>\| `Gateway + OpenClaw orchestration + embedded Pi runtime`<br>共同组成主体 | Hermes 是“Agent-first”；<br>OpenClaw 是“control-plane-first” |  | 代码组织方式 |
Python 单仓，核心逻辑集中在 `run_agent.py`、`tools/`、`gateway/`、`acp_adapter/`

 | 

TypeScript/Node 大型单仓，含 `src/`、`extensions/`、`packages/`、`apps/`、`ui/`

 | 

OpenClaw 的系统边界明显更大

 |
| 

运行边界

 | 

单 Agent 为默认；subagent 是工具能力；profiles 是多实例机制

 | 

多 Agent、多 channel account、bindings、workspace、agentDir 都是一等公民

 | 

OpenClaw 原生把“多脑并存”建模进系统了

 |
| 

对外形态

 | 

CLI、messaging gateway、ACP adapter、cron、MCP client

 | 

Gateway、channels、control UI、ACP、MCP HTTP、plugins、nodes、apps

 | 

OpenClaw 的外部产品面更宽

 |

## 3\. Harness Engineering / 内核工程

| 子维度 | Hermes Agent | OpenClaw | Comments |
| --- | --- | --- | --- |
| 内核是谁<br>\| `run_agent.py`<br>里的 `AIAgent.run_conversation()` 就是内核循环<br>\| `docs/concepts/agent.md`<br>明确写出“embedded agent runtime is built on the Pi agent core”，外层由 OpenClaw 接管 session、tool wiring、delivery | OpenClaw 的内核更像“Pi runtime + 外部编排壳”；<br>Hermes 的内核更像“一体化 Agent loop” |  | 编排层职责 |
模型调用、工具循环、上下文压缩、缓存、回调、delegation 基本集中在 Agent 主干

 | 

workspace 解析、sessionKey、auth profile、模型 failover、lane queue、plugin runtime、tool/runtime 注入都在 Pi 外层编排中完成

 | 

OpenClaw 的

harness 更重、更工程化

 |
| 

失败恢复

 | 

Hermes 有上下文压缩、辅助模型、provider 适配，但整体仍偏单环路控制

 | 

OpenClaw 在 `run.ts` 中显式处理 auth profile rotation、failover、live model switch、lane enqueue、runtime plugin 初始化

 | 

OpenClaw 的“运行时调度工程”更强

 |
| 

维护成本

 | 

低到中，主链路可直接读懂

 | 

高，优点是能力面大，代价是理解成本高

 | 

小团队更容易先吃透 Hermes

 |

## 4\. IM / Message Gateway

| 子维度 | Hermes Agent | OpenClaw | Comments |
| --- | --- | --- | --- |
| Gateway 定位<br>\| `gateway/`<br>主要是消息平台适配层 + 会话转发层<br>\| `src/gateway/`<br>是完整 control plane：HTTP / WS、discovery、device auth、control UI、models HTTP、MCP HTTP、operator approvals、session persistence、cron server | OpenClaw 的 gateway 强很多，且不只是 IM 网关 |  | 平台列表<br>\| `gateway/config.py`<br>当前内置 `telegram / discord / whatsapp / slack / signal / mattermost / matrix / homeassistant / email / sms / dingtalk / webhook / feishu / wecom / api_server` |
频道与扩展面分散在 `src/gateway/`、`docs/channels/`、`extensions/`，整体明显更广，并支持多 account + bindings

 | 

Hermes 已覆盖常见平台；

OpenClaw 在广度和调度能力上更强

 |
| 

多账号与路由

 | 

Hermes 偏“一个平台适配器 + 一个 Hermes 配置”

 | 

OpenClaw 在 `docs/concepts/multi-agent.md` 中把 `bindings`、`agentId`、`accountId`、`workspace`、`agentDir` 作为一级模型

 | 

OpenClaw 更适合复杂团队和多账号运营

 |
| 

交付风格

 | 

更像聊天入口

 | 

更像本地控制总线

 | 

这是两者最直观的系统边界差异之一

 |

## 5\. Skills 系统

| 子维度 | Hermes Agent | OpenClaw | Comments |
| --- | --- | --- | --- |
| Skills 根目录<br>\| `~/.hermes/skills/`<br>是单一真相源，外部目录可读不可写 | skills 来自 `<workspace>/skills`、`<workspace>/.agents/skills`、`~/.agents/skills`、`~/.openclaw/skills`、bundled、`extraDirs`，且有明确优先级 | OpenClaw 的 skills 来源层次更复杂、更偏 workspace-first |  |
Progressive disclosure

 | 

有，`skills_list -> skill_view -> path-specific view`

 | 

也有，`docs/tools/skills.md` 明确描述 prompt 中只注入精简技能索引，并在运行时按需展开

 | 

这不是差异点，两边都有

 |
| 

Skill 目录能力

 | `SKILL.md + references/templates/scripts/assets` | 

兼容 AgentSkills，同样支持 skill folder 与 gating / installer metadata

 | 

这也不是差异点，两边都支持完整 skill 包

 |
| 

生态重心

 | 

更偏“Agent 本地可写技能库”

 | 

更偏“多来源 skills + ClawHub + installer + gating + allowlist”

 | 

OpenClaw 更强在 skills 生态与分发；

Hermes 更强在 skills 自写自修

 |
| 

安装与分发

 | 

有 Skills Hub，但生态与安装管线较轻

 | `openclaw skills install`

、`clawhub`、`skills-install.ts`、installer metadata、dangerous-code scanner 形成完整分发链

 | 

OpenClaw 在“技能平台”维度更强

 |
| 

每 Agent 隔离

 | 

Hermes 通过 `HERMES_HOME` / profile 隔离技能目录

 | 

OpenClaw 通过 workspace、agentDir、agent allowlist、shared roots 组合隔离与共享

 | 

OpenClaw 的隔离/共享策略更细粒度

 |

## 6\. Hermes 独有的 Skill 自我进化能力

| 子维度 | Hermes Agent | OpenClaw | Comments |
| --- | --- | --- | --- |
| 是否有显式写接口<br>\| `skill_manage`<br>支持 `create / edit / patch / delete / write_file / remove_file` | 本次基线下未看到等价的“Agent 显式自写自修 skill”接口；主要看到的是 install / load / gate / sync | 这是 Hermes 的强差异点 |  |
概念定位

 | `tools/skill_manager_tool.py`

直接写明 “Skills are the agent's procedural memory”

 | 

OpenClaw 文档更强调技能的来源、优先级、gating、安装与 workspace 组织

 | 

Hermes 明确把 skill 放进 agent 认知闭环

 |
| 

触发条件

 | 

官方文档写明：复杂任务成功后、踩坑后、修正后可沉淀为 skill；发现 skill 过时可 patch

 | 

OpenClaw 文档中更常见的是让用户/工作区维护 skills，而不是 agent 直接演化 skill 本身

 | 

Hermes 在“从经验到程序性记忆”的闭环上更强

 |
| 

风险控制

 | 

agent-created skills 也会跑 `skills_guard` 安全扫描

 | 

OpenClaw 主要在第三方 skill/install 时做扫描与安装保护

 | 

两边都重视安全，但切入点不同

 |
| 

最准确结论

 | 

Hermes 的优势是“skill 具有可写、可补丁、可演化的正式运行时接口”

 | 

 | 

 |

> Hermes Agent最具优势能力(看Hermes Agent工作log就是在频繁调用skill\_manage工具)：  
> 
> ![WMm8pC](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGiaOzHjaTDr87IZZpBEC9Aw1bHEibVd0ebDm5k8YSo0PClK9DvwIy613ZoCTI6JuwrjcLXuNQY8oaKqT3S76ToCIYX3wOBcAibP8A/640?wx_fmt=png&from=appmsg)

## 7\. LLM Provider / Auth

| 子维度 | Hermes Agent | OpenClaw | Comments |
| --- | --- | --- | --- |
| Provider 配置风格 | 以 `.env`、CLI setup、Python provider 适配为主<br>\| `models-config.ts`<br>+ `auth-profiles.ts` + `agent-command.ts` 组成完整模型目录与认证画像体系 | OpenClaw 的 provider/auth 工程更强 |  |
Auth 抽象

 | 

有 provider 凭证解析，够用但相对直接

 | 

有 auth profile store、profile order、cooldown、good/failure 标记、repair、OAuth/API key 双栈

 | 

OpenClaw 在认证编排上明显更成熟

 |
| 

失败恢复

 | 

Hermes 可以换 provider/model，但没有 OpenClaw 那么重的 auth profile 调度层

 | 

OpenClaw 显式支持 profile rotation、cooldown、fallback、models.json 原子更新与运行时指纹

 | 

OpenClaw 更适合复杂 provider 组合与长期运行

 |
| 

维护体验

 | 

Hermes 更简单，单人机器和快速配置更友好

 | 

OpenClaw 更强，但也更复杂

 | 

小规模使用偏 Hermes；

复杂生产路由偏 OpenClaw

 |

## 8\. Memory

| 子维度 | Hermes Agent | OpenClaw | Comments |
| --- | --- | --- | --- |
| 记忆主形态<br>\| `MEMORY.md + USER.md`<br>的 curated memory，加 `session_search` 做 FTS 会话检索 | workspace bootstrap files + `memory_search` + session transcripts + QMD / memory runtime 插件化后端 | OpenClaw 的 memory 面更大，<br>Hermes 的 memory 更贴近 prompt 内核 |  |
Prompt 注入策略

 | `memory_tool.py`

明确采用 frozen snapshot：会话开始时注入，session 内写盘但不改 system prompt，保护 prefix cache

 | 

OpenClaw 也有 bootstrap file 注入，但 memory 还外延到检索与 transcript corpus

 | 

Hermes 在“提示词稳定性”上更明确

 |
| 

检索能力

 | `session_search_tool.py`

基于 SQLite FTS5，再由辅助模型总结命中结果

 | `memory-search.ts`

支持 sources、sqlite/vector/hybrid/MMR/temporal decay、remote/local embedding provider、多模态、sync policy

 | 

OpenClaw 在 retrieval memory 维度更强

 |
| 

跨 Agent / 多 collection

 | 

Hermes 主要按 profile / session 组织，外部 memory providers 可接入

 | 

OpenClaw 在 `docs/concepts/multi-agent.md` 中已支持 per-agent transcript collection 与 cross-agent QMD memory search

 | 

OpenClaw 更偏“多脑共享或隔离的检索记忆系统”

 |
| 

最准确结论

 | 

Hermes 更像“内生化、可控、提示词友好”的记忆栈

 | 

OpenClaw 更像“检索型、可编排、面向多 agent 的记忆系统”

 | 

不能简单说谁绝对更强，只能说侧重点不同

 |

## 9\. 多 Agent / 会话编排

| 子维度 | Hermes Agent | OpenClaw | Comments |
| --- | --- | --- | --- |
| 多 Agent 是什么<br>\| `delegate_task`<br>产生受限 subagent；profiles 产生多个隔离实例；两者是两种不同机制<br>\| `docs/concepts/multi-agent.md`<br>直接把多 agent routing 作为系统一级能力 | OpenClaw 的多 Agent 模型更原生 |  | Subagent 深度 |
Hermes `delegate_tool.py` 明确限制深度与工具集，child 不能继续 delegation

 | 

OpenClaw 有 `sessions_spawn`、`sessions_yield`、`subagent-*` 整套机制，且和 session registry 绑定

 | 

OpenClaw 的子 Agent 编排更系统化

 |
| 

会话存储

 | `hermes_state.py`

SQLite + FTS5

 | 

JSONL transcripts + `~/.openclaw/agents/<agentId>/sessions` + routing/session metadata

 | 

OpenClaw 更偏 transcript-first；

Hermes 更偏 DB-first

 |
| 

Fork / resume

 | 

Hermes 在 ACP / CLI 有 session 概念，但核心还是单 Agent loop

 | 

OpenClaw 在 ACP、gateway、sessions tool、multi-agent docs 中都把 session / spawn / yield 视为核心操作对象

 | 

OpenClaw 在会话 orchestration 上更完整

 |

## 10\. ACP / MCP / 可扩展性 / 集成能力

| 子维度 | Hermes Agent | OpenClaw | Comments |
| --- | --- | --- | --- |
| ACP<br>\| `acp_adapter/server.py`<br>把 Hermes 暴露给编辑器：new/load/resume/fork/list session、tool progress、model switch、approval callback<br>\| `src/acp/`<br>是完整 ACP 子系统，含 control-plane manager、runtime cache、policy、persistent bindings、spawn、translator、server | OpenClaw 的 ACP 不只是 adapter，而是一整层控制面 |  | MCP<br>\| `tools/mcp_tool.py`<br>负责连接 stdio / HTTP MCP server，并把工具注册进 Hermes tool registry<br>\| `src/gateway/mcp-http.ts`<br>+ `src/mcp/` + loopback runtime，把 MCP 与 gateway/control plane 深度结合 |
OpenClaw 的 MCP 集成更像平台能力；

Hermes 更像 client-side tool bridge

 |
| 

插件化

 | 

Hermes 有 tools、skills、MCP servers、外部 skill dirs，但插件化边界相对收敛

 | 

OpenClaw 有 `extensions/`、`packages/plugin-sdk`、`plugins/*`、plugin package contract、provider/channel/memory 扩展

 | 

OpenClaw 的扩展能力明显更强

 |
| 

外部系统整合方式

 | 

Hermes 依赖工具/skill/MCP 的组合

 | 

OpenClaw 同时提供 extensions、plugins、gateway APIs、channels、nodes、ACP、MCP

 | 

OpenClaw 更像集成底座

 |

## 11\. Workspace / Profile / 隔离模型

| 子维度 | Hermes Agent | OpenClaw | Comments |
| --- | --- | --- | --- |
| 隔离根目录<br>\| `~/.hermes`<br>与 `~/.hermes/profiles/<name>`<br>\| `~/.openclaw/agents/<agentId>/agent`<br>+ `workspace` + `sessions` | OpenClaw 隔离对象更多，<br>Hermes 隔离路径更直观 |  | 默认工作区 |
CLI 使用当前目录，messaging 可配置 `MESSAGING_CWD`；profile 影响 `HERMES_HOME`

 | `agents.defaults.workspace`

是 agent 默认 cwd；multi-agent 时每个 agent 都有自己的 workspace

 | 

OpenClaw 的 workspace 更强绑定系统配置

 |
| 

隔离粒度

 | 

profile 级隔离明显；subagent 是临时执行隔离

 | 

agentId、workspace、auth profiles、channel binding、session store 都可单独隔离

 | 

OpenClaw 更适合多人/多脑同机共存

 |

## 12\. 工具运行时与执行面

| 子维度 | Hermes Agent | OpenClaw | Comments |
| --- | --- | --- | --- |
| 工具注册 | Python registry 模式，`tools/*.py` 在导入时 `register()` | 工具 catalog + runtime wiring + plugin/extensions 注入 | Hermes 简洁；<br>OpenClaw 灵活但复杂 |
| 执行沙箱 | Hermes 有 `tools/environments/`，支持 local/docker/ssh/modal/daytona/singularity 等 | OpenClaw docs 与代码里对 sandbox、workspace override、nodes、gateway sandboxing 讨论更深入 | OpenClaw 的运行面更宽 |
| 浏览器 / Web / Canvas / 节点 | Hermes 有 browser、web、vision、image-generation、tts 等工具 | OpenClaw 除 browser/web 外，还把 canvas、nodes、设备节点、control UI 等整合进统一平台 | OpenClaw 更偏“能力平台” |
##   

## 13\. 适用场景判断

| 场景 | 更适合 Hermes Agent | 更适合 OpenClaw |
| --- | --- | --- |
| 想要一个会随着使用逐步沉淀技能的方法型 Agent | 是 | 否 |
| 想把 Agent 当作“长期协作的工作搭子”持续养熟 | 是 | 可做，但不是最鲜明优势 |
| 想运营多个 agent、多个 channel account、多个 workspace | 一般 | 是 |
| 想构建本地 control plane，把消息平台、插件、ACP、MCP、sessions 都纳进一个大系统 | 一般 | 是 |
| 想快速 hack 一个核心 Agent、阅读主循环、直接改行为 | 是 | 较难 |
| 想要强 skills 生态、安装和分发能力 | 一般 | 是 |
| 想做“技能即 procedural memory，且 agent 能自行 patch” | 是 | 否 |
##   

* * *

# 二、Hermes Agent究竟有什么优势

上面的表格已经从客观角度做出了非常详尽的比较，以下是我的主观评价：

1.  1\. 从员工沟通和管理角度：Hermes Agent将所有的工作过程（log）都在聊天界面中打印出来了，工作的“透明度”带来了”可信度“，职场老油条们应该都明白这个道理。  
    
    ![Uvb1zy](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGiaaibQEuIrgERe5kNXa8TR8YKmGqfzBO3Rwqag6icibQShnYY0rXgiafpaGLPliaKCC3Vy1GAdzTM5we95sjiaL3sn8ENmjESUhSIHzs/640?wx_fmt=png&from=appmsg)
    
2.  2\. 从员工“Growth Mindset”角度：凡是摔过的坑，Hermes大概率不会再犯，因为Hermes的工作过程就是不断的调整和优化它自己的工作流（其实也是我的工作流），然后用调整过的工作流去跑业务流程，有问题就再调整，如此循环，直到最终的业务结果通过验收，那么最后一版的工作流大概率就是最终需要被沉淀下来的knowhow，你会得到自己都忘了应该进行封装但Hermes已经帮你封装好的若干个新skills，以及一路优化下来的N多旧skills -- 妥妥以“Bayesian Inference” 为底层运行机制的Agent。
    
3.  3\. 从员工无监管自动运行角度：Hermes Agent的长程无监管运行能力也比较强；我用GPT-5.4跑过2小时以上的Hermes Agent任务，这个时长放在OpenClaw身上我还没有成功过...
    
4.  4\. 在上面的表格中我们可以看到OpenClaw的优势在于摊子铺的更大，更“平台化”；但问题是，如果在非常具体的场景中没办法很好沉淀个人或者组织的knowhow的话，摊子又铺那么大，放大的究竟是优势还是劣势呢？
    
5.  5\. 总之，“白马”（未经过调教的Hermes）一定是比“白虾”（未经过调教的OpenClaw）更值得信赖和培养的好员工。
    

* * *

# 三、Hermes Agent发展趋势

Hermes Agent项目发布于2月26日，在Github上有接近3.5万颗星。  

![R82MAR](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGg3eZCrXyolGyzUc5NzKrkxJoV8WbQ5zT3wp0n9Tflx0ZHWyugpET7f3mVNZtv2A2VYiaibf3iboBibU6z42UAHsicJMRYTCEclxZIs/640?wx_fmt=png&from=appmsg)

在OpenRouter的应用token消耗日榜上，Hermes Agent同时“Top Coding Agent榜”和“Top Productivity”两张榜上。  
在Coding Agent区，Hermes Agent在本周超越了老牌Coding Agent “Cline”，排在Coding Agent榜单第三名，并且用量还在快速上升，离去年的当红炸子鸡Kilo Code一步之遥，大概率会在未来一周超越Kilo Code，2-3周超越Claude Code。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGjFkrvn4DdHPDqQ4F3Dh3bJtJQtYgG48B4fcEAsDV1IotGoxhSz1XBzEPwPjhdpgoCdnYxLasJFoKVrricQDibOypfbniadk26o4g/640?wx_fmt=png&from=appmsg)

在Productivity区，目前Hermes的token消耗量约为OpenClaw的1/4左右，而这个值在上周在1/8左右。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGjWkwFwsMbMXFkdaicuCg8QcAJXNNZNxnKMHGEoYSnHkr4KFibOg1I11wFFKnaEukLmQ1An29rh0poBUxB8h2Dd1sa6jUwEJB3cQ/640?wx_fmt=png&from=appmsg)

也就是说，1个月后，从token消耗量角度观察，就是OpenClaw和Hermes Agent两强争霸的局面。

这也就是为什么最近有越来越多的人在谈论Hermes Agent... 趋势已经飙起来了，数据不会撒谎。

# 四、文档资源：

> 其实你只需要看下面两个文档站，或者把文档站喂给你手边的一个Agent，然后问它，就能得到几乎所有问题的答案了 ...

官方文档站： https://hermes-agent.nousresearch.com/docs/  
我上周复刻为中文文档站（随官方日更）： https://hermes-doc.aigc.green/

另外，可以关注Hermes Agent的官推：

@Teknium： https://x.com/Teknium  （Hermes创始人，NOUS Research Cofounder和模型后训练负责人）  
@NousResearch： https://x.com/NousResearch （Hermes Agent官方团队）

> NOUS Research团队的迭代能力也堪称光速，昨天就已经把火爆的Karpathy的LLM Wiki能力集成到Hermes里了；  
> 
> ![Gy0ObY](https://mmbiz.qpic.cn/sz_mmbiz_png/0m9F5vC1OGiadqfDKYbicDVjQrEbpD13JicQibv9AzL71NQTT4Uc3bgWN3yoVmZc6TLhCTXZcXCzIq7kR0NWBOJTibtqak3yfuhxFiaEwGCrlia5j4/640?wx_fmt=png&from=appmsg)

# 五、社群资源

我在上周创建的“Hermes Agent中文社区”飞书群目前已有2000多位同学加入并已经沉淀了不少不错的资源，欢迎更多同学onboard 

![L4IX7g](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGhXTzBdicgB8vs7hur0qFcGAVdVDy7bn4biaINy7tft6tjyBTq9B1AIyCYVLp0miaicfKy9fGmevKKAvLKAyDjmz9heib4HH1LiaSUiag/640?wx_fmt=png&from=appmsg)