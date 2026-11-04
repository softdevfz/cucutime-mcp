#!/bin/sh
# Keyless calls to the Cucutime MCP server (Streamable HTTP, stateless). No key, no dependencies.
MCP=https://cucutime.org/mcp
H1='Content-Type: application/json'; H2='Accept: application/json, text/event-stream'
curl -s $MCP -H "$H1" -H "$H2" -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"curl-example","version":"1"}}}'; echo
curl -s $MCP -H "$H1" -H "$H2" -d '{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}'; echo
curl -s $MCP -H "$H1" -H "$H2" -d '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"generate_song_idea","arguments":{"name":"Mia","theme":"space","language":"en"}}}'; echo
curl -s $MCP -H "$H1" -H "$H2" -d '{"jsonrpc":"2.0","id":4,"method":"tools/call","params":{"name":"search_catalog","arguments":{"query":"elephant","language":"en","limit":3}}}'; echo
