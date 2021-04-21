from utils import cache_utils
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


def RecoveryPortalCard():
    return dbc.Card([
        dbc.CardHeader(dbc.Col(html.H1('ConPlot', style={'font-size': '7vh', 'text-align': 'center'}))),
        dbc.CardBody([
            html.H3('Account recovery portal', className="card-text", style={'text-align': "center"}),
            html.Hr(),
            html.Br(),
            dbc.Spinner(html.Div([
                components.UserNameInput('recovery-portal-username-input'),
                components.EmailInput('recovery-portal-email-input', show_tooltip=False),
                components.VerificationCodeInput(id='recovery-portal-secret-input'),
                components.PasswordInput(id='recovery-portal-password-1-input', addon='New Password'),
                components.PasswordInput(id='recovery-portal-password-2-input', addon='Repeat Password'),
                html.Br(),
                html.Div(id='recovery-portal-modal-div'),
                dbc.Button("Recover", color="primary", block=True, id='recover-account-button')
            ], id='recovery-portal-div')),
            html.Br(),
        ])
    ])


def UserPortalCardBody(username):
    if username is not None:
        return [
            html.H6('You are currently logged in as %s. Do you want to logout?' % username,
                    style={'text-align': "center"}),
            html.Div([
                components.UserNameInput('login-username-input'),
                components.PasswordInput('login-password-input'),
                components.InvalidLoginCollapse(id='user-portal-invalid-login-collapse'),
            ], id='place-holder-user-portal', style={'display': 'none'}),
            html.Br(),
            dbc.Button("Logout", color="primary", block=True, id={'type': 'user-portal-button', 'idx': 'logout'}),
        ]
    else:
        return [
            components.UserNameInput('login-username-input'),
            components.PasswordInput('login-password-input'),
            components.InvalidLoginCollapse(id='user-portal-invalid-login-collapse'),
            html.Br(),
            dbc.Button("Login", color="primary", block=True, id={'type': 'user-portal-button', 'idx': 'login'})
        ]


def UserPortalCard(username):
    return dbc.Card([
        dbc.CardBody([
            html.H3('User portal', className="card-text", style={'text-align': "center"}),
            html.Hr(),
            html.Br(),
            dbc.Spinner(html.Div(UserPortalCardBody(username), id='user-portal-div')),
            html.Br(),
            html.Div(id='user-portal-alert-div'),
        ])
    ])


def UserLoginCard():
    return dbc.Card([
        dbc.CardBody([
            html.H3('User login', className="card-text", style={'text-align': "center", 'color': 'red'}),
            html.Hr(),
            html.H5('You must login before accessing the members only area',
                    style={'text-align': "center", 'color': 'red'}),
            html.Br(),
            components.UserNameInput(),
            components.PasswordInput(),
            components.InvalidLoginCollapse(),
            html.Br(),
            dbc.Spinner(html.Div(id='success-login-alert-div')),
            html.Br(),
            dbc.Button("Login", color="primary", block=True, id='require-user-login-button'),
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
            html.H5('Contact Information', style={'text-align': "center"}),
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
            dbc.Button(children='Save', id='store-session-button', disabled=disabled,
                       outline=True, block=True, color='primary')
        ]),
    ])


