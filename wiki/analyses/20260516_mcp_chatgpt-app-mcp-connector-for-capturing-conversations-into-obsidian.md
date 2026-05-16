---
type: analysis
title: ChatGPT App MCP Connector for Capturing Conversations into Obsidian
aliases:
- 用 ChatGPT App / MCP Connector 将对话保存到 Obsidian
date_created: '2026-05-16'
source: MCP conversation capture
tags:
- chatgpt
- mcp
- obsidian
- second-brain
- knowledge-capture
- ai-agents
summary_en: 'A practical architecture for turning selected ChatGPT conversation content
  into durable Obsidian notes: ChatGPT calls a custom MCP tool, the MCP server writes
  Markdown into an Inbox or raw/chatgpt folder, and the vault syncs via Git, Syncthing,
  iCloud, or another second-brain pipeline.'
summary_zh: 一个将 ChatGPT 对话中选定内容沉淀为 Obsidian 笔记的实用架构：ChatGPT 调用自定义 MCP 工具，MCP Server
  将 Markdown 写入 Inbox 或 raw/chatgpt 目录，再通过 Git、Syncthing、iCloud 或 second-brain pipeline
  同步。
---

# ChatGPT App MCP Connector for Capturing Conversations into Obsidian
> 用 ChatGPT App / MCP Connector 将对话保存到 Obsidian

## Summary
A practical architecture for turning selected ChatGPT conversation content into durable Obsidian notes: ChatGPT calls a custom MCP tool, the MCP server writes Markdown into an Inbox or raw/chatgpt folder, and the vault syncs via Git, Syncthing, iCloud, or another second-brain pipeline.
> 一个将 ChatGPT 对话中选定内容沉淀为 Obsidian 笔记的实用架构：ChatGPT 调用自定义 MCP 工具，MCP Server 将 Markdown 写入 Inbox 或 raw/chatgpt 目录，再通过 Git、Syncthing、iCloud 或 second-brain pipeline 同步。

## Knowledge
## Core idea

Build a tool-style ChatGPT App / MCP Connector rather than trying to save every conversation automatically. The user explicitly decides which content is worth saving, then ChatGPT calls a custom `save_to_obsidian` tool exposed by an MCP server.

The default target should be an Obsidian Inbox, not the final knowledge graph. This keeps capture fast while preserving a later review step for splitting material into source, concept, entity, and analysis notes.

## Recommended architecture

Use a remote or always-on MCP server as the write bridge. ChatGPT cannot directly write to a local desktop Vault, so the MCP endpoint should be reachable over HTTPS and should write into either a server-hosted Vault or a locally running Vault exposed through a secure tunnel.

### Preferred path

Remote Linux server + second-brain Vault + Git sync back to local Obsidian.

This is better than direct local writes when the knowledge base already has an ingest pipeline, RSS/manual capture folders, and wiki generation rules.

## Embedded HTML flow for Obsidian

The following block can be pasted directly into an Obsidian Markdown note. It uses simple inline HTML/CSS so the flow remains readable even without Mermaid rendering.

<div style="border:1px solid #d0d7de;border-radius:12px;padding:16px;margin:16px 0;background:#f8fafc;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;">
  <div style="font-weight:700;font-size:18px;margin-bottom:12px;">ChatGPT → MCP → Obsidian Capture Flow</div>
  <div style="display:flex;flex-wrap:wrap;gap:10px;align-items:center;">
    <div style="padding:10px 12px;border-radius:10px;background:#ffffff;border:1px solid #cbd5e1;min-width:150px;text-align:center;">ChatGPT conversation<br><small>User selects content</small></div>
    <div style="font-weight:700;">→</div>
    <div style="padding:10px 12px;border-radius:10px;background:#ffffff;border:1px solid #cbd5e1;min-width:150px;text-align:center;">MCP tool call<br><code>save_to_obsidian</code></div>
    <div style="font-weight:700;">→</div>
    <div style="padding:10px 12px;border-radius:10px;background:#ffffff;border:1px solid #cbd5e1;min-width:150px;text-align:center;">HTTPS MCP Server<br><small>Auth + validation</small></div>
    <div style="font-weight:700;">→</div>
    <div style="padding:10px 12px;border-radius:10px;background:#ffffff;border:1px solid #cbd5e1;min-width:150px;text-align:center;">Obsidian Vault<br><small>00-Inbox / raw/chatgpt</small></div>
    <div style="font-weight:700;">→</div>
    <div style="padding:10px 12px;border-radius:10px;background:#ffffff;border:1px solid #cbd5e1;min-width:150px;text-align:center;">Review pipeline<br><small>Source / Concept / Entity</small></div>
  </div>
