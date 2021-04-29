import components
from dash import no_update
import loaders
from operator import itemgetter
from utils import callback_utils, cache_utils, compress_data, decompress_data


def check_sequence_mismatch(session_id, cache, seq_length):
    mismatched = []

    if cache.hexists(session_id, cache_utils.CacheKeys.CONTACT_MAP.value):
        cmap_fnames = decompress_data(cache.hget(session_id, cache_utils.CacheKeys.CONTACT_MAP.value))
        for cmap_fname in cmap_fnames:
            cmap_data = decompress_data(cache.hget(session_id, cmap_fname))
            if cmap_data[0] == 'PDB' or cmap_data[0] == 'DISTO':
                cmap_data = cmap_data[1:]
            cmap_max_register = max((max(cmap_data, key=itemgetter(0))[0], max(cmap_data, key=itemgetter(1))[0]))
            if cmap_max_register > seq_length:
                mismatched.append(cmap_fname)

    for dataset in loaders.AdditionalDatasetReference:
        if cache.hexists(session_id, dataset.value):
            fnames = decompress_data(cache.hget(session_id, dataset.value))
            for fname in fnames:
                data = decompress_data(cache.hget(session_id, fname))
                if data is not None and len(data) != seq_length:
                    mismatched.append(fname)

    return mismatched


def check_dataset_mismatch(session_id, cache, data, dataset):
    if not cache.hexists(session_id, cache_utils.CacheKeys.SEQUENCE.value):
        return False

    seq_fname = decompress_data(cache.hget(session_id, cache_utils.CacheKeys.SEQUENCE.value))
    seq_length = len(decompress_data(cache.hget(session_id, seq_fname)))
    data = decompress_data(data)

    if dataset in loaders.AdditionalDatasetReference._value2member_map_:
        if len(data) != seq_length:
            return seq_fname
        else:
            return False
    elif data[0] == 'PDB' or data[0] == 'DISTO':
        max_register = max((max(data[1:], key=itemgetter(0))[0], max(data[1:], key=itemgetter(1))[0]))
    else:
        max_register = max((max(data, key=itemgetter(0))[0], max(data, key=itemgetter(1))[0]))

    if max_register > seq_length:
        return seq_fname

    return False


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

    mismatched = check_sequence_mismatch(session_id, cache, len(decompress_data(sequence_data)))
    if any(mismatched):
        logger.info('Session {} mismatch {} sequence file detected'.format(session_id, fname))
        return no_update, None, components.MismatchSequenceModal(*mismatched)

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

    mismatched = check_dataset_mismatch(session_id, cache, data, dataset)
    if mismatched:
        logger.info('Session {} mismatch {} file detected'.format(session_id, fname))
        return no_update, None, components.MismatchDatasetModal(fname, mismatched)
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
        return
    else:
        logger.info('Session {} removed {} - {}'.format(session_id, fname, dataset))
        cache.hdel(session_id, fname)
        cache_utils.remove_fname(cache, session_id, fname, dataset)

    if dataset == loaders.DatasetReference.SEQUENCE.value:
        cache_utils.remove_all(session_id, cache_utils.CacheKeys.CONTACT_DENSITY.value, cache)
        cache_utils.remove_all(session_id, cache_utils.CacheKeys.CONTACT_DIFF.value, cache)
    elif dataset == loaders.DatasetReference.CONTACT_MAP.value:
        cache_utils.remove_density(session_id, cache, fname)
        cache_utils.remove_diff(session_id, cache, fname)


def lookup_data(session, session_id, cachekey, cache):
    if cachekey in session.keys():
        data = session[cachekey]
    elif cache.hexists(session_id, cachekey):
        data = cache_utils.retrieve_data(session_id, cachekey, cache)
    else:
        return None
    return data
