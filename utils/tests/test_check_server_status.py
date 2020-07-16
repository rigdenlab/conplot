import unittest
from utils import check_server_status


class CheckServerStatusTestCase(unittest.TestCase):

    def test_1(self):
        logs = b'[2020-07-16 15:59:36 +0000] [1] [INFO] Starting gunicorn 20.0.4\n[2020-07-16 15:59:36 +0000] [1] ' \
               b'[INFO] Listening at: http://0.0.0.0:80 (1)\n[2020-07-16 15:59:36 +0000] [1] [INFO] Using worker: ' \
               b'threads\n[2020-07-16 15:59:36 +0000] [9] [INFO] Booting worker with pid: 9\n[2020-07-16 15:59:36 ' \
               b'+0000] [10] [INFO] Booting worker with pid: 10\n[2020-07-16 15:59:36 +0000] [11] [INFO] Booting ' \
               b'worker with pid: 11\n[2020-07-16 15:59:36 +0000] [12] [INFO] Booting worker with pid: 12\n[2020-07' \
               b'-16 15:59:36 +0000] [13] [INFO] Booting worker with pid: 13\n[2020-07-16 16:02:06 +0000] [12] ' \
               b'[ERROR] Redis connection error! Error -2 connecting to redis_db:6379. Name or service not known.\n' \
               b'[2020-07-16 16:02:06 +0000] [13] [ERROR] Redis connection error! Error -2 connecting to redis_db:637' \
               b'9. Name or service not known.\n[2020-07-16 16:02:06 +0000] [10] [ERROR] Redis connection error! Erro' \
               b'r -2 connecting to redis_db:6379. Name or service not known.\n[2020-07-16 16:02:06 +0000] [11] [ERRO' \
               b'R] Redis connection error! Error -2 connecting to redis_db:6379. Name or service not known.\n[2020-0' \
               b'7-16 16:02:06 +0000] [9] [ERROR] Redis connection error! Error -2 connecting to redis_db:6379. Name ' \
               b'or service not known.\n[2020-07-16 16:02:13 +0000] [12] [ERROR] Redis connection error! Error -2 con' \
               b'necting to redis_db:6379. Name or service not known.\n'
        expected_errors = ['[2020-07-16 16:02:06 +0000] [12] [ERROR] Redis connection error! Error -2 connecting to '
                           'redis_db:6379. Name or service not known.',
                           '[2020-07-16 16:02:06 +0000] [13] [ERROR] Redis connection error! Error -2 connecting to '
                           'redis_db:6379. Name or service not known.',
                           '[2020-07-16 16:02:06 +0000] [10] [ERROR] Redis connection error! Error -2 connecting to '
                           'redis_db:6379. Name or service not known.',
                           '[2020-07-16 16:02:06 +0000] [11] [ERROR] Redis connection error! Error -2 connecting to '
                           'redis_db:6379. Name or service not known.',
                           '[2020-07-16 16:02:06 +0000] [9] [ERROR] Redis connection error! Error -2 connecting to '
                           'redis_db:6379. Name or service not known.',
                           '[2020-07-16 16:02:13 +0000] [12] [ERROR] Redis connection error! Error -2 connecting to '
                           'redis_db:6379. Name or service not known.']
        errors, criticals, warnings, tracebacks = check_server_status.parse_logs(logs)
        self.assertListEqual(expected_errors, errors)
        self.assertListEqual([], warnings)
        self.assertListEqual([], tracebacks)

    def test_2(self):
        logs = b'[2020-07-16 15:59:36 +0000] [1] [INFO] Starting gunicorn 20.0.4\n[2020-07-16 15:59:36 +0000] [1] ' \
               b'[INFO] Listening at: http://0.0.0.0:80 (1)\n[2020-07-16 15:59:36 +0000] [1] [INFO] Using worker: ' \
               b'threads\n[2020-07-16 15:59:36 +0000] [9] [INFO] Booting worker with pid: 9\n[2020-07-16 15:59:36 +0' \
               b'000] [10] [INFO] Booting worker with pid: 10\n[2020-07-16 15:59:36 +0000] [11] [INFO] Booting worke' \
               b'r with pid: 11\n[2020-07-16 15:59:36 +0000] [12] [INFO] Booting worker with pid: 12\n[2020-07-16 15' \
               b':59:36 +0000] [13] [INFO] Booting worker with pid: 13\n[2020-07-16 16:02:06 +0000] [12] [ERROR] Red' \
               b'is connection error! Error -2 connecting to redis_db:6379. Name or service not known.\n[2020-07-16 ' \
               b'16:02:06 +0000] [13] [ERROR] Redis connection error! Error -2 connecting to redis_db:6379. Name or ' \
               b'service not known.\n[2020-07-16 16:02:06 +0000] [10] [ERROR] Redis connection error! Error -2 conne' \
               b'cting to redis_db:6379. Name or service not known.\n[2020-07-16 16:02:06 +0000] [11] [ERROR] Redis ' \
               b'connection error! Error -2 connecting to redis_db:6379. Name or service not known.\n[2020-07-16 16:' \
               b'02:06 +0000] [9] [ERROR] Redis connection error! Error -2 connecting to redis_db:6379. Name or serv' \
               b'ice not known.\n[2020-07-16 16:02:13 +0000] [12] [ERROR] Redis connection error! Error -2 connectin' \
               b'g to redis_db:6379. Name or service not known.\nTraceback (most recent call last):\n File "/usr/loc' \
               b'al/lib/python3.8/site-packages/flask/app.py", line 2447, in wsgi_app\n  response = self.full_dispat' \
               b'ch_request()\n File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1952, in full_dispa' \
               b'tch_request\n  rv = self.handle_user_exception(e)\n File "/usr/local/lib/python3.8/site-packages/fl' \
               b'ask/app.py", line 1821, in handle_user_exception\n  reraise(exc_type, exc_value, tb)\n File "/usr/l' \
               b'ocal/lib/python3.8/site-packages/flask/_compat.py", line 39, in reraise\n  raise value\n File "/usr' \
               b'/local/lib/python3.8/site-packages/flask/app.py", line 1950, in full_dispatch_request\n  rv = self.' \
               b'dispatch_request()\n File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 1936, in disp' \
               b'atch_request\n  return self.view_functions[rule.endpoint](**req.view_args)\n File "/usr/local/lib/p' \
               b'ython3.8/site-packages/dash/dash.py", line 967, in dispatch\n  response.set_data(func(*args, output' \
               b's_list=outputs_list))\n File "/usr/local/lib/python3.8/site-packages/dash/dash.py", line 902, in ad' \
               b'd_context\n  output_value = func(*args, **kwargs)  # %% callback invoked %%\n File "/home/filo/Pych' \
               b'armProjects/conplot/app.py", line 281, in upload_contact\n  return data_utils.upload_dataset(fname,' \
               b' fcontent, input_format, fname_alerts, session_id, cache, app.logger,\n File "/home/filo/PycharmPro' \
               b'jects/conplot/utils/data_utils.py", line 39, in upload_dataset\n  data, invalid = loaders.Loader(fc' \
               b'ontent, input_format)\n File "/home/filo/PycharmProjects/conplot/loaders/__init__.py", line 38, in ' \
               b'Loader\n  return Loader(*args, **kwargs)\n File "/home/filo/PycharmProjects/conplot/loaders/loader.' \
               b'py", line 15, in Loader\n  data_raw = ParserFormats.__dict__[input_format](decoded, input_format)\n' \
               b' File "/home/filo/PycharmProjects/conplot/parsers/__init__.py", line 37, in CCMpredParser\n  return' \
               b' CCMpredParser(*args, **kwargs)\nTypeError: CCMpredParser() takes 1 positional argument but 2 w' \
               b'ere given\n[2020-07-16 16:02:06 +0000] [13] [ERROR] Redis connection error! Error -2 connecting to ' \
               b'redis_db:6379. Name or service not known.'
        expected_errors = ['[2020-07-16 16:02:06 +0000] [12] [ERROR] Redis connection error! Error -2 connecting to '
                           'redis_db:6379. Name or service not known.',
                           '[2020-07-16 16:02:06 +0000] [13] [ERROR] Redis connection error! Error -2 connecting to '
                           'redis_db:6379. Name or service not known.',
                           '[2020-07-16 16:02:06 +0000] [10] [ERROR] Redis connection error! Error -2 connecting to '
                           'redis_db:6379. Name or service not known.',
                           '[2020-07-16 16:02:06 +0000] [11] [ERROR] Redis connection error! Error -2 connecting to '
                           'redis_db:6379. Name or service not known.',
                           '[2020-07-16 16:02:06 +0000] [9] [ERROR] Redis connection error! Error -2 connecting to '
                           'redis_db:6379. Name or service not known.',
                           '[2020-07-16 16:02:13 +0000] [12] [ERROR] Redis connection error! Error -2 connecting to '
                           'redis_db:6379. Name or service not known.',
                           '[2020-07-16 16:02:06 +0000] [13] [ERROR] Redis connection error! Error -2 connecting to '
                           'redis_db:6379. Name or service not known.', ]
        expected_tracebacks = ['Traceback (most recent call last):\n[...]\nTypeError: CCMpredParser() takes 1 '
                               'positional argument but 2 were given\n']
        errors, criticals, warnings, tracebacks = check_server_status.parse_logs(logs)
        self.assertListEqual(expected_errors, errors)
        self.assertListEqual([], warnings)
        self.assertListEqual(expected_tracebacks, tracebacks)
