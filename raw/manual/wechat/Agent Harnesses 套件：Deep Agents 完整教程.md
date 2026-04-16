---
title: "Agent Harnesses 套件：Deep Agents 完整教程"
source: "https://mp.weixin.qq.com/s/GxnEgZekFq4OR48KNUdRSQ"
author:
published:
created: 2026-04-16
description:
tags:
  - "clippings"
---
*2026年4月16日 16:55*

在 AI 圈子混，你可能已经听过无数次“Agent（智能体）”这个词。但现状是：大多数开发者还在写简单的 Prompt 轮询，或者在复杂的框架配置中挣扎。

今天我们要聊的是 **Deep Agents** —— 这是由 LangChain 团队推出的“智能体内核（Agent Harness）”。它不仅仅是一个库，更像是一个给 LLM 穿上的“外骨骼”，让你的 AI 能够像资深工程师一样 **规划、使用文件系统、甚至召唤子智能体** 。

## 什么是 Deep Agents？

> https://docs.langchain.com/oss/python/deepagents/overview

简单来说，如果你把 **LangChain** 看作零件库，把 **LangGraph** 看作生产线，那么 **Deep Agents** 就是一台已经组装好的、高性能的“智能机器人”。

它是一个建立在 LangGraph 之上的独立库，专为解决复杂、多步骤的任务而设计。它的核心优势在于： **内置了大量“开箱即用”的高级能力** ，你不需要从零开始编写复杂的循环逻辑。

### 核心“超能力”一览：

- **任务拆解（Planning）** ：内置 `write_todos` 工具，AI 会先写计划再动手。
- **虚拟文件系统** ：支持 `ls` 、 `read_file` 、 `edit_file` 。这意味着 AI 可以处理超出 Context Window 的超大文件，或者在本地/云端持久化存储数据。
- **子智能体生成** ：主 Agent 觉得任务太累？它可以直接派生出一个专门负责细分任务的“子 Agent”。
- **沙箱执行（Sandbox）** ：配合 Modal 或 Daytona，AI 可以在隔离环境中跑 Shell 命令、执行 Python 代码。
- **人类在干预（Human-in-the-loop）** ：对于删除文件等高危操作，可以设置必须经过人工点击确认。

Deep Agents 最大的魅力在于其 **供应商无关性** 。无论你偏爱 Google Gemini、OpenAI 还是本地的 Ollama，写法几乎完全一致。

```
# pip install -qU deepagents langchain-google-genai
from deepagents import create_deep_agent

# 1. 定义一个简单的工具
def get_weather(city: str) -> str:
    """获取指定城市的实时天气。"""
    returnf"{city} 的天气总是晴空万里！"

# 2. 创建智能体
agent = create_deep_agent(
    model="google_genai:gemini-3.1-pro-preview",
    tools=[get_weather],
    system_prompt="你是一个既聪明又有礼貌的深度助手。",
)

# 3. 运行！
agent.invoke(
    {"messages": [{"role": "user", "content": "旧金山天气怎么样？"}]}
)
```

普通的 Agent 往往在对话几轮后就会“断片”或者陷入死循环。Deep Agents 通过以下机制解决了这些痛点：

### 1\. 智能上下文管理

当对话变得太长时，Deep Agents 会通过 **自动总结（Auto-summarization）** 压缩旧消息。同时，它利用文件系统作为“外部大脑”，把不常用的信息存入文件，而不是塞进宝贵的上下文窗口里。

### 2\. 权限隔离与安全

你可以为 Agent 声明严格的权限规则：

> “你可以读取 `/src` 目录，但严禁修改根目录下的任何文件。” 这种声明式的权限控制，让开发者在调用强大工具（如 Shell）时能睡个安稳觉。

### 3\. 可拔插的后端（Backends）

你可以根据需求随意更换文件系统的存放位置：

- **In-memory** ：适合快速测试。
- **Local disk** ：适合本地开发工具。
- **LangGraph Store** ：实现跨会话、长期的“记忆”。

### 什么时候该选 Deep Agents？

并不是所有场景都需要这尊大佛。

- ✅ **推荐使用** ：你需要构建一个编码助手（CLI）、一个需要长时间运行的自动化调研员、或者一个需要处理大量本地文档的工具。
- ❌ **不推荐使用** ：如果你只是想做一个简单的问答机器人，直接用 LangChain 的 `create_agent` 或者基础的 LLM 调用会更轻量。

## 进阶实践：构建你的第一个“科研专家”智能体

> https://docs.langchain.com/oss/python/deepagents/quickstart

### 1\. 环境准备：给智能体装上“眼睛”

智能体需要工具才能与世界交互。这里我们选用 **Tavily** 作为搜索引擎，它专门为 AI 优化，返回的内容更适合模型阅读。

**安装核心库：**

```
pip install deepagents tavily-python
```

**配置 API 密钥：** 你需要设置模型提供商（如 Gemini）和 Tavily 的 Key。

```
export GOOGLE_API_KEY="你的Key"
export TAVILY_API_KEY="你的Tavily_Key"
```

### 2\. 定义搜索工具

我们定义一个简单的 Python 函数。Deep Agents 会通过函数签名（Type

Hints

）和文档字符串（Docstring）自动理解这个工具的用途。

```
import os
from tavily import TavilyClient
from deepagents import create_deep_agent

tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

def internet_search(query: str):
    """在互联网上搜索信息，获取最新资讯。"""
    return tavily_client.search(query, max_results=5)
```

### 3\. 初始化“深度智能体” (Deep Agent)

关键的一步来了。我们将模型、工具和一段“人设”注入 `create_deep_agent` 。

```
research_instructions = """你是一名资深研究员。
你的任务是进行深入调研并撰写专业报告。
你可以使用 internet_search 工具来收集信息。
"""

agent = create_deep_agent(
    model="google_genai:gemini-1.5-pro", # 或者使用 openai:gpt-4o 等
    tools=[internet_search],
    system_prompt=research_instructions,
)
```

### 4\. 见证奇迹：运行与自动化流程

当你调用 `agent.invoke` 时，后台发生的不仅仅是一次对话。

```
result = agent.invoke({"messages": [{"role": "user", "content": "请分析下 2024 年大语言模型的技术趋势。"}]})
print(result["messages"][-1].content)
```

普通的 Agent 可能只是搜一下就回答了，但 **Deep Agent** 会自动执行以下高级逻辑：

1. **自主规划 (Planning)** ： 它不会直接搜索。它会先调用内置的 `write_todos` 工具，给自己列个提纲： *“1. 搜索长文本技术；2. 调研多模态进展；3. 总结归纳。”*
2. **上下文管理 (Context Management)** ： 如果搜索结果太长（比如搜到了 10 篇论文），它会自动调用 `write_file` 把内容暂存到“虚拟磁盘”，避免撑爆 LLM 的上下文窗口。
3. **子任务分发 (Subagents)** ： 如果任务太重，主 Agent 甚至会生成一个“子 Agent”专门负责整理数据，自己则负责最后的报告润色。
4. **实时流式输出 (Streaming)** ： 通过 LangGraph 底层支持，你可以看到它每一步的思考过程，而不是干等着结果。

## 深度定制：打造你的专属 AI 智能体

> https://docs.langchain.com/oss/python/deepagents/customization

如果说 Quickstart 是让你跑通流程，那么 **Customization** 就是教你如何给智能体装上“大脑”、“肌肉”和“记忆”。

### 1\. 核心配置概览

`create_deep_agent` 函数提供了丰富的参数。你可以把它想象成一个“智能体工厂”，通过不同的配置，你可以生产出擅长不同领域的智能体。

### 2\. 模型选择：灵活切换“大脑”

Deep Agents 支持几乎所有主流 LLM。你可以使用简单的 `provider:model` 字符串快速切换：

