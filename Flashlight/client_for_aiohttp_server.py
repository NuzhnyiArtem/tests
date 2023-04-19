import aiohttp
import asyncio
from typing import Dict



class Flashlight:
    commands = {"on": 'turn_on', "off": 'turn_off', "color": 'change_color'}
    colors = {1: "white", 2: "red", 3: "blue", 4: "green"}

    def __init__(self, status: int=0, color: int=1) -> None:
        self.status = status
        self.color = self.colors[color]

    async def command_accept(self, command: str, metadata: int=None) -> None:
        if command in self.commands:
            method_name = self.commands[command]
            method = getattr(self, method_name)
            if metadata is None:
                method()
            else:
                method(metadata)
        else:
            pass

    def turn_on(self) -> None:
        if self.status == 0:
            self.status = 1
            print(f"Фонарь включен, установлен цвет: {self.color}")
        else:
            print("Фонарь уже включен")

    def turn_off(self) -> None:
        if self.status == 1:
            self.status = 0
            print("Фонарь выключен")
        else:
            print("Фонарь не включен")

    def change_color(self, metadata) -> None:
        if self.status == 1 and self.color != self.colors[metadata]:
            self.color = self.colors[metadata]
            print(f"Выставлен {self.color} цвет")
        elif self.status != self.colors[metadata]:
            print(f"Цвет {self.color} уже выставлен")
        else:
            print("Фонарь не включен")


async def processing_messages(message: Dict, flashlight) -> None:
    try:
        command = message.get("command").lower()
        metadata = message.get("metadata")
        await flashlight.command_accept(command, metadata)
    except Exception as e:
        print(e)


async def main():
    while True:
        host = input("input address ") or "127.0.0.1"
        port = int(input("input port ") or 9999)
        if not (0 < port < 65535):
            print("Указан неверный порт")
        break

    flashlight = Flashlight()
    session = aiohttp.ClientSession()
    while True:
        try:
            async with session.ws_connect(f'ws://{host}:{port}/echo') as ws:
                await ws.send_str(input("Input message "))
                async for msg in ws:
                    if msg.type == aiohttp.WSMsgType.TEXT:
                        message = msg.json()
                        await processing_messages(message, flashlight)
                    elif msg.type == aiohttp.WSMsgType.ERROR:
                        print(ws.exception())
                        break
        except Exception as e:
            print(e)

asyncio.run(main())