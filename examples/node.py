import argparse
import asyncio
from datetime import datetime
import random

import raftos


class Class:
    data = raftos.Replicated(name='data')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--node')
    parser.add_argument('--cluster')
    args = parser.parse_args()

    cluster = ['127.0.0.1:{}'.format(port) for port in args.cluster.split()]
    node = '127.0.0.1:{}'.format(args.node)

    raftos.configure({
        'log_path': './'
    })
    raftos.register(node, cluster=cluster)

    obj = Class()
    while True:
        try:
            obj.data = {
                'id': random.randint(1, 1000),
                'data': {
                    'amount': random.randint(1, 1000) * 1000,
                    'created_at': datetime.now().strftime('%d/%m/%y %H:%M')
                }
            }
        except raftos.state.NotALeaderException:
            """Redirect request to raftos.get_leader()"""

        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.sleep(10))
