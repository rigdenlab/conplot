
def ensure_triggered(trigger):
    context = trigger[0]
    prop_id = context['prop_id']
    value = context['value']
    if prop_id == '.' or value is None:
        return False
    else:
        return True
