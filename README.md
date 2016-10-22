# raftos

Replication framework based on [Raft Algorithm](https://raft.github.io/) for fault-tolerant distributed systems.

![](https://raw.github.com/zhebrak/raftos/master/docs/img/raft_rsm.png)



```python
import raftos


class MyClass:
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

```


[Paper](https://raft.github.io/raft.pdf) & [Video](https://www.youtube.com/watch?v=YbZ3zDzDnrw)