- **OpenAI**: `openai:gpt-5.4`
- **Anthropic**: `anthropic:claude-sonnet-4-6`
- **Google**: `google_genai:gemini-3.1-pro-preview`

> **专业提示** ：对于长任务，建议在初始化模型时增加 `max_retries` （如设为 10-15），并配合 `timeout` 设置，以应对网络抖动。

### 3\. 中间件 (Middleware)：智能体的“插件系统”

中间件是 Deep Agents 的灵魂。它在智能体运行的各个环节（执行前、执行后、工具调用时）注入逻辑。

**默认开启的神级功能：**

- **TodoListMiddleware** ：让 AI 像人类一样维护待办清单。
- **SummarizationMiddleware** ：当对话太长时，自动总结历史，防止“失忆”和 Token 溢出。
- **PatchToolCallsMiddleware** ：自动修复中断的工具调用，增强系统的稳定性。

### 4\. 后端与沙箱：给 AI 一个“操作空间”

AI 不能只在对话框里聊天，它需要一个地方存文件、跑代码。

### 常见的虚拟文件系统（Backends）：

| 后端类型 | 存储位置 | 特点 |
| --- | --- | --- |
| **StateBackend** | 内存 (LangGraph State) | **单线程隔离**  ，运行完即销毁。 |
| **StoreBackend** | 数据库/持久化存储 | **跨线程记忆**  ，AI 下次登录还能看到之前存的文件。 |
| **CompositeBackend** | 混合存储 | 灵活路由：比如 `/tmp` 用内存， `/user_data` 用数据库。 |

### 隔离沙箱 (Sandboxes)

如果你想让 AI 运行 `pip install` 或执行 Shell 命令， **千万不要在本地跑！** 使用 **Modal** 、 **Daytona** 或 **Runloop** 提供的沙箱后端。这就像给 AI 准备了一个一次性的“隔离实验室”，即便它写了 Bug 或恶意代码，也不会伤及你的主机。

### 5\. 进阶：人类在干预 (Human-in-the-loop)

在处理支付、删除数据等敏感操作时，你可以配置 `interrupt_on` 。智能体会运行到这一步时 **自动挂起** ，等待你在后台点击“允许”后才继续执行。

## LangChain Deep Agents、Claude Agent SDK 和 Codex SDK 的概览对比

> https://docs.langchain.com/oss/python/deepagents/comparison

### 1\. 核心选择逻辑：场景驱动

- **如果你需要构建一个“通用型”且“生产就绪”的 Agent：** **LangChain Deep Agents** 是首选。它最大的优势在于 **模型无关性** （Model-agnostic）和 **部署能力的完整性** 。如果你不希望被绑定在单一供应商（如 Anthropic 或 OpenAI），或者需要处理复杂的生产环境问题（如多租户隔离、RBAC 权限控制、长短期记忆管理），Deep Agents 提供了最成熟的脚手架。
- **如果你专注于“AI 编程辅助”且追求极致的模型调优：**
- **Claude Agent SDK：** 适合深度集成 Claude 系列模型（如 Claude 3.5/4）。它与 Claude Code 紧密结合，在处理代码编写、Bash 执行等任务上有着非常丝滑的体验。
	- **Codex SDK：** 如果你的技术栈完全建立在 OpenAI 生态之上，Codex SDK 提供了诸如“OS 级沙箱模式”（如 `read-only` ）和内置的 Git 检查点功能，非常适合需要严格系统安全约束的编程场景。

### 2\. 技术特性深度对比

#### 环境与安全（Sandboxing）

- **Deep Agents** 允许你将“沙箱”作为一种 **工具** 来调用（Sandbox-as-tool），这意味着 Agent 可以根据需要在不同的隔离环境中运行特定操作，而不仅仅是自身运行在沙箱里。
- **Codex SDK** 在操作系统层面的权限控制上最为细腻，提供了明确的 `workspace-write` 和 `danger-full-access` 模式，适合对本地文件安全极其敏感的开发者。

#### 记忆与状态管理（State & Memory）

- **Deep Agents** 拥有完整的 **Memory Store** 系统，支持长期记忆。
- **Claude & Codex** 更多依赖于文件系统（如 `CLAUDE.md` 或 `AGENTS.md` ）或会话恢复（Session Resume），在跨会话的“知识沉淀”上，Deep Agents 的结构化存储能力更强。

#### 可观测性（Observability）

- **Deep Agents** 深度集成了 **LangSmith** ，这在生产环境中是巨大的优势。你可以轻松进行追踪（Tracing）、评估（Evaluation）和 A/B 测试。
- **Claude SDK** 目前在原生追踪和评估上相对较弱，通常需要开发者自行构建 HTTP/WebSocket 层来捕获状态。

## Deep Agents 本地部署

> https://docs.langchain.com/oss/python/deepagents/deploy

现在我们进入了实操层面。 `deepagents deploy` 是将你的 Agent 从本地原型转化为 **生产级服务** 的关键工具。它不仅仅是代码部署，更是为你构建了一套包含多租户、持久化记忆和安全沙箱的完整基础设施。

以下是根据文档总结的部署核心逻辑与实战建议：

### 1\. 部署架构：从代码到服务

当你运行 `deepagents deploy` 时，系统会自动完成以下转换：

- **多协议支持** ：部署后，你的 Agent 会自动暴露 30 多个端点，包括标准的 **Agent Protocol** （用于前端 UI）、 **MCP** （让其他 Agent 调用你）以及 **A2A** （用于 Agent 间的协作）。
- **模型与沙箱解耦** ：你可以在 `deepagents.toml` 中随意更换模型（如从 `claude-3-5-sonnet` 切换到 `gemini-1.5-pro` ），而无需修改核心逻辑。

---

### 2\. 核心配置文件：deepagents.toml

这是你的部署蓝图。以下是一个典型的配置示例，它结合了高性能模型与安全的代码执行环境：

```
[agent]
name = "my-expert-agent"
model = "anthropic:claude-3-5-sonnet-latest" # 也可以是 google_genai, openai 等

[sandbox]
provider = "langsmith"  # 使用 LangSmith 托管的沙箱
image = "python:3.12"   # 运行环境
scope = "thread"        # 每个对话独立沙箱，确保安全隔离
```

### 3\. 两种记忆模式：静态 vs 动态

这是 Deep Agents 的一大特色，它区分了“开发者定义的指令”和“用户个人的偏好”：

| 记忆类型 | 文件路径 | 读写属性 | 作用 |
| --- | --- | --- | --- |
| **系统指令** | `/AGENTS.md` | **只读** | 定义 Agent 的人格、任务目标和全局规范。 |
| **用户偏好** | `/user/AGENTS.md` | **可写** | **每个用户专属**  。Agent 可以通过 `edit_file` 记录用户的喜好，实现跨会话的个性化。 |

### 4\. 关键限制（必看）

在生产环境中，为了安全和性能，有几个重要的“坑”需要避开：

- **MCP 传输协议** ：部署环境不支持 `stdio` （本地进程）。如果你使用了本地的 MCP 服务器，必须先将其转换为 **HTTP** 或 **SSE** 协议。
- **工具逻辑** ：部署后无法运行自定义的 Python 脚本作为工具。如果你有复杂的业务逻辑，建议将其封装成一个独立的 **MCP Server** 。

## Deep Agents 从原型到生产

> https://docs.langchain.com/oss/python/deepagents/going-to-production

如果你已经完成了本地开发，准备将你的 Agent 部署到生产环境，那么本节内容是 **至关重要** 的。从原型到生产（Production）的跨越，本质上是解决 **安全性（Security）** 、 **隔离性（Isolation）** 和 **持久性（Persistence）** 的过程。

### 1\. 生产环境的三大基石

在生产中，你需要管理三种不同的“边界”来确保数据不串流：