def NoUserLoggedCard():
    return dbc.Card(dbc.CardBody("You must login before saving session data"), color="danger", outline=True,
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
            components.DistanceMatrixSwitch(False),
            components.VerboseLabelsSwitch(False),
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
                       track_separation=2, transparent=True, superimpose=False, distance_matrix=False,
                       verbose_labels=False):
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
        tracks = get_track_options(available_tracks)
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
                            dbc.Card(components.LFactorSelector(factor, distance_matrix), outline=False),
                            html.Br(),
                            dbc.Card(
                                components.SizeSelector(
                                    'contact-marker-size-input', contact_marker_size, 1, 15, disabled=distance_matrix
                                ), outline=False
                            ),
                            html.Br(),
                            HalfSquareSelectionCard('A', selection=selected_cmaps[0], available_cmaps=available_maps),
                            html.Br(),
                            HalfSquareSelectionCard('B', selection=selected_cmaps[1], available_cmaps=available_maps),
                            html.Br(),
                            components.SuperimposeSwitch(superimpose),
                            components.DistanceMatrixSwitch(distance_matrix),
                            components.VerboseLabelsSwitch(verbose_labels),
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
                            dbc.Card(components.TrackLayoutSelector('-4', tracks, selected_tracks[0]), outline=False),
                            html.Br(),
                            dbc.Card(components.TrackLayoutSelector('-3', tracks, selected_tracks[1]), outline=False),
                            html.Br(),
                            dbc.Card(components.TrackLayoutSelector('-2', tracks, selected_tracks[2]), outline=False),
                            html.Br(),
                            dbc.Card(components.TrackLayoutSelector('-1', tracks, selected_tracks[3]), outline=False),
                            html.Br(),
                            dbc.Card(components.TrackLayoutSelector('0', tracks, selected_tracks[4]), outline=False),
                            html.Br(),
                            dbc.Card(components.TrackLayoutSelector('+1', tracks, selected_tracks[5]), outline=False),
                            html.Br(),
                            dbc.Card(components.TrackLayoutSelector('+2', tracks, selected_tracks[6]), outline=False),
                            html.Br(),
                            dbc.Card(components.TrackLayoutSelector('+3', tracks, selected_tracks[7]), outline=False),
                            html.Br(),
                            dbc.Card(components.TrackLayoutSelector('+4', tracks, selected_tracks[8]), outline=False),
                            html.Br(),
                            html.Br(),
                            html.H5("Colour palettes", className="card-text", style={'text-align': "center"}),
                            html.Hr(),
                            html.Br(),
                            ColorPaletteSelectionCard('density', selected_palettes[0]),
                            html.Br(),
                            ColorPaletteSelectionCard('custom', selected_palettes[1]),
                            html.Br(),
                            ColorPaletteSelectionCard('heatmap', selected_palettes[2]),
                            html.Br(),
                            ColorPaletteSelectionCard('hydrophobicity', selected_palettes[3]),
                            html.Br(),
                            ColorPaletteSelectionCard('membranetopology', selected_palettes[4]),
                            html.Br(),
                            ColorPaletteSelectionCard('msa', selected_palettes[5]),
                            html.Br(),
                            ColorPaletteSelectionCard('conservation', selected_palettes[6]),
                            html.Br(),
                            ColorPaletteSelectionCard('disorder', selected_palettes[7]),
                            html.Br(),
                            ColorPaletteSelectionCard('secondarystructure', selected_palettes[8]),
                            html.Br(),
                        ])
                    ]
                )
            )
        ])
    else:
        raise ValueError('This should not occur! Please report.')


def get_track_options(available_tracks):
    track_iterator = iter(available_tracks)

    fname = next(track_iterator)
    track_options = [{'label': '--- Empty ---', 'value': 'Empty_1'},
                     {'label': '--- Seq. Hydrophobicity ---', 'value': 'Hydrophobicity_Header', 'disabled': True},
                     {'label': fname, 'value': fname},
                     {'label': '--- Contact Density ---', 'value': 'Density_Header', 'disabled': True}]

    fname = next(track_iterator, None)
    cmap_density = []
    while fname and cache_utils.MetadataTags.DENSITY.value in fname:
        cmap_density.append({'label': fname, 'value': fname})
        fname = next(track_iterator, None)
    if not cmap_density:
        track_options.append({'label': '--- Empty ---', 'value': 'Empty_2'})
    else:
        track_options += sorted(cmap_density, key=lambda k: k['label'])

    track_options.append({'label': '--- Contact Diff ---', 'value': 'Diff_Header', 'disabled': True})
    cmap_diff = []
    while fname and cache_utils.MetadataTags.DIFF.value in fname:
        cmap_diff.append({'label': fname, 'value': fname})
        fname = next(track_iterator, None)
    if not cmap_diff:
        track_options.append({'label': '--- Empty ---', 'value': 'Empty_3'})
    else:
        track_options += sorted(cmap_diff, key=lambda k: k['label'])

    track_options.append({'label': '--- Other Tracks ---', 'value': 'AdditionalTracks_Header', 'disabled': True})
    other_tracks = []
    while fname:
        other_tracks.append({'label': fname, 'value': fname})
        fname = next(track_iterator, None)
    if not other_tracks:
        track_options.append({'label': '--- Empty ---', 'value': 'Empty_4'})
    else:
        track_options += sorted(other_tracks, key=lambda k: k['label'])
    return track_options


