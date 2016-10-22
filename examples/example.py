import random
import time

import raftos


class MyClass:
    data = raftos.Replicated(name='data')


if __name__ == '__main__':
    cluster = [
        '127.0.0.1:8000',
        '127.0.0.1:8001',
        '127.0.0.1:8002'
    ]

    # Here we run all nodes on one computer; normally you would want to do it like this:
    # raftos.register('127.0.0.1:8000', cluster=cluster)

    raftos.register(*cluster, cluster=cluster)

    my_obj = MyClass()
    while True:
        number = random.randint(1, 1000)

        print('setting data to: ', number)
        my_obj.data = number
        print('data is: ', my_obj.data)

        time.sleep(1)
