import uuid
from core.session import Session
from app import cache


def initiate_session():
    session_id = str(uuid.uuid4())
    session = Session(session_id)
    cache.set('session-{}'.format(session_id), session)
    return session_id


def store_dataset(dataset, session, *args):
    session.__getattribute__('{}_loader'.format(dataset)).register_input(*args)
    session.__getattribute__('{}_loader'.format(dataset)).load()
    cache.set('session-{}'.format(session.id), session)
    return session.__getattribute__('{}_loader'.format(dataset)).layout_states


def remove_file(dataset, session):
    session.__getattribute__('{}_loader'.format(dataset)).clear()
    cache.set('session-{}'.format(session.id), session)


def ensure_triggered(trigger):
    context = trigger[0]
    prop_id = context['prop_id']
    value = context['value']
    if prop_id == '.' or value is None:
        return False
    else:
        return True
