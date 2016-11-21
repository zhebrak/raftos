# raftos

[![Build Status](https://travis-ci.org/zhebrak/raftos.svg)](https://travis-ci.org/zhebrak/raftos) [![PyPI version](https://badge.fury.io/py/raftos.svg)](http://badge.fury.io/py/raftos)

Asynchronous replication framework based on [Raft Algorithm](https://raft.github.io/) for fault-tolerant distributed systems.

![](https://raw.github.com/zhebrak/raftos/master/docs/img/raft_rsm.png)

#### Install

```
pip install raftos
```

#### Register nodes on every server

```python
import raftos


loop.create_task(
    raftos.register(
        # node running on this machine
        '127.0.0.1:8000',

        # other servers
        cluster=[
            '127.0.0.1:8001',
            '127.0.0.1:8002'
        ]
    )
)
loop.run_forever()
```

#### Data replication

```python
counter = raftos.Replicated(name='counter')
data = raftos.ReplicatedDict(name='data')


# value on a leader gets replicated to all followers
await counter.set(42)
await data.update({
    'id': 337,
    'data': {
        'amount': 20000,
        'created_at': '7/11/16 18:45'
    }
})
```

#### In case you only need consensus algorithm with leader election

```python
await raftos.wait_until_leader(current_node)
```
or
```python
if raftos.get_leader() == current_node:
    # make request or respond to a client
```
or
```python
raftos.configure({
    'on_leader': start,
    'on_follower': stop
})
```

Whenever the leader falls, someone takes its place.


[Paper](https://raft.github.io/raft.pdf) & [Video](https://www.youtube.com/watch?v=YbZ3zDzDnrw)
