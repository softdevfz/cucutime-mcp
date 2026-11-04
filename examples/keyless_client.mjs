// Keyless Cucutime MCP client: Node 18+ (built-in fetch), no dependencies. Run: node keyless_client.mjs Mia space
const MCP = 'https://cucutime.org/mcp';
async function rpc(method, params, id = 1) {
  const r = await fetch(MCP, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', Accept: 'application/json, text/event-stream' },
    body: JSON.stringify({ jsonrpc: '2.0', id, method, params }),
  });
  let text = await r.text();
  if (/^\s*(event|data):/.test(text)) text = text.split('data:').slice(1).join('data:');
  return JSON.parse(text);
}
const [name = 'Mia', theme = 'space'] = process.argv.slice(2);
const { result: { tools } } = await rpc('tools/list', {});
console.log('tools:', tools.map(t => t.name).join(', '));
const res = await rpc('tools/call', { name: 'generate_song_idea', arguments: { name, theme, language: 'en' } }, 2);
console.log(res.result.content[0].text);
