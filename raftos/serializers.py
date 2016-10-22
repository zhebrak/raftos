import json


class JSONSerializer:
    @staticmethod
    def pack(data):
        return json.dumps(data).encode()

    @staticmethod
    def unpack(data):
        decoded = data.decode() if isinstance(data, bytes) else data
        return json.loads(decoded)
