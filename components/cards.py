from components import UploadButton, AddTrackButton, ContactFormatSelector, AdditionalTrackFormatSelector, \
    DisplayControlHeader, AdditionalInputHeader, MandatoryInputHeader, LFactorSelector, SizeSelector, \
    TrackLayoutSelector, ErrorAlert
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from loaders import DatasetReference


def NoPageFoundCard(url):
    return dbc.Card([
        dbc.CardBody([
            html.H2('Something went wrong...', className="card-text", style={'text-align': "center"}),
            html.Hr(),
            html.Br(),
            html.P(["404 Page not found: {}".format(url)]),
            html.Br(),
            ErrorAlert(True)

        ])
    ])


def SequenceUploadCard():
    return dbc.Card([
        dbc.CardBody([
            html.H5('Sequence', style={'text-align': "center"}),
            html.Br(),
            html.Div(id={'type': 'file-div', 'index': DatasetReference.SEQUENCE.value}),
            UploadButton(DatasetReference.SEQUENCE.value),
        ], id='format-selection-card'),
    ])


def ContactFormatSelectionCard():
    return dbc.Card(ContactFormatSelector(), id='format-selection-card', color="danger", outline=True)


def AdditionalTrackFormatSelectionCard():
    return dbc.Card(AdditionalTrackFormatSelector(), id='track-selection-card', color="danger", outline=True)


def ContactUploadCard():
    return dbc.Card([
        dbc.CardBody([
            html.H5('Contact Map', style={'text-align': "center"}),
            html.Br(),
            ContactFormatSelectionCard(),
            html.Br(),
            html.Div(id={'type': 'file-div', 'index': DatasetReference.CONTACT_MAP.value}),
            UploadButton(DatasetReference.CONTACT_MAP.value, disabled=True)
        ], id='format-selection-card'),
    ])


def MandatoryUploadCard():
    return dbc.Card(
        dbc.CardBody(
            [
                MandatoryInputHeader(),
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
            AdditionalInputHeader(),
            html.Br(),
            html.Div([
                NoAdditionalTracksCard()
            ], id='additional-tracks-filenames'),
            html.Br(),
            AdditionalTrackFormatSelectionCard(),
            html.Br(),
            AddTrackButton(disabled=True)
        ]),
    ])


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
            dbc.Input(id='contact-marker-size-input', value=contact_marker_size),
            dbc.Input(id='track-marker-size-input', value=track_marker_size),
            dbc.Input(id='track-separation-size-input', value=track_separation),
        ], style={'display': 'none'})
    ],
        color="danger",
        outline=True
    )


def DisplayControlCard(available_tracks=None, selected_tracks=None, factor=2, contact_marker_size=5,
                       track_marker_size=5, track_separation=2):
    if available_tracks is None:
        return dbc.Card(
            dbc.CardBody(
                [
                    DisplayControlHeader(),
                    html.Br(),
                    NoPlotDisplayControlCard(contact_marker_size, track_marker_size, track_separation)
                ]
            )
        )
    elif selected_tracks is not None and len(selected_tracks) >= 9:
        return html.Div([
            html.H4('Display control', className="card-text", style={'text-align': "center"}),
            html.Br(),
            dbc.Card(
                dbc.CardBody(
                    [
                        html.Div([
                            html.P("Adjust contact map", className="card-text"),
                            dbc.Card(LFactorSelector(factor), outline=False),
                            html.Br(),
                            dbc.Card(SizeSelector('contact-marker-size-input', contact_marker_size, 1, 15),
                                     outline=False),
                            html.Br(),
                            html.Hr(),
                            html.P('Adjust additional tracks'),
                            dbc.Card(SizeSelector('track-marker-size-input', track_marker_size, 1, 20),
                                     outline=False),
                            html.Br(),
                            dbc.Card(
                                SizeSelector('track-separation-size-input', track_separation, 1, 150, 'Separation'),
                                outline=False),
                            html.Br(),
                            html.Hr(),
                            html.P("Active tracks", className="card-text"),
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
                        ])
                    ]
                )
            )
        ])
    else:
        raise ValueError('Available tracks detected but not enough were selected! Please report.')


def TrackSelectionCard(track_idx, track_value, available_tracks):
    track_options = [{'label': 'None', 'value': None}]
    track_options += [{'label': dataset, 'value': dataset} for dataset in available_tracks]

    return dbc.Card(TrackLayoutSelector(track_idx, track_options, track_value), outline=False)


def InvalidFormatCard():
    return dbc.Card(dbc.CardBody("Invalid format, unable to load", style={'text-align': "center"}), color="danger",
                    outline=True)
