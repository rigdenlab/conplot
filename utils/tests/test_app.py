import os
import unittest
from app import app, redis_url


class AppTestCase(unittest.TestCase):

    def test_1(self):
        stylesheets = ['https://stackpath.bootstrapcdn.com/bootswatch/4.4.1/lux/bootstrap.min.css',
                       'https://use.fontawesome.com/releases/v5.7.2/css/all.css']
        self.assertEqual('ConPlot', app.title)
        self.assertListEqual(stylesheets, app.config['external_stylesheets'])
        self.assertEqual(13, len(app.callback_map))
        self.assertEqual("redis://localhost:6379", os.environ['REDISCLOUD_URL'])

    def test_2(self):
        self.assertEqual('localhost', redis_url.hostname)
        self.assertIsNone(redis_url.password)
        self.assertEqual(6379, redis_url.port)


if __name__ == '__main__':
    unittest.main()
