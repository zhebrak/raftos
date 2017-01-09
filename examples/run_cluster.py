#!/usr/bin/bin python3
import os
import logging
import asyncio
import random
import raftos
import raftos.serializers
from argparse import ArgumentParser
from datetime import datetime
from multiprocessing import Process


logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


class Class:
    data = raftos.Replicated(name='data')


def main(log_dir, node, cluster):
    loop = asyncio.new_event_loop()

    raftos.configure({
        'log_path': log_dir,
        'serializer': raftos.serializers.JSONSerializer,
        'loop': loop
    })

    loop.run_until_complete(run(loop, node, cluster))


async def run(loop, node, cluster):
    await raftos.register(node, cluster=cluster, loop=loop)

    obj = Class()

    while True:
        await asyncio.sleep(5, loop=loop)

        if raftos.get_leader() == node:
            obj.data = {
                'id': random.randint(1, 1000),
                'data': {
                    'amount': random.randint(1, 1000) * 1000,
                    'created_at': datetime.now().strftime('%d/%m/%y %H:%M')
                }
            }


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('-p', '--start-port', help='Start port', type=int, default=8000)
    parser.add_argument('-n', '--processes', help='Cluster size', type=int, default=3)
    parser.add_argument('-d', '--log-dir', default=os.path.abspath('logs'),
                        dest='log_dir', help="Log dir")

    args = parser.parse_args()

    os.makedirs(args.log_dir, exist_ok=True)

    neighbours = set(
        "127.0.0.1:{}".format(args.start_port + i) for i in range(args.processes)
    )

    processes = set([])

    try:
        for neighbour in neighbours:
            node_args = (args.log_dir, neighbour, neighbours - {neighbour})
            p = Process(target=main, args=node_args)
            log.info("%r", node_args)

            p.start()
            processes.add(p)

        while processes:
            for process in tuple(processes):
                process.join()
                processes.remove(process)
    finally:
        for process in processes:
            if process.is_alive():
                log.warning('Terminating %r', process)
                process.terminate()