</div>

## Tool design

Start with one write tool only:

```json
{
  "name": "save_to_obsidian",
  "description": "Save useful ChatGPT conversation content into the user's Obsidian vault inbox as a Markdown note.",
  "inputSchema": {
    "title": "string",
    "content": "string",
    "tags": "string[]",
    "target_folder": "string",
    "note_type": "chatgpt-capture | source | concept | entity"
  }
}
```

Useful initial targets:

- `00-Inbox/` for quick captures.
- `raw/chatgpt/` for longer source-like conversation captures.
- `wiki/concepts/` only after human review.
- `wiki/entities/` only after human review.

## Suggested Markdown template

```markdown
---
type: chatgpt-capture
source: ChatGPT
created: {{iso_timestamp}}
status: inbox
tags:
  - chatgpt
  - mcp
  - obsidian
---

# {{title}}

## Summary

{{summary}}

## Captured Content

{{content}}

## Possible Links

- [[ai-agents]]
- [[mcp]]
- [[obsidian]]

## Next Actions

- [ ] Review
- [ ] Split into source/concept/entity notes if durable
- [ ] Link to existing wiki pages
```

## Security rules

The connector should be intentionally narrow at first:

- Only write under a configured Vault root.
- Only create or append Markdown files.
- Reject `../` path traversal.
- Avoid delete and overwrite operations in the first version.
- Generate safe filenames from titles.
- Return the final path after every write.
- Keep secrets out of tool responses.
- Require authentication on the MCP server, not only on the client UI.

## Implementation roadmap

1. Build `save_to_obsidian` only.
2. Write to `00-Inbox/` or `raw/chatgpt/`.
3. Add automatic Git commit/push after successful capture.
4. Add search tools later to avoid duplicate notes.
5. Add specialized tools only after the capture loop is reliable: `append_to_daily_note`, `create_concept_note`, `create_entity_note`, and `search_obsidian_notes`.

## Design principle

