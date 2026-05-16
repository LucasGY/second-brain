# Second Brain MCP Server

This repository includes a small MCP server that lets ChatGPT, Claude, and other MCP clients search the wiki, read pages, and save durable conversation knowledge back into `wiki/analyses/`.
> 本仓库包含一个轻量 MCP 服务，让 ChatGPT、Claude 和其他 MCP 客户端可以搜索 wiki、读取页面，并把值得沉淀的对话知识保存到 `wiki/analyses/`。

## Tools

- `search_wiki`: search maintained wiki pages before creating new notes.
> `search_wiki`：创建新笔记前搜索已有 wiki 页面。
- `read_wiki_page`: read a page by canonical slug.
> `read_wiki_page`：通过规范 slug 读取页面。
- `list_recent_sources`: list recently modified source notes.
> `list_recent_sources`：列出最近修改的来源笔记。
- `save_knowledge_note`: create a bilingual analysis page from durable conversation knowledge, rebuild the index, and append an `UPDATE` log entry.
> `save_knowledge_note`：将对话中值得长期保存的知识写成双语分析页面，重建索引，并追加 `UPDATE` 日志。
- `get_wiki_operating_rules`: return the key write rules.
> `get_wiki_operating_rules`：返回关键写入规则。

## Run Locally For Claude Desktop

Use stdio transport in `claude_desktop_config.json`:
> 在 `claude_desktop_config.json` 中使用 stdio transport：

```json
{
  "mcpServers": {
    "second-brain": {
      "command": "/root/.openclaw/.venv/bin/python",
      "args": ["/root/.openclaw/second-brain/scripts/second_brain_mcp.py"]
    }
  }
}
```

## Run As A Remote MCP Server

ChatGPT Developer Mode and remote Claude connectors require an HTTP-accessible MCP server. Start streamable HTTP like this:
> ChatGPT Developer Mode 和 Claude 远程连接器需要可通过 HTTP 访问的 MCP 服务。这样启动 streamable HTTP：

```bash
/root/.openclaw/.venv/bin/python /root/.openclaw/second-brain/scripts/second_brain_mcp.py \
  --transport streamable-http \
  --host 0.0.0.0 \
  --port 8765
```

The MCP endpoint is:
> MCP 端点是：

```text
http://YOUR_HOST:8765/mcp
```

For SSE clients, start with `--transport sse`; the endpoint is `http://YOUR_HOST:8765/sse`.
> 对于 SSE 客户端，使用 `--transport sse` 启动；端点是 `http://YOUR_HOST:8765/sse`。

## Security Notes

This server currently has no built-in authentication. Do not expose it directly to the public internet unless it is behind a trusted access layer such as a private network, reverse proxy, or Cloudflare Access.
> 当前服务没有内置认证。除非放在可信访问层之后，例如私有网络、反向代理或 Cloudflare Access，否则不要直接暴露到公网。

The write surface is intentionally narrow: conversation captures are saved under `wiki/analyses/`, `raw/` is never modified, and every save appends to `wiki/log.md`.
> 写入面刻意保持狭窄：对话沉淀会保存到 `wiki/analyses/`，永不修改 `raw/`，每次保存都会追加到 `wiki/log.md`。
