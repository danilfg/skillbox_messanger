import asyncio
from asyncio import transports
from typing import Optional


class ServerProtocol(asyncio.Protocol):
    login: str
    server: 'Server'
    transport: transports.BaseTransport

    def __init__(self, server: 'Server'):
        self.server = server

    def data_received(self, data: bytes):
        print(data)

    def connection_made(self, transport: transports.BaseTransport):
        self.server.clients.append(self)
        self.transport = transport

        print("Пришел новый клиент")

    def connection_lost(self, exc: Optional[Exception]):
        self.server.clients.remove(self)

        print("Клиент вышел")


class Server:
    clients: list

    def __init__(self):
        self.clients = []

    def build_protocol(self):
        return ServerProtocol(self)
    async def start(self):
        loop = asyncio.get_running_loop()

        coroutine = await loop.create_server(
            self.build_protocol,
            '127.0.0.1',
            9999
        )

        print("Сервер запущен ...")

        await coroutine.serve_forever()


process = Server()
try:
    asyncio.run(process.start())
except KeyboardInterrupt:
    print("Сервер остановлен вручную")