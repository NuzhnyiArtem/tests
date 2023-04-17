import aiohttp
import asyncio
import websockets

async def responce(websocket, path):
    message = await websocket.recv()
    print(f"we got msg: {message}")
    await websocket.send(message)


start_server = websockets.serve(responce, "127.0.0.1", 9999)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()