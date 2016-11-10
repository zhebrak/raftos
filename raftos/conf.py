from .serializers import JSONSerializer


class Configuration:
    def __init__(self):
        self.configure(self.default_settings())

    @staticmethod
    def default_settings():
        return {
            'serializer': JSONSerializer,
            'log_path': '/var/log/raftos/',
            'heartbeat_interval': 0.5,
            'election_interval': (2, 4)
        }

    def configure(self, kwargs):
        for param, value in kwargs.items():
            setattr(self, param.lower(), value)


config = Configuration()
configure = config.configure
