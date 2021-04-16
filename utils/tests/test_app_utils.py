from app import app
import components
from dash.dash import no_update
import json
import keydb
import logging
import plotly
import unittest
from utils import app_utils, keydb_utils, session_utils, cache_utils


class AppTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        keydb_pool = keydb_utils.create_pool('redis://127.0.0.1:6379')
        cls.cache = keydb.KeyDB(connection_pool=keydb_pool)
        cls.session_id = session_utils.initiate_session(cls.cache, logging.getLogger())

    def test_1(self):
        stylesheets = ['https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/lux/bootstrap.min.css',
                       'https://use.fontawesome.com/releases/v5.7.2/css/all.css']
        self.assertEqual('ConPlot', app.title)
        self.assertListEqual(stylesheets, app.config['external_stylesheets'])

    def test_2(self):
        expected_output = components.InvalidPasswordRecoverAccount()
        expected_output = json.loads(json.dumps(expected_output, cls=plotly.utils.PlotlyJSONEncoder))
        output = app_utils.recover_account('username', 'email', 'secret', 'password_1', 'password_2', None)
        output = json.loads(json.dumps(output, cls=plotly.utils.PlotlyJSONEncoder))
        self.assertDictEqual(expected_output, output)

    def test_3(self):
        expected_output = [components.SuccessLogoutAlert(), components.UserPortalCardBody(None)]
        expected_output = [json.loads(json.dumps(x, cls=plotly.utils.PlotlyJSONEncoder)) for x in expected_output]
        expected_cache = {b'id': cache_utils.compress_data(self.session_id)}
        cache_utils.store_fname(self.cache, self.session_id, 'dummy_fname_1', 'contact')
        self.cache.hset(self.session_id, 'user', 'username')
        self.cache.hset(self.session_id, 'session_pkid', '123')

        test_log = logging.getLogger('test_3_log')
        output = app_utils.user_logout(self.session_id, self.cache, test_log)
        self.assertEqual(output[0], no_update)
        output = [json.loads(json.dumps(x, cls=plotly.utils.PlotlyJSONEncoder)) for x in output[1:]]
        self.assertListEqual(output, expected_output)
        self.assertDictEqual(expected_cache, self.cache.hgetall(self.session_id))


if __name__ == '__main__':
    unittest.main()
