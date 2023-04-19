from aiohttp import web
import asyncio
import aiohttp
from aiohttp.http_websocket import WSCloseCode, WSMessage
from aiohttp.web_request import Request

async def ws_echo(request):
    ws = web.WebSocketResponse(autoclose=False, timeout=0.1)
    await ws.prepare(request)
    async for msg in ws:
        if msg.type == web.WSMsgType.text:
            await ws.send_str(msg.data)
            print(msg.data)
            return ws


app = web.Application()
app.add_routes([web.get('/echo', handler=ws_echo)])

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    web.run_app(app, host="127.0.0.1", port=9998, handle_signals=False)