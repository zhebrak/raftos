from .conf import configure, config
from .replicator import Replicated
from .server import register, stop
from .state import State


__all__ = [
    'Replicated',

    'config',
    'configure',
    'register',
    'stop',

    'leader'
]

leader = State.leader
