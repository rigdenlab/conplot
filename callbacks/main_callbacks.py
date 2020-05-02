from core import PathIndex
from layouts import noPage, Home, DataUpload, Contact


def display_page(url, session_id):
    if url == PathIndex.HOME.value or url == PathIndex.ROOT.value:
        return Home(session_id)
    elif url == PathIndex.CONTACT.value:
        return Contact(session_id)
    elif url == PathIndex.PLOT.value:
        return DataUpload(session_id)
    else:
        return noPage(url)
