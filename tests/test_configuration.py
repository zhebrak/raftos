import unittest

import raftos


class TestConfiguration(unittest.TestCase):
    def test_configure(self):
        raftos.configure({
            'log_path': '/test_path/',
            'serializer': 'TestSerializer',
            'heartbeat_interval': 0.2,
            'election_interval': (0.8, 2)
        })

        self.assertEqual(raftos.config.log_path, '/test_path/')
        self.assertEqual(raftos.config.serializer, 'TestSerializer')
        self.assertEqual(raftos.config.heartbeat_interval, 0.2)
        self.assertEqual(raftos.config.election_interval, (0.8, 2))


if __name__ == '__main__':
    unittest.main()
