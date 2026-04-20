---
title: "什么才是真正的 Harness Engineering？"
source: "https://x.com/SaitoWu/status/2045458721929892345"
author:
  - "[[@SaitoWu]]"
published: 2026-04-18
created: 2026-04-20
description: "刚刷完 OpenAI Ryan 在伦敦的演讲 + 访谈，干货直接爆棚。他一句话把 Harness Engineering 的核心说穿了：代码已经免费了（code is free），实施不再是瓶颈，人类真正的价值是“steering”（指导）— 定义什么是好代码、注入 guardr..."
tags:
  - "clippings"
---
![图像](https://pbs.twimg.com/media/HGLtGT-aEAA9t0h?format=jpg&name=large)

刚刷完 OpenAI Ryan 在伦敦的演讲 + 访谈，干货直接爆棚。

他一句话把 Harness Engineering 的核心说穿了：代码已经免费了（code is free），实施不再是瓶颈，人类真正的价值是“steering”（指导）— 定义什么是好代码、注入 guardrails、让 agent 自己去执行。

以前我们自己敲键盘，现在 agent 写 99% 的代码，我们只管 orchestration（编排）。来，拆解他最硬核的几点观点

**代码免费，但上下文和 guardrails 永远稀缺**

Ryan 说：模型已经够强了，能像人类一样写完整代码。

真正稀缺的是人类时间、注意力和模型上下文窗口。

所以 Harness 的本质就是：把人类经验（taste、review 标准、非功能要求）全部写成文本（docs、skills、ADRs、logs），让 agent 随时能看到“什么叫好代码”。

**别再把 agent 关在小盒子里，要给它完整工具和权限**

传统做法是给 agent 预设好 scaffold（脚手架），限制它一步步走。

Ryan 的做法完全相反：让 agent 自己成为整个 box，给它 CLI、bash、observability stack、甚至自己 spin up 服务的能力。

这样 agent 就能像全栈工程师一样，从头到尾把活干完，人类只需偶尔 review。

**人类角色彻底升级：从 implementer 变成 orchestrator**

以前工程师是“写代码的人”，现在是“staff engineer 带 5000 个 agent 的团队 leader”。

你的工作不再是敲代码，而是： 定义优先级和 success criteria

观察 agent 哪里反复出错

把这些错误转化成 durable guardrails（lints、tests、review agents）

不断把人类时间解放到更高杠杆的事上

**Skills + progressive disclosure 是神器**

Ryan 超级推 skills：只把「名字 + 描述」塞进上下文（几十 tokens），需要时才加载完整内容。

这样既省 token，又让 agent 更聪明。

他团队只用 5-10 个核心 skills，但不断打磨，让 agent 像老员工一样懂团队 taste。

**Review 也要 agent 化，人类只看 post-merge**

PR 不再需要人类同步 review。

他们用 review agents 自动检查代码（看 docs、guardrails、QA plan）。

人类只在最终 merge 前抽样看，或者 post-merge 再 review。

这样 agent 能 24/7 并行工作，人类不用一直卡在 review 瓶颈。

**让代码库本身变得 agent-friendly 所有东西尽量相同（one way to do X）**

构建时间压到 1 分钟内

文件结构清晰、package 隔离、observability 内置

用 tests 和 lints 做 source code verification（验证代码结构本身）

这样 agent 无论看哪里，都能快速理解、少犯错。

**一句话总结 Ryan 的核心观点：**

Harness Engineering 不是让 agent 帮你写代码，而是让你彻底从执行层解放出来，只做 steering 和 orchestration。

代码免费了，prompt 和 guardrails 才是王道。

把团队的 taste、标准、历史经验全部写成文本喂给 agent，你就拥有了一支 24/7 永不疲倦、永远在进步的 5000 人工程团队。

**更多硬核科技播客内容：**[Podwise](https://podwise.ai/dashboard/episodes/7787884)