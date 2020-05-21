import components
from dash import no_update
import loaders
from utils import callback_utils


def upload_dataset(input_format, trigger, fnames, fcontents, session_id, cache, logger):
    logger.info('Session {} upload triggered'.format(session_id))
    dataset, fname, fcontent, index = callback_utils.get_upload_id(trigger, fnames, fcontents)
    file_divs = [no_update for x in range(0, len(fcontents))]
    cleared_fcontents = [None for x in range(0, len(fcontents))]

    if cache.hexists(session_id, dataset):
        logger.info('Session {} dataset {} already exists'.format(session_id, dataset))
        return file_divs, cleared_fcontents, components.RepeatedInputModal(dataset)
    elif dataset == loaders.DatasetReference.SEQUENCE.value:
        data, invalid = loaders.SequenceLoader(fcontent, fname)
    else:
        data, invalid = loaders.Loader(fcontent, input_format, fname)

    if invalid:
        logger.info('Session {} dataset {} invalid'.format(session_id, dataset))
        return file_divs, cleared_fcontents, components.InvalidFormatModal()
    else:
        logger.info('Session {} uploads {} - {}'.format(session_id, dataset, fname))
        file_divs[index] = components.FilenameAlert(fname, dataset)
        cache.hset(session_id, dataset, data)
        return file_divs, cleared_fcontents, None


def upload_additional_track(fcontent, input_format, fname, fname_alerts, session_id, cache, logger):
    logger.info('Session {} upload triggered'.format(session_id))
    dataset = loaders.AdditionalDatasetReference.__getattr__(input_format).value

    if cache.hexists(session_id, dataset):
        logger.info('Session {} dataset {} already exists'.format(session_id, dataset))
        return components.RepeatedInputModal(dataset), no_update

    data, invalid = loaders.Loader(fcontent, input_format, fname)

    fname_alerts = callback_utils.remove_unused_fname_alerts(fname_alerts)

    if invalid:
        logger.info('Session {} dataset {} invalid'.format(session_id, dataset))
        return components.InvalidFormatModal(), fname_alerts
    else:
        logger.info('Session {} uploads {} - {}'.format(session_id, dataset, fname))
        fname_alerts = [alert for alert in fname_alerts
                        if alert['props']['id'] != 'no-tracks-card'
                        and alert['props']['id'] != 'invalid-track-collapse']
        fname_alerts.append(components.FilenameAlert(fname, dataset))
        cache.hset(session_id, dataset, data)
        return None, fname_alerts


def remove_dataset(trigger, cache, session_id, logger):
    logger.info('Session {} remove file triggered'.format(session_id))
    fname, dataset, is_open = callback_utils.get_remove_trigger(trigger)

    if is_open:
        logger.info('Session {} removal of {} aborted'.format(session_id, dataset))
    else:
        logger.info('Session {} removed dataset {}'.format(session_id, dataset))
        cache.hdel(session_id, dataset)
