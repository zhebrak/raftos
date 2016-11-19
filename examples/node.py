import argparse
import asyncio
from datetime import datetime
import random

import raftos


class Class:
    data = raftos.Replicated(name='data')


def run(node_id):
    obj = Class()
    loop = asyncio.get_event_loop()

    while True:
        loop.run_until_complete(asyncio.sleep(5))

        if raftos.get_leader() == node_id:
            obj.data = {
                'id': random.randint(1, 1000),
                'data': {
                    'amount': random.randint(1, 1000) * 1000,
                    'created_at': datetime.now().strftime('%d/%m/%y %H:%M')
                }
            }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--node')
    parser.add_argument('--cluster')
    args = parser.parse_args()

    cluster = ['127.0.0.1:{}'.format(port) for port in args.cluster.split()]
    node = '127.0.0.1:{}'.format(args.node)

    raftos.configure({
        'log_path': './',
        'serializer': raftos.serializers.JSONSerializer
    })

    raftos.register(node, cluster=cluster)
    run(node)
