import argparse
import asyncio
import random

import raftos


class MyClass:
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

    my_obj = MyClass()
    while True:
        number = random.randint(1, 1000)

        try:
            my_obj.data = number
        except raftos.state.NotALeaderException:
            pass

        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.sleep(10))
