import components
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from loaders import DatasetReference
from utils import color_palettes


def ChangeUserPasswordCard(username):
    return dbc.Card([
        dbc.CardBody([
            html.H3("Change %s's password" % username, className="card-text", style={'text-align': "center"}),
            html.Hr(),
            html.Br(),
            components.PasswordInput(id='old-password-input', addon='Old', placeholder='password'),
            components.PasswordInput(id='new-password-input', addon='New', placeholder='password'),
            html.Br(),
            dbc.Spinner(html.Div(id='success-change-password-alert-div')),
            html.Br(),
            dbc.Button("Change", color="primary", block=True, id='user-change-password-button'),
            html.Br(),
        ])
    ])


def NoPageFoundCard(url):
    return dbc.Card([
        dbc.CardBody([
            html.H2('Something went wrong...', className="card-text", style={'text-align': "center"}),
            html.Hr(),
            html.Br(),
            html.P(["404 Page not found: {}".format(url)]),
            html.Br(),
            components.ErrorAlert(True)

        ])
    ])


def UserLoginCard(not_logged_in=False):
    if not_logged_in:
        warning = html.H5('You must login before accessing the members only area', style={'text-align': "center"})
    else:
        warning = None

    return dbc.Card([
        dbc.CardBody([
            html.H3('User login', className="card-text", style={'text-align': "center"}),
            html.Hr(),
            warning,
            html.Br(),
            components.UserNameInput(),
            components.PasswordInput(),
            components.InvalidLoginCollapse(),
            html.Br(),
            dbc.Spinner(html.Div(id='success-login-alert-div')),
            html.Br(),
            dbc.Button("Login", color="primary", block=True, id='user-login-button'),
            html.Br(),
        ])
    ])


def UserLogoutCard(username):
    return dbc.Card([
        dbc.CardBody([
            html.H3('User logout', className="card-text", style={'text-align': "center"}),
            html.Hr(),
            html.Br(),
            html.Br(),
            html.H6('You are currently logged in as %s. Do you want to logout?' % username,
                    style={'text-align': "center"}),
            html.Br(),
            dbc.Spinner(html.Div(id='success-logout-alert-div')),
            html.Br(),
            dbc.Button("Logout", color="danger", block=True, id='user-logout-button'),
            html.Br(),
        ])
    ])


def SequenceUploadCard():
    return dbc.Card([
        dbc.CardBody([
            html.H5('Sequence', style={'text-align': "center"}),
            html.Br(),
            html.Div(id='sequence-filename-div'),
            components.UploadButton(DatasetReference.SEQUENCE.value),
        ], id='format-selection-card'),
    ])


def ContactFormatSelectionCard():
    return dbc.Card(components.ContactFormatSelector(), id='format-selection-card', color="danger", outline=True)


def AdditionalTrackFormatSelectionCard():
    return dbc.Card(components.AdditionalTrackFormatSelector(), id='track-selection-card', color="danger", outline=True)


def ContactUploadCard():
    return dbc.Card([
        dbc.CardBody([
            html.H5('Contact Map', style={'text-align': "center"}),
            html.Br(),
            ContactFormatSelectionCard(),
            html.Br(),
            html.Div(id='contact-filenames-div'),
            html.Br(),
            components.UploadButton(DatasetReference.CONTACT_MAP.value, disabled=True)
        ], id='format-selection-card'),
    ])


def MandatoryUploadCard():
    return dbc.Card(
        dbc.CardBody(
            [
                components.MandatoryInputHeader(),
                html.Br(),
                SequenceUploadCard(),
                html.Br(),
                ContactUploadCard(),
            ]
        )
    )


def AdditionalTracksUploadCard():
    return dbc.Card([
        dbc.CardBody([
            components.AdditionalInputHeader(),
            html.Br(),
            html.Div([
                NoAdditionalTracksCard(),
            ], id='additional-tracks-filenames-div'),
            html.Br(),
            AdditionalTrackFormatSelectionCard(),
            html.Br(),
            components.AddTrackButton(disabled=True)
        ]),
    ])


