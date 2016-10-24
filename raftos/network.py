import asyncio

from .log import logger
from .conf import config


class UDPProtocol(asyncio.DatagramProtocol):
    def __init__(self, queue, request_handler, serializer=None):
        self.queue = queue
        self.serializer = serializer or config.serializer
        self.request_handler = request_handler

    def __call__(self):
        return self

    async def start(self):
        while not self.transport.is_closing():
            data, destination = await self.queue.get()
            self.transport.sendto(self.serializer.pack(data), destination)

    def connection_made(self, transport):
        self.transport = transport
        asyncio.ensure_future(self.start())

    def datagram_received(self, data, sender):
        data = self.serializer.unpack(data)
        data.update({
            'sender': sender
        })
        self.request_handler(data)

    def error_received(self, exc):
        logger.error('Error received {}'.format(exc))

    def connection_lost(self, exc):
        logger.error('Connection lost {}'.format(exc))
