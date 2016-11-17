import unittest

import raftos


class TestConfiguration(unittest.TestCase):
    def test_configure(self):
        raftos.configure({
            'log_path': '/test_path/',
            'serializer': 'TestSerializer',
            'secret_key': b'raftos test secret key',
            'salt': b'raftos test salt'
        })

        self.assertEqual(raftos.config.log_path, '/test_path/')
        self.assertEqual(raftos.config.serializer, 'TestSerializer')
        self.assertEqual(raftos.config.secret_key, b'raftos test secret key',)
        self.assertEqual(raftos.config.salt, b'raftos test salt')


if __name__ == '__main__':
    unittest.main()
