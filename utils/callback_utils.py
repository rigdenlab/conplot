from enum import Enum
import json
import components
from dash import no_update
from components import EmailIssueReference
from loaders import DatasetReference, AdditionalDatasetReference
from utils import slack_utils, decompress_data, cache_utils, email_utils, postgres_utils


class DatasetIndex(Enum):
    sequence = 0
    contact = 1


class ButtonActions(Enum):
    delete = 1
    load = 2
    share = 3
    stop = 4


def toggle_modal(trigger):
    if not ensure_triggered(trigger):
        return no_update
    return True


def toggle_createuserbutton(trigger, disabled):
    if not ensure_triggered(trigger):
        return no_update
    return not disabled


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


def is_user_login(trigger):
    prop_id = json.loads(trigger['prop_id'].replace('.n_clicks', ''))
    index = prop_id['idx']
    if index == 'login':
        return True
    else:
        return False


def remove_unused_fname_alerts(falerts):
    new_falerts = []

    if falerts is None:
        return new_falerts

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

    elif subject != EmailIssueReference.FORGOT_PSSWRD.value:
        slack_success = slack_utils.user_get_in_touch(name, email, subject, description, logger)
        if not slack_success:
            return components.SlackConnectionErrorModal()
        return components.SuccessContactFormModal()

    else:
        secret = postgres_utils.activate_recovery_mode(name, email)
        if secret is None:
            return components.ContactWrongAccountModal()

        email_success = email_utils.acount_recovery(name, email, secret, logger)
        slack_success = slack_utils.user_get_in_touch(name, email, subject, description, logger)
        if not email_success or not slack_success:
            return components.SlackConnectionErrorModal()

        return components.ContactRecoverAccountModal()


def retrieve_contact_fnames(session_id, cache):
    fname_alerts = []
    if cache.hexists(session_id, cache_utils.CacheKeys.CONTACT_MAP.value):
        fname_list = decompress_data(cache.hget(session_id, cache_utils.CacheKeys.CONTACT_MAP.value))
        for fname in fname_list:
            fname_alerts.append(components.FilenameAlert(fname, DatasetReference.CONTACT_MAP.value))

    if not fname_alerts:
        return no_update

    return fname_alerts


def retrieve_sequence_fname(session_id, cache):
    if cache.hexists(session_id, cache_utils.CacheKeys.SEQUENCE.value):
        fname = decompress_data(cache.hget(session_id, cache_utils.CacheKeys.SEQUENCE.value))
        return components.FilenameAlert(fname, DatasetReference.SEQUENCE.value)
    else:
        return no_update


def retrieve_additional_fnames(session_id, cache):
    fname_alerts = []

    for dataset in AdditionalDatasetReference:
        if cache.hexists(session_id, dataset.value):
            dataset_fnames = decompress_data(cache.hget(session_id, dataset.value))
            for fname in dataset_fnames:
                fname_alerts.append(components.FilenameAlert(fname, dataset.value))

    if not fname_alerts:
        return no_update
    else:
        return fname_alerts