- **Thread（线程）** ：单次对话。消息历史和临时文件默认只在这一层，不跨线程。
- **User（用户）** ：互动的个体。 **记忆（Memory）** 通常在这一层实现持久化，确保“用户 A”的偏好不会被“用户 B”看到。
- **Assistant（助手）** ：你部署的 Agent 实例。你可以为所有用户设定统一的全局指令（如：品牌准则）。

### 2\. 深度定制记忆：CompositeBackend

为了让 Agent 既能快速读写临时文件，又能记住长期的用户偏好，生产环境通常采用 **复合后端** ：

```
agent = create_deep_agent(
    model="google_genai:gemini-1.5-pro",
    backend=CompositeBackend(
        default=StateBackend(), # 默认路径：临时草稿，对话结束即销毁
        routes={
            "/memories/": StoreBackend( # 路由路径：永久存储到数据库
                namespace=lambda rt: (
                    rt.server_info.assistant_id, 
                    rt.server_info.user.identity # 按用户 ID 隔离
                ),
            ),
        },
    ),
    system_prompt="你的长期记忆存放在 /memories/ 目录下。"
)
```

### 3\. 沙箱生命周期：Thread vs Assistant

当你的 Agent 需要执行代码或安装工具（Skill）时，必须在沙箱（Sandbox）中运行。你需要决定沙箱的存活时间：

- **Thread-scoped（线程级）** ：
- *场景* ：数据分析。每个新对话都给一个干净的容器，对话结束即销毁。
	- *优点* ：极度安全，不会受之前操作的影响。
- **Assistant-scoped（助手级）** ：
- *场景* ：代码开发助手。它需要跨对话保留克隆的 GitHub 仓库或已安装的复杂环境。
	- *优点* ：效率高，无需重复进行初始化设置。

### 4\. 生产级安全：OAuth 与 凭证注入

在生产中，Agent 绝对不能硬编码 API Key。

- **OAuth 流程** ：如果 Agent 需要操作用户的 GitHub，它会触发一个“中断（Interrupt）”，给用户发送一个授权链接。用户点击授权后，Agent 自动获得 Token 并继续工作。
- **沙箱认证代理（Auth Proxy）** ：这是一种高级安全机制，Agent 在沙箱里发出的请求会被透明地注入凭证，但 **Agent 自身的代码永远看不到这些原始密钥** 。

### 5\. 韧性与可靠性（Durability）

Deep Agents 基于 LangGraph 构建，天生具备“ **可暂停/可恢复** ”的能力：

- **故障自动恢复** ：如果服务器在中途宕机，Agent 会在下次启动时从最后一个 Checkpoint（检查点）自动恢复，而不需要从头开始消耗 Token。
- **人机协作（Human-in-the-loop）** ：对于敏感操作（如：向客户发邮件），你可以设置 Agent 在此步骤暂停，等待你在管理后台手动点击“批准”后再继续。

## Deep Agents 与 Agent Harness

这部分文档详细介绍了 **Agent Harness（助手装甲/外壳）** ，这是 Deep Agents 的核心。如果说 LLM 是大脑，那么 Harness 就是它的 **感官、肢体和工具箱** 。它让 Agent 能够超越简单的对话，真正具备在复杂环境中生存和工作的能力。

### 1\. 虚拟文件系统（Virtual Filesystem）—— 核心交互窗口

Agent 并不是直接操作你的硬盘，而是通过一个 **虚拟层** 进行交互。这个虚拟层不仅支持传统的文本读写，还具备 **多模态感知** 能力：

- **结构化操作** ：支持 `ls`, `read_file`, `edit_file`, `grep` 等 Linux 风格的工具。
- **多模态读取** ：当 Agent 调用 `read_file` 读取 `.pdf`, `.png` 或 `.mp4` 时，Harness 会自动将其转化为模型可理解的多模态消息块。
- **精密修改** ： `edit_file` 支持精确的字符串替换，避免模型重写整个大文件时产生的随机错误。

### 2\. 任务委派（Task Delegation）—— 多智能体协作

这是解决复杂任务的杀手锏。主 Agent 可以像项目经理一样，调用 `task` 工具创建一个 **子智能体（Subagent）** ：

- **上下文隔离** ：子智能体在独立的空间工作，它的中间过程（琐碎的尝试和错误）不会污染主 Agent 的对话历史。
- **结果压缩** ：主 Agent 只接收子智能体提交的最终报告，极大地节省了 Token。
- **并发处理** ：你可以同时派出“代码审计员”和“文档编写员”子智能体。

### 3\. 安全与权限（Permissions & Sandboxes）

在生产环境中，赋予 Agent 动力必须伴随着约束：

- **声明式权限** ：你可以通过 `permissions` 列表，明确禁止 Agent 访问特定敏感路径（如 `.env` 或 `/etc/` ），采用“首条匹配原则”。
- **代码执行沙箱** ：当使用 `Daytona` 或 `Modal` 等后端时，Agent 获得 `execute` 工具。这允许它在隔离的容器内运行 `pip install` 或执行 Python 脚本，即使 Agent 运行了恶意代码，也无法伤害到你的宿主服务器。

### 4\. 动态上下文管理（Context Engineering）

Deep Agents 不会因为对话变长而崩溃，Harness 扮演了“记忆过滤器”的角色：

- **技能（Skills）的按需加载** ：与普通的 System Prompt 不同，技能采用 **延迟加载** 。Agent 只在需要时才读取完整的 `SKILL.md` ，平时只保留索引，显著降低了常驻 Token 消耗。
- **自动压缩** ：当对话接近 Context Window 上限时，Harness 会自动触发摘要逻辑。

### 5\. 人机协作（Human-in-the-loop）

你可以为任何高风险工具配置“审批拦截”。例如：

```
interrupt_on={"edit_file": True} # Agent 在修改代码前必须征得你的同意
```

这让 Agent 变成了一个 **受控的增强工具** ，而不是失控的黑盒。

## Deep Agents 与 模型

> https://docs.langchain.com/oss/python/deepagents/models

这部分文档介绍了 Deep Agents 的“大脑”—— **模型（Models）** 。与普通的 Chat 机器人不同，Deep Agents 对模型的要求极高，它们必须支持 **工具调用（Tool Calling）** 。

以下是文档中关于模型配置与选型的重要知识点：

### 1\. 核心选型准则

Deep Agents 兼容任何支持工具调用的 LangChain 聊天模型。文档推荐了在官方评测集（Eval Suite）中表现优异的模型，这些模型能更稳定地处理复杂的 Agent 循环：

- **Google**: `gemini-3.1-pro-preview` (特别推荐，支持强大的推理与长上下文)
- **OpenAI**: `gpt-5.4`, `gpt-4o`
- **Anthropic**: `claude-sonnet-4-6`
- **开源权重模型**: `GLM-5`, `Qwen-3.5` (可通过 Ollama 或 vLLM 接入)

### 2\. 两种配置方式

你可以根据需要的控制粒度选择配置方法：

- **快捷字符串** ：适用于简单场景，格式为 `provider:model`
	```
	agent = create_deep_agent(model="google_genai:gemini-3.1-pro-preview")
	```
- **实例对象** ：当你需要精细控制参数（如 `thinking_level` 或 `temperature` ）时，先用 `init_chat_model` 初始化。
	```
	model = init_chat_model("google_genai:gemini-3.1-pro-preview", thinking_level="medium")
	agent = create_deep_agent(model=model)
	```

### 3\. 高级黑科技：运行时动态切换模型

在生产环境中，你可能希望根据用户的选择（例如下拉列表）或任务的复杂度（简单任务用 Flash，复杂任务用 Pro）来切换模型。文档提供了一个优雅的 **Middleware（中间件）** 方案：

