from .state import State


class Replicated:
    """Replication descriptor makes sure data changes are all applied to State Machine"""

    def __init__(self, name, default=None):
        self.name = name
        self.value = default

        self.in_memory = False

    def __get__(self, obj, obj_type):

        # If we didn't set a value in this life cycle try to get it from State Machine
        if not self.in_memory:
            try:
                self.value = State.get_value(self.get_name(obj))
            except KeyError:
                pass

        return self.value

    def __set__(self, obj, value):
        State.set_value(self.get_name(obj), value)

        self.value = value
        self.in_memory = True

    def get_name(self, obj):
        return '{}.{}'.format(obj.__class__.__name__, self.name)
