from .state import State


class Replicated:
    """Replication descriptor makes sure data changes are all applied to State Machine"""

    def __init__(self, name, default=None):
        self.name = name
        self.value = default

        self.is_replicated = False

    def __get__(self, obj, obj_type):

        # If we didn't set a value in this life cycle try to get it from State Machine
        if not self.is_replicated:
            try:
                self.value = State.get_value(self.name)
            except KeyError:
                pass

        return self.value

    def __set__(self, obj, value):
        State.set_value(self.name, value)

        self.value = value
        self.is_replicated = True