通过 `@wrap_model_call` 装饰器，你可以在不重新构建整个 Agent 图的情况下，根据传入的 `context` 动态拦截并替换模型请求。

## Deep Agents 与 上下文工程

https://docs.langchain.com/oss/python/deepagents/context-engineering

这部分文档是关于 **上下文工程（Context Engineering）** 的深度指南。对于构建长程（Long-running）任务的 Agent 来说，上下文管理直接决定了它的“智力”是否能持续在线。

以下是文档中关于如何控制 Agent 上下文的核心机制：

### 1\. 自动上下文压缩：拒绝“爆 Token”

Deep Agents 内置了两套自动防御机制，防止对话历史超过 LLM 的上下文窗口：

- **内容卸载（Offloading）** ：
- **触发条件** ：当工具调用的输入或输出超过 **20,000 Token** 时。
	- **动作** ：Harness 会自动将大段内容存入文件系统，并在对话历史中将其替换为一个“引用指针”（例如： `[结果已存至 /tmp/data.txt，前10行预览如下...]` ）。Agent 需要详细信息时，可以通过 `read_file` 自行读取。
- **智能摘要（Summarization）** ：
- **触发条件** ：当上下文占用达到模型限制的 **85%** 且无法进一步卸载时。
	- **动作** ：LLM 会生成一个包含“任务意图、已产出工件、下一步计划”的结构化总结，替代掉中间冗长的对话细节，同时将原始记录备份到文件系统中以供追溯。

### 2\. 渐进式披露：技能（Skills） vs. 记忆（Memory）

为了平衡“知识丰富度”和“Token 成本”，上下文被分为两类加载模式：

- **记忆（Memory/AGENTS.md）** ： **始终加载** 。用于存放必须时刻遵守的准则（如：代码规范、用户姓名）。
- **技能（Skills/SKILL.md）** ： **按需加载** 。Agent 在启动时只读取技能的摘要（Frontmatter），只有当它判定当前任务需要该技能时，才会加载完整内容。

### 3\. 上下文隔离：利用子智能体（Subagents）

这是处理“重型任务”的最佳实践。如果主 Agent 需要进行大量的网页搜索或处理复杂的数据库查询，这些中间过程会迅速填满上下文。

- **逻辑** ：主 Agent 派出一个子智能体去处理琐碎过程。
- **结果** ：主 Agent 的上下文保持干净，只接收子智能体返回的一份“精简结论”。

### 4\. 运行时上下文（Runtime Context）

这部分数据不直接进入 System Prompt，而是作为“隐藏背景”存在。

- **用途** ：存放 API Keys、用户 ID、数据库连接字符串等。
- **传递** ：运行时上下文会自动 **透传** 给所有子智能体，确保整个任务链条都能访问必要的凭证。

## Deep Agents 与 后端

> https://docs.langchain.com/oss/python/deepagents/backends

### 1\. 常见的内置后端类型

根据你的应用场景（是本地开发还是生产环境），你可以选择不同的后端：

- **StateBackend (默认/临时)** ：
- **特点** ：文件存储在内存状态中，仅在当前对话线程（Thread）内有效。
	- **场景** ：Agent 的临时“草稿本”，处理大型输出时的缓冲区。
- **FilesystemBackend (本地磁盘)** ：
- **特点** ：读写你电脑上的真实文件。 **注意安全** ，建议开启 `virtual_mode=True` 。
	- **场景** ：你目前正在构建的 **"Learn Claude Code"** 等本地开发辅助工具。
- **StoreBackend (持久化存储)** ：
- **特点** ：跨线程持久化。即使用户关掉窗口下次再来，Agent 依然记得 `/memories/` 下的文件。
	- **场景** ：存储用户的偏好设置、长期任务的进度。
- **Sandbox (沙箱后端)** ：
- **特点** ：在 Modal 或 Daytona 等隔离容器中执行。提供 `execute` 工具。
	- **场景** ：需要 Agent 运行不可信代码或复杂的 Shell 指令。

### 2\. 路由机制：CompositeBackend (复合后端)

这是最强大的配置方式，允许你通过 **路径路由** 将不同的后端组合在一起：

```
backend = CompositeBackend(
    default=StateBackend(),       # 默认文件都是临时的
    routes={
        "/memories/": StoreBackend(), # 只有 /memories/ 下的文件会永久保存
        "/logs/": FilesystemBackend(root_dir="./logs") # 日志写到本地磁盘
    }
)
```

### 3\. 数据隔离：命名空间工厂 (Namespace Factories)

在多用户生产环境下，你肯定不希望用户 A 读到用户 B 的存储。通过 `NamespaceFactory` ，你可以根据运行时上下文（Runtime Context）动态隔离数据：

- **按用户隔离** ： `namespace=lambda rt: (rt.server_info.user.identity,)`
- **按助手隔离** ： `namespace=lambda rt: (rt.server_info.assistant_id,)`

---

### 4\. 权限与策略钩子 (Permissions & Hooks)

除了路径级别的 `allow/deny` 权限，你还可以通过 **装饰器模式** 或 **子类化** 来增加自定义策略：

- **审计日志** ：记录 Agent 所有的写操作。
- **内容审查** ：防止 Agent 将敏感数据（如密钥）写入文件。

## Deep Agents 与 子代理

> https://docs.langchain.com/oss/python/deepagents/subagents

在 Deep Agents 框架中， **子代理（Subagents）** 是一种强大的架构模式，用于处理复杂任务并保持主代理上下文的整洁。

子代理的主要作用是解决 **“上下文膨胀（Context Bloat）”** 问题。当代理执行需要大量工具调用（如多次搜索、读取大文件）的任务时，这些中间过程会迅速填满上下文窗口。通过将任务委派给子代理，主代理只需接收最终结果。

### 工作流程

1. **主代理（Main Agent）** ：接收复杂指令，利用 `task()` 工具触发子代理。
2. **子代理（Subagent）** ：在隔离的上下文中执行具体工作（例如：进行 10 次网页搜索）。
3. **结果返回** ：子代理将处理好的总结或 **结构化 JSON** 返回。
4. **上下文清理** ：主代理只看到结果，而不会看到那 10 次搜索的冗长细节。

可以通过以下两种主要方式定义子代理：

### 1\. 基于字典的子代理（最常用）

适用于大多数需要特定提示词（Prompt）和工具集的场景。

| 字段 | 是否必填 | 说明 |
| --- | --- | --- |
| `name` | 是 | 唯一标识符，主代理通过此名称调用。 |
| `description` | 是 | **关键：**  主代理根据描述决定何时委派任务。描述需具体且面向动作。 |
| `system_prompt` | 是 | 子代理的角色指令，不会继承主代理的提示词。 |
| `tools` | 是 | 子代理可调用的工具列表。建议保持精简。 |
| `model` | 否 | 可选。可覆盖主代理的模型（例如：用更强的模型处理复杂逻辑）。 |

### 2\. 已编译的子代理（CompiledSubAgent）

适用于极复杂的流程。你可以将一个预先编译好的 **LangGraph** 图（Graph）作为子代理传入。

## Deep Agents 与 异步子代理

> https://docs.langchain.com/oss/python/deepagents/async-subagents

在 Deep Agents 框架中， **异步子代理（Async Subagents）** 是一项进阶功能，允许主代理在后台启动多个任务，同时保持与用户的持续沟通。这与同步子代理（主代理必须等待子代理完成）有本质区别。

异步子代理让主代理具备了“多线程”处理能力。主代理可以一边让研究员去查资料，一边让程序员去写代码，自己则继续陪用户聊天或处理其他琐事。

### 关键区别：同步 vs 异步

