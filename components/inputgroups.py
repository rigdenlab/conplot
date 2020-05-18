import dash_bootstrap_components as dbc
from loaders import AdditionalDatasetReference
from parsers import ContactFormats


def ContactFormatSelector():
    return dbc.InputGroup(
        [
            dbc.Select(
                id='contact-format-selector',
                options=[{"label": map_format, "value": map_format} for map_format in
                         ContactFormats.__dict__.keys() if '_' not in map_format]
            ),
            dbc.InputGroupAddon("Format", addon_type="append")
        ]
    )


def SizeSelector(id, marker_size, min, max, text='Size'):
    return dbc.InputGroup(
        [
            dbc.InputGroupAddon(text, addon_type="prepend"),
            dbc.Input(id=id, type="number", min=min, max=max, step=1, value=marker_size),
        ]
    )


def LFactorSelector(factor=2):
    return dbc.InputGroup(
        [
            dbc.InputGroupAddon("L /", addon_type="prepend"),
            dbc.Input(id='L-cutoff-input', type="number", min=1, max=10, step=1, value=factor)
        ]
    )


def AdditionalTrackFormatSelector():
    return dbc.InputGroup(
        [
            dbc.Select(
                id='track-selector',
                options=[{"label": '{} ({})'.format(track.name, track.value), "value": track.name}
                         for track in AdditionalDatasetReference]
            ),
            dbc.InputGroupAddon("Track", addon_type="append"),
        ]
    )


def TrackLayoutSelector(idx, options, value):
    return dbc.InputGroup(
        [
            dbc.InputGroupAddon("Track {}".format(idx), addon_type="prepend"),
            dbc.Select(id={'type': 'track-select'.format(idx), 'index': idx}, options=options, value=value)
        ]
    )


def EmailInput():
    return dbc.InputGroup([
        dbc.InputGroupAddon("@", addon_type="prepend"),
        dbc.Input(placeholder="Email address", type="email")
    ], className="mb-3")


def NameInput():
    return dbc.InputGroup(dbc.Input(placeholder="First Name"), className="mb-3")


def ProblemDescriptionInput():
    return dbc.InputGroup([
        dbc.InputGroupAddon("Description", addon_type="prepend"),
        dbc.Textarea()
    ], className="mb-3")


def EmailIssueSelect():
    return dbc.InputGroup([
        dbc.Select(
            id='issue-select',
            options=[{"label": "Bug report", "value": 1}, {"label": "General inquiry", "value": 2}]
        ),
        dbc.InputGroupAddon("Subject", addon_type="prepend"),
    ])
