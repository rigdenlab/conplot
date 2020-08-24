import dash_bootstrap_components as dbc
import dash_html_components as html
from loaders import AdditionalDatasetReference
from parsers import ContactFormats
from components import EmailIssueReference, UserReadableTrackNames
from utils.plot_utils import DefaultTrackLayout
from utils import UrlIndex


def ContactFormatSelector():
    format_list = sorted([{"label": map_format, "value": map_format} for map_format in
                          ContactFormats.__dict__.keys() if '_' not in map_format], key=lambda k: k['label'])
    return dbc.InputGroup(
        [
            dbc.Select(
                id='contact-format-selector',
                options=format_list
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
            dbc.Input(id='L-cutoff-input', type="number", min=0, max=10, step=1, value=factor)
        ]
    )


def AdditionalTrackFormatSelector():
    format_list = sorted([{"label": '{} ({})'.format(track.name, track.value), "value": track.name}
                          for track in AdditionalDatasetReference], key=lambda k: k['value'])
    return dbc.InputGroup(
        [
            dbc.Select(
                id='additional-track-selector',
                options=format_list
            ),
            dbc.InputGroupAddon("Track", addon_type="append"),
        ]
    )


def HalfSquareSelector(idx, options, value):
    return dbc.InputGroup(
        [
            dbc.InputGroupAddon("Map {}".format(idx), addon_type="prepend"),
            dbc.Select(id={'type': 'halfsquare-select', 'index': idx}, options=options, value=value)
        ]
    )


def TrackLayoutSelector(idx, options, value):
    return dbc.InputGroup(
        [
            dbc.InputGroupAddon("Track {}".format(idx), addon_type="prepend"),
            dbc.Select(id={'type': 'track-select'.format(idx), 'index': idx}, options=options, value=value)
        ]
    )


def PaletteSelector(dataset, options, value):
    index = [x.value for x in DefaultTrackLayout].index(dataset.encode())
    return dbc.InputGroup(
        [
            dbc.InputGroupAddon(UserReadableTrackNames.__getattr__(dataset).value, addon_type="prepend"),
            dbc.Select(id={'type': 'colorpalette-select', 'index': index}, options=options, value=value)
        ]
    )


def EmailInput(id='email-input'):
    return dbc.InputGroup([
        dbc.InputGroupAddon("Email", addon_type="prepend"),
        dbc.Input(placeholder="example@email.com", type="email", id=id, minLength=1, maxLength=65),
        dbc.InputGroupAddon('?', id='{}-tooltip'.format(id), addon_type='append', style={'font-size': '500%'}),
        dbc.Tooltip('We will only use this email address to get in touch with you in case your forget your '
                    'password or you request assistance from us.', target='{}-tooltip'.format(id))
    ], className="mb-3")


def NameInput():
    return dbc.InputGroup([
        dbc.InputGroupAddon("Name", addon_type="prepend"),
        dbc.Input(placeholder="First Name", type="text", id='contact-name-input')
    ], className="mb-3")


def ProblemDescriptionInput():
    return dbc.InputGroup([
        dbc.InputGroupAddon("Description", addon_type="prepend"),
        dbc.Textarea(id='contact-text-area-input')
    ], className="mb-3")


def EmailIssueSelect():
    return dbc.InputGroup([
        dbc.Select(
            id='issue-select',
            options=[{"label": "Bug report", "value": EmailIssueReference.BUG.value},
                     {'label': 'I Forgot my password', 'value': EmailIssueReference.FORGOT_PSSWRD.value},
                     {"label": "General inquiry", "value": EmailIssueReference.OTHER.value}]
        ),
        dbc.InputGroupAddon("Subject", addon_type="prepend"),
    ])


def StoreSessionNameInput():
    return dbc.InputGroup([
        dbc.InputGroupAddon("Name", addon_type="prepend"),
        dbc.Input(type="text", id='new-session-name-input', placeholder='New session name', minLength=1, maxLength=25)
    ], className="mb-3")


def UserNameInput(id='username-input', classname="mb-3"):
    return dbc.InputGroup([
        dbc.InputGroupAddon("Username", addon_type="prepend"),
        dbc.Input(type="text", id=id, placeholder='User', minLength=1, maxLength=25)
    ], className=classname)


def PasswordInput(id='password-input', placeholder='XXXX', addon="Password"):
    return dbc.InputGroup([
        dbc.InputGroupAddon(addon, addon_type="prepend"),
        dbc.Input(type="password", id=id, placeholder=placeholder)
    ], className="mb-3")


def ShareWithInput(id):
    return dbc.InputGroup([
        dbc.Input(type="text", id=id, placeholder='Share with...', minLength=1, maxLength=25)
    ])


def TransparentSwitch(transparent):
    if transparent:
        value = [1]
    else:
        value = []

    return dbc.FormGroup(
        [
            dbc.Checklist(
                options=[
                    {"label": "Transparent tracks", "value": 1},
                ],
                value=value,
                id="transparent-tracks-switch",
                switch=True,
            ),
        ], className='mr-1'
    )


def SuperimposeSwitch(superimpose):
    if superimpose:
        value = [1]
    else:
        value = []

    return dbc.FormGroup(
        [
            dbc.Checklist(
                options=[
                    {"label": "Superimpose maps", "value": 1},
                ],
                value=value,
                id="superimpose-maps-switch",
                switch=True,
            ),
        ], className='mr-1'
    )


def GdprAgreementCheckbox():
    return dbc.FormGroup(
        [
            dbc.Checkbox(id="gdpr-agreement-checkbox", className="form-check-input"),
            dbc.Label([
                "I read and agree to ConPlot ",
                dbc.CardLink(html.U("Privacy Policy"), href=UrlIndex.PRIVACY_POLICY.value)
            ], html_for="standalone-checkbox", className="form-check-label", style={'margin-top': 2.5})
        ], check=True)