| 维度 | 同步子代理 (Sync) | 异步子代理 (Async) |
| --- | --- | --- |
| **执行模型** | 主代理被阻塞，直到子代理完成 | 立即返回任务 ID，主代理继续运行 |
| **并发性** | 顺序或阻塞式并行 | 真正的非阻塞并行 |
| **中途干预** | 不支持 | 支持更新指令 (`update_async_task`) |
| **取消任务** | 不支持 | 支持随时取消 (`cancel_async_task`) |
| **适用场景** | 耗时短、必须拿到结果才能下一步 | 耗时长、需要并行、需要用户交互 |

当配置了异步子代理后，主代理会自动获得 5 个核心工具：

1. `start_async_task` ：启动任务，立即拿到一个任务 ID。
2. `check_async_task` ：查询特定任务的状态（运行中、成功、失败）和结果。
3. `update_async_task` ：给正在运行的任务发“新指令”，子代理会结合历史上下文重新开始。
4. `cancel_async_task` ：强制停止任务。
5. `list_async_tasks` ：列出所有后台任务及其当前进度。

理解异步任务的生命周期对于设计高效的 AI 代理至关重要：

1. **启动（Launch）** ：用户要求研究 X 话题。主代理启动研究员子代理，记录 ID 后告诉用户：“好的，研究已开始，你可以继续问我其他问题。”
2. **交互（Interact）** ：用户继续问其他事，主代理正常回答。
3. **查询（Check）** ：用户问：“研究得怎么样了？”。主代理调用 `check` 工具。
- 如果没完，告诉用户：“还在努力中，请稍候。”
	- 如果完了，将子代理的总结反馈给用户。

你可以根据性能和扩展性需求选择不同的部署方式：

- **单一部署 (ASGI) **：所有代理都在同一个进程/服务器中运行。没有网络延迟，配置最简单，是** 默认推荐** 方式。
- 拆分部署 (HTTP)：主代理在 A 服务器，子代理在 B 服务器。适用于子代理由不同团队维护，或者需要不同计算资源（如子代理需要 GPU）的情况。
- **混合部署** ：部分子代理本地运行，部分子代理远程调用。

### 1\. 描述必须精准

主代理依靠 `description` 来决定把任务派给谁。

- ✅ **好描述** ： "负责使用 Web 搜索进行深入研究，适用于需要多步搜索和信息综合的复杂问题。"
- ❌ **坏描述** ： "帮我查东西的助手。"

### 2\. 避免盲目轮询

**常见错误** ：主代理在启动任务后立刻反复调用 `check` ，这会让异步变成事实上的同步。

- **对策** ：在系统提示词（System Prompt）中明确告诉主代理：“启动异步任务后， **必须** 立即把控制权交还给用户，不要立刻轮询状态。”

### 3\. 本地开发注意 worker 数量

如果你在本地使用 `langgraph dev` 开发，记得增加 worker 数量。如果 supervisor 带 3 个异步子代理，至少需要 4 个并发槽位，否则任务会一直排队。

```
langgraph dev --n-jobs-per-worker 10
```

### 4\. 状态持久化

异步任务的元数据存储在独立的 `async_tasks` 通道中。这意味着即使主代理的对话历史因为太长而被总结（Summarization），它依然能记得所有后台任务的 ID。

## Deep Agents 与 人机交互

> https://docs.langchain.com/oss/python/deepagents/human-in-the-loop

在 Deep Agents 框架中， **人机交互（Human-in-the-loop, HITL）** 是一项关键的安全特性。它允许开发者在代理执行敏感操作（如删除文件、发送邮件、支付扣款）之前，强制引入人工审核环节。

HITL 基于 LangGraph 的 **中断（Interrupt）** 机制。当代理尝试调用被标记为“敏感”的工具时，系统会自动暂停执行并保存当前状态，直到接收到人类的显式指令。

### 决策类型 (Decision Types)

当任务被中断时，人类可以做出以下三种决策：

1. `approve` (批准)：原封不动地执行代理提出的工具调用。
2. `edit` (修改)：在执行前，手动调整工具的参数（例如：修改邮件收件人或缩减删除范围）。
3. `reject` (拒绝)：完全取消该操作，代理会收到“操作被拒绝”的反馈。

要启用 HITL，你需要在创建代理时配置 `interrupt_on` 参数，并 **必须提供一个 `checkpointer`** 来保存状态。

### 示例代码

```
from deepagents import create_deep_agent
from langgraph.checkpoint.memory import MemorySaver

# 1. 必须配置 Checkpointer
checkpointer = MemorySaver()

# 2. 定义哪些工具需要审核
interrupt_on = {
    "delete_file": True,  # 默认允许：批准、修改、拒绝
    "send_email": {"allowed_decisions": ["approve", "reject"]},  # 禁止修改内容
    "read_file": False,   # 安全操作，无需审核
}

agent = create_deep_agent(
    model="google_genai:gemini-3.1-pro-preview",
    tools=[delete_file, send_email, read_file],
    interrupt_on=interrupt_on,
    checkpointer=checkpointer
)
```

### 1\. 触发中断

当代理执行 `delete_file` 时， `agent.invoke` 会立即返回。你可以通过 `result.interrupts` 检查是否发生了中断。

### 2\. 获取用户反馈

你需要将待办操作展示给用户，并收集他们的决策。

### 3\. 恢复执行 (Resume)

使用 `Command(resume=...)` 并传入相同的 `thread_id` 来继续任务。

```
# 恢复执行的伪代码
if result.interrupts:
    # 假设用户点击了“批准”
    decisions = [{"type": "approve"}]
    
    # 使用 Command 恢复，必须保持 config 一致
    result = agent.invoke(
        Command(resume={"decisions": decisions}),
        config=config,
        version="v2"
    )
```

Deep Agents 支持更精细的中断控制：

- **工具级别中断** ：主代理和子代理可以有各自独立的 `interrupt_on` 配置。子代理可以覆盖主代理的设置。
- 指令级别中断 (`interrupt()`)：在工具代码内部，你可以直接调用 `interrupt()` 原语。这适用于那些逻辑复杂、需要根据中间计算结果请求人类输入的场景。

## Deep Agents 与 权限控制

> https://docs.langchain.com/oss/python/deepagents/permissions

在 Deep Agents 框架中， **权限控制（Permissions）** 允许你通过声明式的规则，精确定义代理可以访问或修改哪些文件和目录。这对于构建安全、可控的 AI 系统至关重要。

权限系统通过一组规则来约束代理内置的各种文件系统工具（如 `ls`, `read_file`, `write_file` 等）。

每个权限规则包含三个核心字段：

- `operations` ：指定适用的操作类型。 `"read"` （涵盖读取、列表、搜索等）或 `"write"` （涵盖写入、修改等）。
- `paths` ：使用 Glob 模式（如 `/workspace/` ）匹配目标路径。
- `mode` ：设为 `"allow"` （允许）或 `"deny"` （拒绝）。

权限规则按照你定义的 **列表顺序** 从上往下进行评估。一旦找到匹配的操作和路径，该规则就决定了最终结果（允许或拒绝），后续规则将被忽略。

### 1\. 隔离工作区

只允许代理读写 `/workspace/` 目录，禁止访问系统其他任何地方。

```
permissions=[
    FilesystemPermission(operations=["read", "write"], paths=["/workspace/**"], mode="allow"),
    FilesystemPermission(operations=["read", "write"], paths=["/**"], mode="deny"),
]
```

### 2\. 保护敏感文件 (如.env)

允许代理在工作区操作，但必须排除掉配置文件。

```
permissions=[
    FilesystemPermission(operations=["read", "write"], paths=["/workspace/.env"], mode="deny"), # 先写禁止
    FilesystemPermission(operations=["read", "write"], paths=["/workspace/**"], mode="allow"), # 后写允许
]
```

### 3\. 只读内存 (Read-only Memory)

允许代理读取组织策略或共享知识库，但禁止其修改。

