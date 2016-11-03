import asyncio
import functools

from .network import UDPProtocol
from .state import State


def register(*address_list, cluster=None):
    """Start Raft node (server)
    Args:
        address_list — 127.0.0.1:8000 [, 127.0.0.1:8001 ...]
        cluster — [127.0.0.1:8001, 127.0.0.1:8002, ...]
    """

    for address in address_list:
        host, port = address.split(':')
        node = Node(address=(host, int(port)))
        node.start()

        for address in cluster:
            host, port = address.split(':')
            port = int(port)

            if (host, port) != (node.host, node.port):
                node.update_cluster((host, port))


def stop():
    for node in Node.nodes:
        node.stop()


class Node:
    """Raft Node (Server)"""

    nodes = []

    def __init__(self, address):
        self.host, self.port = address
        self.cluster = set()

        self.requests = asyncio.Queue()
        self.state = State(self)

        self.loop = asyncio.get_event_loop()

        self.__class__.nodes.append(self)

    def start(self):
        protocol = UDPProtocol(queue=self.requests, request_handler=self.request_handler)
        address = self.host, self.port
        task = asyncio.Task(self.loop.create_datagram_endpoint(protocol, local_addr=address))
        self.transport, _ = self.loop.run_until_complete(task)
        self.state.start()

    def stop(self):
        self.state.stop()
        self.transport.close()

    def update_cluster(self, address_list):
        self.cluster.update({address_list})

    @property
    def cluster_count(self):
        return len(self.cluster)

    def request_handler(self, data):
        self.state.request_handler(data)

    async def send(self, data, destination):
        """Sends data to destination Node
        Args:
            data — serializable object
            destination — <str> '127.0.0.1:8000' or <tuple> (127.0.0.1, 8000)
        """
        if isinstance(destination, str):
            host, port = destination.split(':')
            destination = host, int(port)

        await self.requests.put((data, destination))

    def broadcast(self, data):
        """Sends data to all Nodes in cluster (cluster list does not contain self Node)"""
        for destination in self.cluster:
            asyncio.ensure_future(self.send(data, destination))
