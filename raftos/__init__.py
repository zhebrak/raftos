from .conf import configure, config
from .replicator import Replicated
from .server import register, stop
from .state import State, Leader


__all__ = [
    'Replicated',

    'config',
    'configure',
    'register',
    'stop',

    'get_leader'
]


def get_leader():
    leader = State.leader
    if isinstance(leader, Leader):
        return leader.id

    return leader