```
permissions=[
    FilesystemPermission(operations=["write"], paths=["/policies/**"], mode="deny"),
]
```

默认情况下， **子代理会继承父代理的所有权限** 。 如果你想给子代理设定不同的权限（例如：给“审计员”子代理只读权限），你可以在子代理的配置中定义 `permissions` 字段。这将 **完全替换** 父代理的规则，而不是合并。

## Deep Agents 与 记忆

> https://docs.langchain.com/oss/python/deepagents/memory

在 Deep Agents 框架中， **记忆（Memory）** 是让代理能够跨对话学习、改进并建立个性化体验的核心机制。它将记忆视为“文件系统”，代理可以像读写本地文件一样管理自己的知识。

Deep Agents 的记忆分为两个层面：

1. **短期记忆** ：单次对话内的上下文（由 LangGraph 状态管理，自动处理）。
2. **长期记忆** ：跨越不同对话、甚至不同用户的持久化信息（由 `memory` 和 `backends` 管理）。

### 运作流程

- **加载** ：启动时，代理读取指定的内存文件（如 `preferences.md` ）进入系统提示词。
- **按需读取** ：对于较大的知识库或“技能（Skills）”，代理只在需要时才读取具体文件内容，保持上下文精简。
- **更新** ：代理在对话中学习到新信息时，会调用 `edit_file` 工具修改记忆文件。

你可以通过配置 `StoreBackend` 的 `namespace` （命名空间）来决定谁能访问哪些记忆。

### 1\. 代理级记忆 (Agent-scoped)

- **定义** ：所有用户共享同一个记忆文件。
- **效果** ：代理形成统一的“人设”和知识库。它从与 A 用户的交流中学习到的经验，可以应用在与 B 用户的对话中。
- **实现** ：命名空间绑定到 `assistant_id` 。

### 2\. 用户级记忆 (User-scoped)

- **定义** ：每个用户拥有独立的记忆文件。
- **效果** ：实现高度个性化。代理记得 Alice 喜欢简洁的代码，记得 Bob 喜欢详细的解释，两者互不干扰。
- **实现** ：命名空间绑定到 `user.identity` 。

并不是所有的记忆都应该是可写的。

| 记忆类型 | 读写权限 | 管理方式 |
| --- | --- | --- |
| **用户偏好** | 读写 (Read-Write) | 代理通过工具自行更新。 |
| **组织策略** | 只读 (Read-Only) | 由管理员通过代码更新，防止“提示词注入”篡改合规要求。 |
| **共享技能** | 只读/受限 | 只有特定权限的代理或人工审核后方可修改。 |

## Deep Agents 与 Skills

> https://docs.langchain.com/oss/python/deepagents/skills

在 Deep Agents 框架中， **技能（Skills）** 是赋予代理专业能力、复杂工作流和领域知识的可重用模块。与总是加载到提示词中的“记忆”不同，技能采用 **渐进式披露（**

**Progressive**

**

Disclosure

）** 机制：代理仅在任务需要时才读取具体的技能细节，从而保持上下文的高效和精简。

技能以文件夹的形式存在，核心是一个 `SKILL.md` 文件，其中包含元数据和详细指令。

### 技能文件夹结构

- **`SKILL.md` （必须）** ：包含 YAML 格式的元数据（名称、描述、允许使用的工具）和具体的执行指令。
- **辅助脚本（可选）** ：如 `.py` 或 `.sh` 文件，供技能内部逻辑调用。
- **参考资料（可选）** ：相关的文档或知识库文件。
- **资源模板（可选）** ：用于生成特定格式内容的模板。

### 🔄 工作流程：渐进式披露

代理管理技能遵循三个阶段，确保在大规模技能库中依然能保持高性能：

1. 匹配 (Match)：启动时，代理仅读取所有技能的 `description` 。当接收到用户请求时，它会判断哪个技能最匹配。
2. 读取 (Read)：一旦确定匹配，代理才会读取该技能完整的 `SKILL.md` 内容。
3. 执行 (Execute)：代理根据 `SKILL.md` 中的详细步骤，调用工具或参考辅助文件来完成任务。

### ⚖️ 技能 vs 记忆 (Memory) vs 工具 (Tools)

| 特性 | 技能 (Skills) | 记忆 (Memory) | 工具 (Tools) |
| --- | --- | --- | --- |
| **加载方式** | **按需加载** | 始终加载到提示词中 | 始终作为函数列表存在 |
| **主要用途** | 复杂的、任务特定的工作流 | 个性化偏好、项目规范 | 执行具体原子操作（如 API 调用） |
| **文件格式** | 包含元数据的 `SKILL.md` | `AGENTS.md`  文本文件 | Python 函数或类 |
| **优势** | 节省 Token，适合大型知识库 | 保证代理始终遵循核心规范 | 让代理能与外部系统交互 |

### 1\. 定义技能 (SKILL.md)

技能文件的顶部必须包含 Frontmatter 元数据：

```
---
name: arxiv-researcher
description: 当用户需要从 arXiv 搜索和总结论文时使用此技能。
allowed-tools: web_search, fetch_url
---
# 详细步骤...
```

### 2\. 注册技能

在创建代理时，通过 `skills` 参数传入技能目录路径。如果多个目录中有同名技能， **后传入的会覆盖前面的** （Last-match-wins）。

```
agent = create_deep_agent(
    model="gemini-3.1-pro",
    skills=["/base/skills/", "/project/custom_skills/"], # 自定义技能优先
)
```

## Deep Agents 与 沙箱

> https://docs.langchain.com/oss/python/deepagents/sandboxes

在 Deep Agents 框架中， **沙箱（Sandboxes）** 是一种特殊的后端（Backend），它为代理提供了一个完全隔离的执行环境。与仅支持文件操作的普通后端不同，沙箱后端允许代理运行任意的 Shell 命令，这使得它成为构建 **编程代理** 和 **数据分析代理** 的核心。

沙箱在代理与你的主机系统之间建立了一道防线。即便代理生成并执行了具有破坏性的代码，它也无法访问你的本地凭据、私有文件或宿主机网络。

- **代码执行** ：自动克隆 Git 仓库、安装依赖、运行单元测试（如 `pytest` ）。
- **数据科学** ：安装 `pandas` 等库，处理大型数据集，生成统计图表或报告。
- **环境一致性** ：为每个任务或每个用户提供一个干净、预装好工具的运行环境。

一旦配置了沙箱后端，代理会自动获得两类工具：

1. **标准文件工具** ： `ls`, `read_file`, `write_file`, `edit_file`, `glob`, `grep` 。
2. 执行工具 (`execute`)：在沙箱内运行任意 Shell 命令的能力。

你可以根据应用需求选择不同的架构模式：

### 1\. 沙箱即工具 (Sandbox as Tool) —— 推荐

代理运行在你的服务器上，仅在需要运行代码时，通过 API 调用远程沙箱执行命令。

- ✅ **优点** ：无需重建镜像即可更新代理逻辑；API 密钥保存在沙箱外，更安全。
- ❌ **缺点** ：每次执行命令都有一定的网络延迟。

### 2\. 代理在沙箱中 (Agent in Sandbox)

代理及其所有逻辑直接运行在沙箱内部。

- ✅ **优点** ：环境与本地开发完全一致；延迟更低。
- ❌ **缺点** ：API 密钥必须存放在沙箱内；更新逻辑需要重新构建镜像。

沙箱会消耗资源，因此管理其“存活时间”至关重要：

