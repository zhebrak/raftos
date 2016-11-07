# raftos

[![Build Status](https://travis-ci.org/zhebrak/django-statsy.svg)](https://travis-ci.org/zhebrak/django-statsy)

Replication framework based on [Raft Algorithm](https://raft.github.io/) for fault-tolerant distributed systems.

![](https://raw.github.com/zhebrak/raftos/master/docs/img/raft_rsm.png)



```python
import raftos


class Class:
    data = raftos.Replicated(name='data')


raftos.register(
    # node running on this machine
    '127.0.0.1:8000',

    # other servers
    cluster=[
        '127.0.0.1:8001',
        '127.0.0.1:8002'
    ]
)

obj = Class()

# data value on a leader gets replicated to all followers (more in examples)
obj.data = {
    'id': 337,
    'data': {
        'amount': 20000,
        'created_at': '7/11/16 18:45'
    }
}

```


[Paper](https://raft.github.io/raft.pdf) & [Video](https://www.youtube.com/watch?v=YbZ3zDzDnrw)
