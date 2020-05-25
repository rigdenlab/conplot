from enum import Enum
import json
import components
from dash import no_update
from components import EmailIssueReference
from loaders import MandatoryDatasetReference
from utils import slack_utils, decompress_data


class DatasetIndex(Enum):
    sequence = 0
    contact = 1


class ButtonActions(Enum):
    delete = 1
    load = 2
    share = 3
    stop = 4



def toggle_selection_alert(format_selection):
    if format_selection is not None:
        return None, False
    else:
        return 'danger', True


def get_remove_trigger(trigger):
    is_open = trigger['value']
    prop_id = json.loads(trigger['prop_id'].replace('.is_open', ''))
    index = json.loads(prop_id['index'])
    fname = index[0]
    dataset = index[1]
    return fname, dataset, is_open


def remove_unused_fname_alerts(falerts):
    new_falerts = []
    for alert in falerts:
        if 'is_open' not in alert['props'].keys():
            new_falerts.append(alert)
        elif alert['props']['is_open']:
            new_falerts.append(alert)
    return new_falerts


def get_upload_id(trigger, fnames, fcontents):
    fname = trigger['value']
    prop_id = json.loads(trigger['prop_id'].replace('.filename', ''))
    dataset = prop_id['index']
    index = DatasetIndex.__getattr__(dataset).value
    fcontent = fcontents[index]

    return dataset, fname, fcontent, index


def ensure_triggered(trigger):
    prop_id = trigger['prop_id']
    value = trigger['value']
    if prop_id == '.' or value is None:
        return False
    else:
        return True


def toggle_alert(value):
    if value == EmailIssueReference.BUG.value:
        return components.ContactBugAlert(), False
    elif value == EmailIssueReference.FORGOT_PSSWRD.value:
        return components.ContactForgotPsswrdAlert(), False
    elif value == EmailIssueReference.OTHER.value:
        return None, False
    else:
        return None, True


def get_session_action(trigger):
    prop_id = json.loads(trigger['prop_id'].replace('.n_clicks', ''))
    action = ButtonActions.__getattr__(prop_id['type'].split('-')[0])
    return prop_id['index'], action


def submit_form(name, email, subject, description, logger):
    if not name or not email or not description or not subject:
        return components.InvalidContactFormModal()
    elif slack_utils.send_slack_message(name, email, subject, description, logger):
        return components.SuccessContactFormModal()
    else:
        return components.SlackConnectionErrorModal()


def update_fname_alerts(session_id, enumerator, cache):
    fname_alerts = []
    for idx, dataset in enumerate(enumerator):
        if cache.hexists(session_id, dataset.value):
            fname = decompress_data(cache.hget(session_id, dataset.value)).pop(-1)
            fname_alerts.append(components.FilenameAlert(fname, dataset.value))
    if enumerator == MandatoryDatasetReference:
        return fname_alerts + [no_update for x in range(0, 2 - len(fname_alerts))]
    elif not fname_alerts:
        return no_update

    return fname_alerts
