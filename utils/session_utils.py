from utils import decompress_data


def decompress_session(session):
    try:
        del session[b'id']
    except KeyError:
        pass
    for key in session:
        session[key] = decompress_data(session[key])
    return session
