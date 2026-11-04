<!-- mcp-name: org.cucutime/mcp -->
# Cucutime MCP server & API

Personalized **kids-song** tools for AI agents and apps, from [Cucutime](https://cucutime.org). A hosted **remote MCP server** (Streamable HTTP) plus a small REST API.

- **MCP endpoint:** `https://cucutime.org/mcp`
- **Official MCP Registry:** [`org.cucutime/mcp`](https://registry.modelcontextprotocol.io/v0/servers?search=org.cucutime)
- **Docs:** <https://cucutime.org/developers> · OpenAPI: <https://cucutime.org/api/openapi.json> · [llms.txt](https://cucutime.org/llms.txt)

This repository has the public **registry manifest, client configs and examples**. The server itself is hosted by Cucutime, so there is nothing to install.

## Tools

| Tool | Key? | What it does |
|---|---|---|
| `generate_song_idea` | no | Draft a personalized song (title, music style, chorus) for a child's first name and a theme |
| `get_song_for_name` | no | Cucutime's page and free-sample link for a child's first name |
| `search_catalog` | no | Search Cucutime's own kids songs and educational videos (es / pt / en) by words in the title |
| `create_personalized_song` | **yes** | A 30-second song that sings the name (lyrics + signed mp3 URL, valid 24 h) |
| `moderate_kids_text` | **yes** | Check whether a text is appropriate for children aged 2–8 |

The keyless tools use no generative AI and are safe for any app. **The two AI tools are for adult-facing apps only** (parents, teachers, creators), as required by the [developer terms](https://cucutime.org/developers/terms). Get a free trial key at <https://cucutime.org/developers>.

Send **first names only**: no surnames or other personal data.

## Connect

**Claude Code**
```bash
# keyless tools
claude mcp add --transport http cucutime https://cucutime.org/mcp
# with a developer key (adult-facing apps only)
claude mcp add --transport http cucutime https://cucutime.org/mcp --header "Authorization: Bearer cct_YOUR_KEY"
```

**Cursor** (`.cursor/mcp.json`) and other clients that support remote servers with headers:
```json
{ "mcpServers": { "cucutime": { "url": "https://cucutime.org/mcp", "headers": { "Authorization": "Bearer cct_YOUR_KEY" } } } }
```
Omit `headers` to use the keyless tools only. A ready-made project config is in [`.mcp.json`](.mcp.json).

**Claude Desktop** (`claude_desktop_config.json`, via `mcp-remote`):
```json
{ "mcpServers": { "cucutime": { "command": "npx", "args": ["-y", "mcp-remote", "https://cucutime.org/mcp", "--header", "Authorization:Bearer cct_YOUR_KEY"] } } }
```

**Claude.ai and ChatGPT custom connectors:** add `https://cucutime.org/mcp` with no authentication to use the three keyless tools. These connectors can't send a static API key yet, so use the AI tools from a client that sends headers, or through the REST API.

## Try it in 10 seconds (no key)

```bash
curl -s https://cucutime.org/mcp -H 'Content-Type: application/json' -H 'Accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"generate_song_idea","arguments":{"name":"Mia","theme":"space","language":"en"}}}'
```

More examples are in [`examples/`](examples/): [curl](examples/curl.sh), [Python](examples/keyless_client.py) and [Node](examples/keyless_client.mjs). None of them has dependencies.

## REST

```bash
# keyless
curl "https://cucutime.org/api/song-idea?name=Mia&theme=space&lang=en"
curl "https://cucutime.org/api/catalog?q=elephant&lang=en&limit=5"

# with a key (adult-facing apps only)
curl -X POST https://cucutime.org/api/dev/v1/songs \
  -H "Authorization: Bearer cct_YOUR_KEY" -H "Content-Type: application/json" \
  -d '{"name":"Mia","language":"en","theme":"a trip to the moon","age":5}'
curl https://cucutime.org/api/dev/v1/usage -H "Authorization: Bearer cct_YOUR_KEY"
```

## Limits and terms

- The trial key is free, with a per-key song limit and rate limits. See [/developers](https://cucutime.org/developers) for the current numbers.
- AI tools: **adult-facing apps only.** Never in an app directed to children or likely to be used by them.
- [Developer terms](https://cucutime.org/developers/terms) · [Privacy](https://cucutime.org/privacy)

## License

The examples and configs in this repository are MIT-licensed (see [LICENSE](LICENSE)). The Cucutime service, its content and its API are governed by the developer terms.
