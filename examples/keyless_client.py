"""Keyless Cucutime MCP client: standard library only (Python 3.8+). Run: python3 keyless_client.py Mia space"""
import json, sys, urllib.request

MCP = "https://cucutime.org/mcp"


def rpc(method, params, id_=1):
    body = json.dumps({"jsonrpc": "2.0", "id": id_, "method": method, "params": params}).encode()
    req = urllib.request.Request(MCP, data=body, headers={"Content-Type": "application/json",
                                                          "Accept": "application/json, text/event-stream"})
    raw = urllib.request.urlopen(req, timeout=30).read().decode()
    # The server answers with plain JSON (or a single SSE "data:" line, depending on the client's Accept header).
    raw = raw.split("data:", 1)[-1] if raw.lstrip().startswith("event:") or raw.lstrip().startswith("data:") else raw
    return json.loads(raw)


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "Mia"
    theme = sys.argv[2] if len(sys.argv) > 2 else "space"
    tools = rpc("tools/list", {})["result"]["tools"]
    print("tools:", ", ".join(t["name"] for t in tools))
    res = rpc("tools/call", {"name": "generate_song_idea", "arguments": {"name": name, "theme": theme, "language": "en"}}, 2)
    print(res["result"]["content"][0]["text"])