- 线程作用域 (Thread-scoped)：每个对话线程对应一个独立的沙箱。对话结束或超过存活时间（TTL）后，沙箱自动销毁。适合需要干净环境的单次任务。
- 助手作用域 (Assistant-scoped)：同一个助手下的所有对话共享一个沙箱。文件和安装的包会持久化。适合需要长期维护工作区（如维护一个代码库）的场景。
```
from daytona import Daytona
from deepagents import create_deep_agent
from langchain_daytona import DaytonaSandbox

# 1. 创建沙箱实例
sandbox = Daytona().create()
backend = DaytonaSandbox(sandbox=sandbox)

# 2. 注入后端到代理
agent = create_deep_agent(
    model="gemini-3.1-pro",
    backend=backend,
    system_prompt="你是一个拥有沙箱访问权限的 Python 编程助手。"
)

# 3. 调用并自动清理
try:
    agent.invoke({"messages": [{"role": "user", "content": "安装 requests 并测试连接"}]})
finally:
    sandbox.stop() # 记得释放资源
```

目前支持的沙箱提供商包括 **Modal**, **Runloop**, **Daytona**, **LangSmith (Beta)** 等。你可以根据对算力、持久化和成本的需求选择最适合的集成。

## Deep Agents 与 流式传输

> https://docs.langchain.com/oss/python/deepagents/streaming

在 Deep Agents 框架中， **流式传输（Streaming）** 是提升用户体验的核心技术。它允许你实时查看主代理及其所有 **子代理（Subagents）** 的运行状态，而不需要等待整个复杂的任务链执行完毕。

Deep Agents 基于 LangGraph 的基础设施。要接收来自子代理的实时事件，关键是在调用 `stream` 时设置 `subgraphs=True` 和 `version="v2"` 。

### 核心代码结构

```
for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "研究量子计算"}]},
    stream_mode="updates", # 流式模式：更新、消息或自定义
    subgraphs=True,        # 必须：开启子代理流
    version="v2",          # 推荐：使用统一的 v2 数据格式
):
    # chunk 包含 type (类型), ns (命名空间), data (数据)
    print(f"来源: {chunk['ns']} | 类型: {chunk['type']}")
```

### 📡 四种主流流式模式

### 1\. 进度流 (stream\_mode="updates")

实时跟踪每个步骤的完成情况。你可以看到哪个子代理正在运行，以及它刚完成了哪个节点（如 `model_request` 或 `tools` ）。

- **用途** ：显示加载状态、步骤列表或进度条。

### 2\. 令牌流 (stream\_mode="messages")

实时输出 LLM 生成的每一个字符（Token）。

- **高级特性** ：由于子代理可能在并行运行，你可以根据 `chunk["ns"]` 将不同代理的 Token 路由到前端不同的 UI 窗口中，避免文字混杂。

### 3\. 工具调用流 (stream\_mode="messages")

在模型决定调用工具但尚未执行完时，提前获取工具名称和参数。

- **用途** ：在界面上显示“正在搜索网页...”或“正在分析数据库...”。

### 4\. 自定义更新流 (stream\_mode="custom")

使用 `get_stream_writer()` 在工具内部手动发送信号。

- **场景** ：对于耗时较长的任务（如处理 100 份文档），可以每处理一份就发送一个 `{"progress": 15%}` 的自定义事件。

## Deep Agents 与 ACP

> https://docs.langchain.com/oss/python/deepagents/acp

**代理客户端协议 (Agent Client Protocol, ACP)** 是一种标准化协议，旨在将你开发的 **Deep Agents** 无缝集成到代码编辑器和 IDE（如 Zed, VS Code, JetBrains）中。

通过 ACP，你的自定义代理可以直接访问项目上下文、修改文件，并以原生 UI 的方式在编辑器内与你互动。

ACP 充当了“代理大脑”与“代码编辑器”之间的桥梁。

- **双向通信** ：编辑器向代理发送当前选中的代码、项目结构；代理向编辑器发送修改建议、运行 Shell 命令或创建新文件。
- **标准化控制** ：无论你使用哪种 LLM 或代理框架，只要符合 ACP 标准，就可以在任何支持 ACP 的编辑器中使用。

你可以通过 `deepagents-acp` 库快速将一个普通的 Deep Agent 转换为 ACP 服务器。

### 1\. 安装

```
pip install deepagents-acp
```

### 2\. 启动 ACP 服务器

ACP 通常运行在 **stdio** 模式下，这意味着它通过标准输入/输出与 IDE 通信。

```
import asyncio
from acp import run_agent
from deepagents import create_deep_agent
from deepagents_acp.server import AgentServerACP

asyncdef main():
    # 创建你的 Deep Agent
    agent = create_deep_agent(
        model="gemini-3.1-pro",
        system_prompt="你是一个精通 Python 的编程助手。"
    )

    # 封装为 ACP 服务器
    server = AgentServerACP(agent)
    await run_agent(server)

if __name__ == "__main__":
    asyncio.run(main())
```

开发者经常混淆 ACP 和 MCP (Model Context Protocol)，它们的用途完全不同：

| 协议 | 全称 | 核心用途 | 比喻 |
| --- | --- | --- | --- |
| **ACP** | Agent Client Protocol | **代理 <-> 编辑器**  ：让代理住进你的编辑器。 | 代理的“UI 接口” |
| **MCP** | Model Context Protocol | **代理 <-> 外部工具**  ：让代理访问数据库、Google Drive 等外部数据。 | 代理的“手和数据源” |

## Deep Agents CLI

> https://docs.langchain.com/oss/python/deepagents/cli/overview

**Deep Agents CLI** 是一个基于 Deep Agents SDK 构建的开源终端编程助手。它能够像高级开发者一样工作：拥有持久化记忆、管理项目上下文、学习你的编码习惯，并在执行敏感操作（如修改文件或运行命令）前寻求你的许可。

### 🛠️ 核心能力

- **文件与终端操作** ：能够阅读、创建和编辑代码，并在本地或远程沙箱中运行测试及命令。
- **任务规划与追踪** ：自动将复杂的需求分解为待办事项列表（To-Dos），并实时跟踪进度。
- **智能记忆系统** ：通过 `AGENTS.md` 文件和自动保存的记忆，代理能记住项目的架构设计、编码规范及你的个人偏好。
- **上下文压缩** ：在长时间对话中，它会自动总结旧消息并清理上下文窗口，确保模型始终高效。
- **MCP 工具集成** ：支持通过 Model Context Protocol 加载外部工具，扩展其能力边界。

### 1\. 设置 API 密钥

将你的模型供应商（OpenAI, Anthropic 或 Google）密钥导出为环境变量，或添加到 `~/.deepagents/.env` 中。

```
export ANTHROPIC_API_KEY="your-api-key"
```

### 2\. 安装与运行

你可以直接使用以下命令进行安装并启动：

```
# 安装并运行
curl -LsSf https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/libs/cli/scripts/install.sh | bash

# 启动 CLI
deepagents
```

### 3\. 下达任务

进入交互界面后，你可以直接输入需求，例如：

> *“帮我创建一个带有单元测试的 Python 爬虫，用于抓取最新的 AI 新闻。”*

Deep Agents CLI 使用两种方式进行个性化定制：

### 1\. 记忆 (Memory)

- **自动记忆** ：代理会将学到的信息自动存放在 `~/.deepagents/<agent_name>/memories/` 下。
- **AGENTS.md** ：这是最重要的配置文件。
- **全局级** (`~/.deepagents/agent/AGENTS.md`)：存放你的通用偏好，如“总是使用 Google 风格的 Python 文档字符串”。
	- **项目级** (`.deepagents/AGENTS.md`)：存放在 Git 项目根目录，定义该项目特有的架构（如“本仓库使用特定版本的 React 状态管理”）。

### 2\. 技能 (Skills)

技能是专门的指令集。你可以创建自定义技能来处理特定任务。

- 使用 `/skill-creator` 可以引导你创建新技能。
- 使用 `/remember` 命令可以让代理根据当前的对话更新其记忆或技能。