def StoreSessionCard(username=None):
    if username is not None:
        disabled = False
        content = components.StoreSessionNameInput()
    else:
        disabled = True
        content = [NoUserLoggedCard(), html.Div(components.StoreSessionNameInput(), style={'display': 'none'})]
    return dbc.Card([
        dbc.CardBody([
            components.StoreSessionHeader(),
            html.Br(),
            html.Div(content, id='store-session-card-div'),
            html.Br(),
            dbc.Button(children=html.I(className="fas fa-save fa-2x"), id='store-session-button', disabled=disabled,
                       outline=True, block=True, color='primary')
        ]),
    ])


def NoUserLoggedCard():
    return dbc.Card(dbc.CardBody("You must loggin before saving session data"), color="danger", outline=True,
                    id='user-not-logged-card', style={'text-align': "center"})


def NoAdditionalTracksCard():
    return dbc.Card(dbc.CardBody("No additional tracks"), color="danger", outline=True, id='no-tracks-card',
                    style={'text-align': "center"})


def NoPlotDisplayControlCard(contact_marker_size, track_marker_size, track_separation):
    return dbc.Card([
        dbc.CardBody("Need to create a plot first!", style={'text-align': "center"}),
        html.Div([
            dbc.Button('Refresh', id='refresh-button', outline=True, color='primary', block=True),
            dcc.Dropdown(id='track-selection-dropdown'),
            dbc.Input(id='L-cutoff-input', value=2),
            components.TransparentSwitch(True),
            components.SuperimposeSwitch(False),
            dbc.Input(id='contact-marker-size-input', value=contact_marker_size),
            dbc.Input(id='track-marker-size-input', value=track_marker_size),
            dbc.Input(id='track-separation-size-input', value=track_separation),
        ], style={'display': 'none'})
    ],
        color="danger",
        outline=True
    )


