import unittest

import raftos


class TestConfiguration(unittest.TestCase):
    def test_configure(self):
        raftos.configure({
            'log_path': '/test_path/',
            'serializer': 'TestSerializer'
        })

        self.assertEqual(raftos.config.log_path, '/test_path/')
        self.assertEqual(raftos.config.serializer, 'TestSerializer')


if __name__ == '__main__':
    unittest.main()