| 命令 / 快捷键 | 功能 |
| --- | --- |
| **`/model`** | 切换当前使用的模型（如从 Claude 切换到 GPT-4o）。 |
| **`!`** | 进入 **Shell 模式** ，直接输入终端命令（如 `!git status` ）。 |
| **`@filename`** | 在对话中自动补全文件名并将其内容注入 Prompt。 |
| **`Shift + Tab`** | 切换 **自动批准 (Auto-approve)** 模式，无需反复确认工具调用。 |
| **`/threads`** | 浏览并恢复之前的对话记录。 |

## 案例：Data Analysis Agent

> https://docs.langchain.com/oss/python/deepagents/data-analysis

构建数据分析智能体（Data Analysis Agent）是 Deep Agents SDK 的核心应用场景之一。这类智能体能够自动规划任务、编写代码、在沙盒中执行分析，并最终产出可视化图表和报告。

数据分析智能体通常由三个关键部分组成：

1. 模型 (LLM)：负责理解分析需求、编写 Python 代码和解释结果。
2. 沙盒后端 (Backend)：提供一个隔离的运行环境（如 Daytona, Modal 或 Local Shell），用于执行生成的代码并处理数据文件。
3. 自定义工具 (Tools)：扩展代理的能力，例如将生成的图表发送到
	Slack
	或存入数据库。

### 1\. 环境准备

首先安装基础库。为了确保安全，强烈建议使用沙盒后端。

```
pip install deepagents slack-sdk
```

### 2\. 配置执行后端

你可以选择不同的沙盒环境。以下是以 **Local Shell** （本地环境）为例的配置：

```
from deepagents.backends import LocalShellBackend

# 设置工作目录，代理只能访问该目录下的文件
backend = LocalShellBackend(root_dir="./data_analysis_workspace")
```

### 3\. 定义发送工具

如果希望代理能分享结果，可以编写一个简单的工具：

```
from langchain.tools import tool

@tool
def share_to_slack(summary: str, image_path: str):
    """将分析摘要和生成的图表路径发送给团队。"""
    # 逻辑代码：使用 slack-sdk 上传文件
    return "已成功发送至 Slack 频道。"
```

### 4\. 创建并运行代理

将模型、工具和后端整合在一起。

```
from deepagents import create_deep_agent

agent = create_deep_agent(
    model="google_genai:gemini-3.1-pro-preview",
    tools=[share_to_slack],
    backend=backend
)

# 开启任务
agent.invoke({"messages": [("user", "分析 sales.csv 文件，绘制销售趋势图并分享到 Slack。")]})
```

当代理接收到任务后，它会经历以下自动化步骤：

1. 探索 (Exploration)：运行 `ls` 或 `read_file` 检查数据文件的列名和格式。
2. 编码 (Coding)：生成一段 Python 脚本（通常使用 Pandas 和 Matplotlib/Seaborn）。
3. 执行 (Execution)：在沙盒中运行该脚本，生成类似 `sales_plot.png` 的文件。
4. 输出 (Delivery)：调用 `share_to_slack` 工具，将统计结论和图表一起推送到指定频道。

## 案例：Deep Research Agent

> https://docs.langchain.com/oss/python/deepagents/deep-research

构建深度研究智能体（Deep Research Agent）是应对复杂查询的进阶方案。不同于简单的问答机器人，这种智能体能够像人类研究员一样，将大目标拆解为小任务，并指挥“子智能体”去互联网的各个角落搜集情报，最后汇编成带引用文献的专业报告。

深度研究智能体的精髓在于 “编排与委托” (

Orchestration

& Delegation)。

1. 编排器 (Orchestrator)：主智能体负责全局规划。它维护一个待办事项列表（Todo List），决定哪些部分需要深挖，哪些部分可以并行处理。
2. 子智能体 (Sub-agents)：被派往执行具体任务的专门部队。它们拥有独立的上下文，专注于搜索特定的子话题（例如“RAG 的成本分析”），并只将提炼后的结果返回给主智能体。

### 1\. 赋予“眼睛”：构建增强搜索工具

普通的搜索工具只返回摘要。为了深度研究，我们需要一个能抓取网页全文并转为 Markdown 格式的工具，让智能体阅读原始素材。

```
@tool
def tavily_search(query: str):
    """搜索网页并抓取全文内容。"""
    # 步骤：1. 用 Tavily 找 URL；2. 用 httpx 抓取 HTML；3. 用 markdownify 转为文本
    # 这种方式确保智能体能读到细节而非碎片
    ...
```

### 2\. 定义角色指令 (System Prompts)

你需要为不同层级的智能体设定明确的“交战规则”：

- **主智能体指令** ：强调规划、并行控制和引用格式（如 `[1]`, `[2]` ）。
- **子智能体指令** ：强调搜索预算（防止死循环）和信息质量评估。

### 3\. 配置并行委托

利用 `create_deep_agent` 的 `subagents` 参数，你可以轻松定义这些“数字雇员”：

```
research_sub_agent = {
    "name": "research-agent",
    "description": "处理具体的搜索和事实发现任务",
    "system_prompt": RESEARCHER_INSTRUCTIONS,
    "tools": [tavily_search], # 只有子智能体需要搜索工具
}

agent = create_deep_agent(
    model=model,
    subagents=[research_sub_agent], # 主智能体通过 subagents 列表管理它们
    ...
)
```

## 案例：Content Builder Agent

> https://docs.langchain.com/oss/python/deepagents/content-builder

构建内容生成智能体（Content Builder Agent）将你的创作流程从简单的“指令-输出”升级为一套具有 **品牌记忆** 、 **专业技能** 和 **多模态产出** 能力的自动化系统。

这个智能体不仅仅是一个撰稿人，它更像是一个配备了研究员、设计和文件管理员的小型编辑团队。

- 长期记忆 (`AGENTS.md`)：存储品牌调性（Brand Voice）、写作标准和核心支柱。这确保了生成的每一篇内容都符合公司风格。
- 技能系统 (`skills/`)：通过 Markdown 文件定义特定任务的 SOP（标准作业程序）。例如， `blog-post` 技能会强制要求先研究再写作，并必须生成封面图。
- **多模态工具** ：集成 Google Gemini 进行图像生成，集成 Tavily 进行联网搜索，让智能体具备“读、写、看、绘”的全方位能力。

### 1\. 技能导向的工作流

通过在 `SKILL.md` 中编写 YAML 元数据和详细指令，你可以让智能体在识别到特定意图（如“写篇博客”）时，自动加载对应的约束条件。

```
# skills/blog-post/SKILL.md 中的定义
---
name: blog-post
description: 用于撰写长篇技术博客和 SEO 优化。
---
# 这里是详细的 SOP 指令...
```

### 2\. 自动化研究与分发

智能体利用 `subagents.yaml` 中定义的 `researcher` 子智能体，在动笔之前先进行深度搜索并保存为 `research/[topic].md` 。这解决了 AI 创作中常见的“事实性错误”问题。

### 3\. 文件系统后端 (FilesystemBackend)

不同于普通的对话机器人，该智能体拥有“手”。它可以在你的本地目录下创建文件夹、保存 Markdown 报告以及 `.png` 封面图，实现真正的资产交付。

```
# 将智能体与本地文件系统绑定
agent = create_deep_agent(
    ...
    backend=FilesystemBackend(root_dir="./my_project"),
)
```

\# *学习大模型 & 讨论Kaggle* #

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uoTGEibAZUEgGtr0ib3fibjtZGGiawJxeZb8NEPR0DibUlaMhD1mD7NiajMfbiaBiarSpbLMkrct2I5dsSVoOnCFD7zElg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=g282dig6&tp=webp#imgIndex=0)

△长按添加竞赛小助手

每天大模型、算法竞赛、干货资讯

与 36000+来自竞赛爱好者一起交流~

继续滑动看下一个

Coggle数据科学

向上滑动看下一个