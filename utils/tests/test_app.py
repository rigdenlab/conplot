import unittest
from app import app


class AppTestCase(unittest.TestCase):

    def test_1(self):
        stylesheets = ['https://stackpath.bootstrapcdn.com/bootswatch/4.4.1/lux/bootstrap.min.css',
                       'https://use.fontawesome.com/releases/v5.7.2/css/all.css']
        self.assertEqual('ConPlot', app.title)
        self.assertListEqual(stylesheets, app.config['external_stylesheets'])


if __name__ == '__main__':
    unittest.main()
