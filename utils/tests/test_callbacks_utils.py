import unittest
from Bio.Alphabet.IUPAC import protein
from utils import callback_utils, get_hydrophobicity


class CallbacksTestCase(unittest.TestCase):

    def test_1(self):
        self.assertTupleEqual(('danger', True), callback_utils.toggle_selection_alert(None))
        self.assertTupleEqual((None, False), callback_utils.toggle_selection_alert('DUMMY'))
        self.assertTupleEqual((None, False), callback_utils.toggle_alert('3'))
        self.assertTupleEqual((None, True), callback_utils.toggle_alert(None))

    def test_2(self):
        test_input = [{'props': {'is_open': True}, 'dummy_1': {'dummy_1': 'dummy_1'}},
                      {'props': {'dummy_2': True}, 'dummy_2': {'dummy_2': 'dummy_2'}},
                      {'props': {'is_open': False}, 'dummy_3': {'dummy_3': 'dummy_3'}}]
        expected_output = [{'props': {'is_open': True}, 'dummy_1': {'dummy_1': 'dummy_1'}},
                           {'props': {'dummy_2': True}, 'dummy_2': {'dummy_2': 'dummy_2'}}]

        self.assertListEqual(expected_output, callback_utils.remove_unused_fname_alerts(test_input))

    def test_3(self):
        test_input = {'prop_id': '{"index":"[\\"dummy_fname\\", \\"sequence\\"]","type":"filename-alert"}.is_open',
                      'value': True}
        expected_output = ('dummy_fname', 'sequence', True)

        self.assertTupleEqual(expected_output, callback_utils.get_remove_trigger(test_input))

    def test_4(self):
        test_input = {'prop_id': 'dummy_id', 'value': 'dummy_value'}
        self.assertTrue(callback_utils.ensure_triggered(test_input))
        test_input = {'prop_id': '.', 'value': 'dummy_value'}
        self.assertFalse(callback_utils.ensure_triggered(test_input))
        test_input = {'prop_id': 'dummy_id', 'value': None}
        self.assertFalse(callback_utils.ensure_triggered(test_input))

    def test_5(self):
        test_trigger = {'prop_id': '{"index":"contact","type":"upload-button"}.filename', 'value': 'dummy_fname'}
        test_fnames = ['dummy', 'dummy_fname']
        test_fcontents = [None, 'dummy_fcontents']
        expected_output = ('contact', 'dummy_fname', 'dummy_fcontents', 1)

        self.assertTupleEqual(expected_output, callback_utils.get_upload_id(test_trigger, test_fnames, test_fcontents))

    def test_6(self):
        expected = [0.33, 0.22, 0.5, 0.12, -0.58, 1.14, -0.06, -0.81, 1.81, -0.69, -0.44, 0.43, -0.31, 0.19, 1.0, 0.33,
                    0.11, -0.53, -0.24, 0.23]
        seq = protein.letters
        self.assertListEqual(expected, get_hydrophobicity(seq))
