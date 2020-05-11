from utils import decompress_data


def decompress_session(session):
    for key in session:
        session[key] = decompress_data(session[key])
    del session['id'.encode()]
    return session
