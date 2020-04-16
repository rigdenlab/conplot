import base64
from conkit.io.psicov import PsicovParser
from conkit.io.fasta import FastaParser
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from components import NavBar, Header, PathIndex, FastaUploadCard, ContactUploadCard
from app import app
import pandas as pd
import dash_bootstrap_components as dbc
import json
from io import StringIO
import logging


def Body():
    return html.Div(
        [
            html.Br(),
            html.H1('Data Upload'),
            html.H6(["Please upload the files of interest or paste their contents"]),
            html.Br(),
            dbc.CardDeck(
                [
                    FastaUploadCard(),
                    ContactUploadCard()
                ]
            ),
            html.Br(),
            html.Br(),
            dbc.Button("Plot", id='plot-button', color="primary", block=True),
            html.Br(),
            html.Div(id='final-plot')
        ]
    )


def Plot():
    return html.Div([
        Header(),
        NavBar(PathIndex.PLOT.value),
        Body(),
        html.Div(id='_cmap', style={'display': 'none'}),
        html.Div(id='_fasta', style={'display': 'none'}),
        html.Div(id='_n_clicks', style={'display': 'none'}),
    ])


@app.callback(Output('final-plot', 'children'),
              [Input('_cmap', 'children'),
               Input('_fasta', 'children'),
               Input("plot-button", "n_clicks"),
               Input('_n_clicks', 'children')])
def create_plot(df, seq, n_clicks, _n_clicks):
    logging.debug('Function create_plot called')

    # TODO: Cache the n_clicks so that we only compute things when the n_clicks change
    if df is None or seq is None or n_clicks is None:
        print('Something is None')
        return

    else:
        print('Plotting!')
        df = pd.read_json(df[0], orient='split')
        seq = json.loads(seq[0])

    # TODO: Need to make this decent
    x_coords = df[0].tolist()[:100]
    y_coords = df[1].tolist()[:100]
    labels = [(x, y) for x, y in zip(x_coords, y_coords)]

    return dcc.Graph(
        figure={
            'data': [
                dict(
                    x=x_coords,
                    y=y_coords,
                    text=labels,
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.1, 'color': 'black'}
                    },
                    name=i
                ) for i in range(0, 100)
            ],
            'layout': dict(
                xaxis={'title': 'Residue 1'},
                yaxis={'title': 'Residue 2'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                hovermode='closest',
                showlegend=False,
            )
        }
    ), n_clicks


@app.callback(Output('_cmap', 'children'),
              [Input('upload-contact-map', 'contents')])
def upload_contacts(list_of_contents):
    def parse_contacts(contents):
        content_type, content_string = contents.split(',')

        decoded = base64.b64decode(content_string)
        decoded = str(decoded)

        cmap = PsicovParser().read(f_handle=decoded.split('\\n')).top_map
        return pd.DataFrame(cmap.as_list()).to_json(date_format='iso', orient='split')

    if list_of_contents is not None:
        children = [parse_contacts(list_of_contents)]
        return children


@app.callback(Output('_fasta', 'children'),
              [Input('upload-fasta', 'contents')])
def upload_sequence(list_of_contents):
    def parse_sequence(contents):
        content_type, content_string = contents.split(',')

        decoded = base64.b64decode(content_string)
        decoded = str(decoded)
        file_handle_like = StringIO(decoded)

        # TODO: Figure out what's wrong here
        # sequence = FastaParser().read(f_handle=file_handle_like).top_sequence.seq

        return json.dumps('DUMMYSEQUENCE')

    if list_of_contents is not None:
        children = [parse_sequence(list_of_contents)]
        return children