def ColorPaletteSelectionCard(dataset, selected_palette):
    available_palettes = []
    for palette in color_palettes.DatasetColorPalettes.__getattr__(dataset).value:
        available_palettes.append({'label': palette.name, 'value': palette.name})

    return dbc.Card(components.PaletteSelector(dataset, available_palettes, selected_palette), outline=False)


def HalfSquareSelectionCard(square_idx, selection, available_cmaps):
    cmap_options = [{'label': '--- Empty ---', 'value': '---'}]
    cmap_options += [{'label': fname, 'value': fname} for fname in available_cmaps]

    return dbc.Card(components.HalfSquareSelector(square_idx, cmap_options, selection), outline=False)


def InvalidFormatCard():
    return dbc.Card(dbc.CardBody("Invalid format, unable to load", style={'text-align': "center"}), color="danger",
                    outline=True)


def CreateUserCard():
    return dbc.Card([
        dbc.CardBody([
            html.Div(id='create-user-modal-div'),
            html.H3('Create a new user', className="card-text", style={'text-align': "center"}),
            html.Hr(),
            html.Br(),
            components.UserNameInput('create-username-input'),
            components.PasswordInput('create-password-input'),
            components.EmailInput('create-email-input'),
            components.InvalidNewUserCollapse(),
            html.Br(),
            components.GdprAgreementCheckbox(),
            html.Br(),
            dbc.Button([
                dbc.Spinner(html.Div("Create new user", id='create-user-button-div'), size='sm')
            ], color="primary", block=True, id='create-user-button', disabled=True)
        ]),
    ])


def UserStoredSessionsCard(username, current_session_pkid=None):
    return dbc.Card([
        dbc.CardBody([
            html.H3('Stored sessions', className="card-text", style={'text-align': "center"}),
            html.Hr(),
            html.P('Here you will find a list of all the sessions you have saved in your personal storage. These '
                   'sessions are private and only you and those user you decide to share them with will be able '
                   'to access them.',
                   style={'text-align': "center"}),
            html.Br(),
            dbc.Spinner(components.SessionList(username, components.SessionListType.STORED, current_session_pkid),
                        id='stored-sessions-list-spinner')
        ])
    ])


def UserSharedSessionsCard(username, current_session_pkid=None):
    return dbc.Card([
        dbc.CardBody([
            html.H3('Shared sessions', className="card-text", style={'text-align': "center"}),
            html.Hr(),
            html.P('Here you will find a list with all the sessions that other users have shared with you. You only '
                   'have read permissions to these sessions, but once you load them you will be able to save a copy '
                   'into your personal storage from the Plot tab. You can also decide to stop sharing them at any '
                   'moment.', style={'text-align': "center"}),
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
            html.P('By sharing a session you grant another user with read-only permissions on '
                   'your data. They will also be able to see your username, the name of the session and the '
                   'date when you created it. If you update the contents of the shared session, they will '
                   'also be able to see the updated data.', style={'text-align': "center"}),
            html.Br(),
            components.SessionList(username, components.SessionListType.TO_SHARE),
        ])
    ])