Do not automatically save all ChatGPT conversations. The better pattern is selective capture: save only the parts the user marks as durable, then process them through the second-brain review pipeline.
> ## 核心想法
>
> 不要一开始做“自动保存所有 ChatGPT 对话”。更好的做法是做一个工具型 ChatGPT App / MCP Connector：用户明确指出哪段内容值得保存，然后 ChatGPT 调用自定义 MCP Server 暴露的 `save_to_obsidian` 工具。
>
> 默认保存目标应该是 Obsidian Inbox，而不是直接进入正式知识图谱。这样可以保持 capture 很快，同时保留后续 review 步骤，把内容拆成 source、concept、entity、analysis 等长期笔记。
>
> ## 推荐架构
>
> 用一个远程或常驻的 MCP Server 作为写入桥。ChatGPT 不能直接写本地桌面上的 Obsidian Vault，所以 MCP endpoint 需要通过 HTTPS 访问，并写入服务器上的 Vault，或写入通过安全隧道暴露的本地 Vault。
>
> ### 首选路径
>
> 远程 Linux server + second-brain Vault + Git 同步回本地 Obsidian。
>
> 如果知识库已经有 ingest pipeline、RSS/manual capture 目录和 wiki 生成规则，这比直接写本地 Vault 更适合。
>
> ## 可内嵌到 Obsidian 的 HTML 流程
>
> 下面这段可以直接粘贴到 Obsidian Markdown 笔记里。它使用简单的 inline HTML/CSS，即使不依赖 Mermaid 也能读。
>
> <div style="border:1px solid #d0d7de;border-radius:12px;padding:16px;margin:16px 0;background:#f8fafc;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;">
>   <div style="font-weight:700;font-size:18px;margin-bottom:12px;">ChatGPT → MCP → Obsidian Capture Flow</div>
>   <div style="display:flex;flex-wrap:wrap;gap:10px;align-items:center;">
>     <div style="padding:10px 12px;border-radius:10px;background:#ffffff;border:1px solid #cbd5e1;min-width:150px;text-align:center;">ChatGPT conversation<br><small>User selects content</small></div>
>     <div style="font-weight:700;">→</div>
>     <div style="padding:10px 12px;border-radius:10px;background:#ffffff;border:1px solid #cbd5e1;min-width:150px;text-align:center;">MCP tool call<br><code>save_to_obsidian</code></div>
>     <div style="font-weight:700;">→</div>
>     <div style="padding:10px 12px;border-radius:10px;background:#ffffff;border:1px solid #cbd5e1;min-width:150px;text-align:center;">HTTPS MCP Server<br><small>Auth + validation</small></div>
>     <div style="font-weight:700;">→</div>
>     <div style="padding:10px 12px;border-radius:10px;background:#ffffff;border:1px solid #cbd5e1;min-width:150px;text-align:center;">Obsidian Vault<br><small>00-Inbox / raw/chatgpt</small></div>
>     <div style="font-weight:700;">→</div>
>     <div style="padding:10px 12px;border-radius:10px;background:#ffffff;border:1px solid #cbd5e1;min-width:150px;text-align:center;">Review pipeline<br><small>Source / Concept / Entity</small></div>
>   </div>
> </div>
>
> ## 工具设计
>
> 第一阶段只做一个写入工具：
>
> ```json
> {
>   "name": "save_to_obsidian",
>   "description": "Save useful ChatGPT conversation content into the user's Obsidian vault inbox as a Markdown note.",
>   "inputSchema": {
>     "title": "string",
>     "content": "string",
>     "tags": "string[]",
>     "target_folder": "string",
>     "note_type": "chatgpt-capture | source | concept | entity"
>   }
> }
> ```
>
> 初始保存位置：
>
> - `00-Inbox/`：随手 capture。
> - `raw/chatgpt/`：较完整、可作为 source 的对话记录。
> - `wiki/concepts/`：只在人工 review 后进入。
> - `wiki/entities/`：只在人工 review 后进入。
>
> ## Markdown 模板
>
> ```markdown
> ---
> type: chatgpt-capture
> source: ChatGPT
> created: {{iso_timestamp}}
> status: inbox
> tags:
>   - chatgpt
>   - mcp
>   - obsidian
> ---
>
> # {{title}}
>
> ## Summary
>
> {{summary}}
>
> ## Captured Content
>
> {{content}}
>
> ## Possible Links
>
> - [[ai-agents]]
> - [[mcp]]
> - [[obsidian]]
>
> ## Next Actions
>
> - [ ] Review
> - [ ] Split into source/concept/entity notes if durable
> - [ ] Link to existing wiki pages
> ```
>
> ## 安全规则
>
> 这个 Connector 第一版应该非常窄：
>
> - 只能写入配置好的 Vault root 之下。
> - 只能创建或追加 Markdown 文件。
> - 拒绝 `../` 这类路径穿越。
> - 第一版不要支持删除和覆盖。
> - 从标题生成安全文件名。
> - 每次写入都返回最终路径。
> - 不要把 secrets 放进 tool response。
> - 认证必须在 MCP Server 侧执行，不能只依赖前端 UI。
>
> ## 实施路线
>
> 1. 只做 `save_to_obsidian`。
> 2. 写入 `00-Inbox/` 或 `raw/chatgpt/`。
> 3. capture 成功后自动 Git commit / push。
> 4. 后续增加搜索工具，避免重复建笔记。
> 5. capture loop 稳定后，再添加 `append_to_daily_note`、`create_concept_note`、`create_entity_note`、`search_obsidian_notes` 等工具。
>
> ## 设计原则
>
> 不要自动保存所有 ChatGPT 对话。更好的模式是 selective capture：只保存用户认为有长期价值的片段，然后通过 second-brain review pipeline 进入正式知识库。

## Related
[[ai-agents]]
> 相关页面：[[ai-agents]]
