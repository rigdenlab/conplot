import json
from utils import decompress_data


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
    index = fnames.index(fname)
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
    if value is not None and value == '1':
        return True
    else:
        return False


def get_current_fnames(session):
    result = {}
    del session[b'id']

    for key in session.keys():
        result[key] = decompress_data(session[key]).pop(-1)

    return result
