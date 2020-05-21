from utils import decompress_data


def decompress_session(session):
    for key in (b'id', b'user', b'session_name'):
        if key in session:
            del session[key]

    for key in session.keys():
        session[key] = decompress_data(session[key])
        session[key].pop(-1)
    return session
