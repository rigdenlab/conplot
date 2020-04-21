import uuid
from core import Session
from app import cache


def initiate_session():
    session_id = str(uuid.uuid4())
    session = Session(session_id)
    cache.set('session-{}'.format(session_id), session)
    return session_id
