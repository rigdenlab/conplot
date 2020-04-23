import dash_bootstrap_components as dbc


def FilenameAlert(component_id):
    return dbc.Alert(
        id="{}-filename-alert".format(component_id),
        dismissable=True,
        color="success"
    )