def DisplayControlCard(available_tracks=None, selected_tracks=None, selected_cmaps=None, available_maps=None,
                       selected_palettes=None, factor=2, contact_marker_size=5, track_marker_size=5,
                       track_separation=2, transparent=True, superimpose=False):
    if available_tracks is None or available_maps is None or selected_palettes is None:
        return dbc.Card(
            dbc.CardBody(
                [
                    components.DisplayControlHeader(),
                    html.Br(),
                    NoPlotDisplayControlCard(contact_marker_size, track_marker_size, track_separation)
                ]
            )
        )
    elif selected_tracks is not None and len(selected_tracks) >= 9 \
            and selected_cmaps is not None and len(selected_cmaps) >= 2:
        return html.Div([
            components.DisplayControlHeader(),
            html.Br(),
            dbc.Card(
                dbc.CardBody(
                    [
                        html.Div([
                            html.H5("Adjust contact map", className="card-text", style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            dbc.Card(components.LFactorSelector(factor), outline=False),
                            html.Br(),
                            dbc.Card(components.SizeSelector('contact-marker-size-input', contact_marker_size, 1, 15),
                                     outline=False),
                            html.Br(),
                            HalfSquareSelectionCard('A', selection=selected_cmaps[0], available_cmaps=available_maps),
                            html.Br(),
                            HalfSquareSelectionCard('B', selection=selected_cmaps[1], available_cmaps=available_maps),
                            html.Br(),
                            components.SuperimposeSwitch(superimpose),
                            html.Br(),
                            html.H5('Adjust additional tracks', className="card-text", style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            dbc.Card(components.SizeSelector('track-marker-size-input', track_marker_size, 1, 20),
                                     outline=False),
                            html.Br(),
                            dbc.Card(
                                components.SizeSelector('track-separation-size-input', track_separation, 1, 150,
                                                        'Separation'),
                                outline=False),
                            html.Br(),
                            components.TransparentSwitch(transparent),
                            html.Br(),
                            html.H5("Active tracks", className="card-text", style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            TrackSelectionCard('-4', selected_tracks[0], available_tracks=available_tracks),
                            html.Br(),
                            TrackSelectionCard('-3', selected_tracks[1], available_tracks=available_tracks),
                            html.Br(),
                            TrackSelectionCard('-2', selected_tracks[2], available_tracks=available_tracks),
                            html.Br(),
                            TrackSelectionCard('-1', selected_tracks[3], available_tracks=available_tracks),
                            html.Br(),
                            TrackSelectionCard(' 0', selected_tracks[4], available_tracks=available_tracks),
                            html.Br(),
                            TrackSelectionCard('+1', selected_tracks[5], available_tracks=available_tracks),
                            html.Br(),
                            TrackSelectionCard('+2', selected_tracks[6], available_tracks=available_tracks),
                            html.Br(),
                            TrackSelectionCard('+3', selected_tracks[7], available_tracks=available_tracks),
                            html.Br(),
                            TrackSelectionCard('+4', selected_tracks[8], available_tracks=available_tracks),
                            html.Br(),
                            html.Br(),
                            html.H5("Colour palettes", className="card-text", style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            ColorPaletteSelectionCard('membranetopology', selected_palettes[0]),
                            html.Br(),
                            ColorPaletteSelectionCard('secondarystructure', selected_palettes[1]),
                            html.Br(),
                            ColorPaletteSelectionCard('disorder', selected_palettes[2]),
                            html.Br(),
                            ColorPaletteSelectionCard('conservation', selected_palettes[3]),
                            html.Br(),
                            ColorPaletteSelectionCard('custom', selected_palettes[4]),
                            html.Br(),
                        ])
                    ]
                )
            )
        ])
    else:
        raise ValueError('This should not occur! Please report.')


def TrackSelectionCard(track_idx, track_value, available_tracks):
    track_options = [{'label': '---', 'value': '---'}]
    track_options += [{'label': fname, 'value': fname} for fname in available_tracks]

    return dbc.Card(components.TrackLayoutSelector(track_idx, track_options, track_value), outline=False)


def ColorPaletteSelectionCard(dataset, selected_palette):
    available_palettes = []
    for palette in color_palettes.DatasetColorPalettes.__getattr__(dataset).value:
        available_palettes.append({'label': palette.name, 'value': palette.name})

    return dbc.Card(components.PaletteSelector(dataset, available_palettes, selected_palette), outline=False)


def HalfSquareSelectionCard(square_idx, selection, available_cmaps):
    cmap_options = [{'label': '---', 'value': '---'}]
    cmap_options += [{'label': fname, 'value': fname} for fname in available_cmaps]

    return dbc.Card(components.HalfSquareSelector(square_idx, cmap_options, selection), outline=False)


def InvalidFormatCard():
    return dbc.Card(dbc.CardBody("Invalid format, unable to load", style={'text-align': "center"}), color="danger",
                    outline=True)


def CreateUserCard():
    return dbc.Card([
        dbc.CardBody([
            html.H3('Create a new user', className="card-text", style={'text-align': "center"}),
            html.Hr(),
            html.Br(),
            components.UserNameInput(),
            components.PasswordInput(),
            components.EmailInput(),
            components.InvalidNewUserCollapse(),
            html.Br(),
            dbc.Spinner(html.Div(id='success-create-user-alert-div')),
            components.GdprAgreementCheckbox(),
            html.Br(),
            dbc.Button("Create new user", color="primary", block=True, id='create-user-button', disabled=True),
        ]),
    ])


def UserStoredSessionsCard(username, current_session_pkid=None):
    return dbc.Card([
        dbc.CardBody([
            html.H3('%s stored sessions' % username, className="card-text", style={'text-align': "center"}),
            html.Hr(),
            html.Br(),
            dbc.Spinner(components.SessionList(username, components.SessionListType.STORED, current_session_pkid),
                        id='stored-sessions-list-spinner')
        ])
    ])


def UserSharedSessionsCard(username, current_session_pkid=None):
    return dbc.Card([
        dbc.CardBody([
            html.H3('Sessions shared with %s' % username, className="card-text", style={'text-align': "center"}),
            html.Hr(),
            html.Br(),
            dbc.Spinner(components.SessionList(username, components.SessionListType.SHARED, current_session_pkid),
                        id='shared-sessions-list-spinner')
        ])
    ])


def ShareSessionsCard(username):
    return dbc.Card([
        dbc.CardBody([
            html.H3('Share a session with another user', className="card-text",
                    style={'text-align': "center"}),
            html.Hr(),
            html.Br(),
            components.SessionList(username, components.SessionListType.TO_SHARE),
        ])
    ])
