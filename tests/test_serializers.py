import unittest

import raftos


class TestSerializers(unittest.TestCase):
    def setUp(self):
        self.serializers = [
            raftos.serializers.JSONSerializer,
            raftos.serializers.MessagePackSerializer
        ]

    def _test_pack_unpack(self, test_data):
        for serializer in self.serializers:
            for data in test_data:
                packed = serializer.pack(data)
                self.assertEqual(data, serializer.unpack(packed))

    def test_int(self):
        self._test_pack_unpack([-1, 0, 1, 10 ** 3])

    def test_string(self):
        self._test_pack_unpack(['', 'test string', 'big_string' * 10])

    def test_list(self):
        self._test_pack_unpack([
            [], list(range(10)), list(range(10 ** 3)),
            [1, 'string', []]
        ])

    def test_dict(self):
        # JSON does not allow integer keys!
        self._test_pack_unpack([
            {}, {'1': 1, '2': 2},
            {str(key): key for key in range(10 ** 3)}
        ])


if __name__ == '__main__':
    unittest.main()
