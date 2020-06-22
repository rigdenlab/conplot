import components
from dash import no_update
import loaders
from utils import callback_utils, cache_utils, compress_data


def upload_sequence(fname, fcontent, session_id, cache, logger):
    logger.info('Session {} sequence upload triggered'.format(session_id))

    if cache.hexists(session_id, fname):
        logger.info('Session {} filename {} already exists'.format(session_id, fname))
        return no_update, None, components.RepeatedInputModal(fname)
    if cache.hexists(session_id, cache_utils.CacheKeys.SEQUENCE.value):
        logger.info('Session {} sequence dataset already uploaded'.format(session_id))
        return no_update, None, components.SequenceAlreadyUploadedModal()

    sequence_data, seq_hydrophobicity, invalid = loaders.SequenceLoader(fcontent)

    if invalid:
        logger.info('Session {} file {} is invalid sequence file'.format(session_id, fname))
        return no_update, None, components.InvalidFormatModal()
    else:
        logger.info('Session {} uploads {} - sequence'.format(session_id, fname))
        cache.hset(session_id, fname, sequence_data)
        cache.hset(session_id, cache_utils.CacheKeys.SEQUENCE_HYDROPHOBICITY.value, seq_hydrophobicity)
        cache.hset(session_id, cache_utils.CacheKeys.SEQUENCE.value, compress_data(fname))
        return components.FilenameAlert(fname, loaders.DatasetReference.SEQUENCE.value), None, None


def upload_dataset(fname, fcontent, input_format, fname_alerts, session_id, cache, logger, dataset=None):
    logger.info('Session {} upload triggered'.format(session_id))
    if dataset is None:
        dataset = loaders.AdditionalDatasetReference.__getattr__(input_format).value

    if cache.hexists(session_id, fname):
        logger.info('Session {} filename {} already exists'.format(session_id, fname))
        return no_update, None, components.RepeatedInputModal(fname)

    data, invalid = loaders.Loader(fcontent, input_format)

    fname_alerts = callback_utils.remove_unused_fname_alerts(fname_alerts)

    if invalid:
        logger.info('Session {} file {} is invalid {}'.format(session_id, fname, dataset))
        return fname_alerts, None, components.InvalidFormatModal()
    else:
        logger.info('Session {} uploads {} - {}'.format(session_id, fname, dataset))
        fname_alerts = [alert for alert in fname_alerts
                        if alert['props']['id'] != 'no-tracks-card'
                        and alert['props']['id'] != 'invalid-track-collapse']
        fname_alerts.append(components.FilenameAlert(fname, dataset))
        cache.hset(session_id, fname, data)
        cache_utils.store_fname(cache, session_id, fname, dataset)

        return fname_alerts, None, None


def remove_dataset(trigger, cache, session_id, logger):
    logger.info('Session {} remove file triggered'.format(session_id))
    fname, dataset, is_open = callback_utils.get_remove_trigger(trigger)

    if is_open:
        logger.info('Session {} removal of {} aborted'.format(session_id, dataset))
    else:
        logger.info('Session {} removed {} - {}'.format(session_id, fname, dataset))
        cache.hdel(session_id, fname)
        cache_utils.remove_fname(cache, session_id, fname, dataset)
