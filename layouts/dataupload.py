import base64
from conkit.io.psicov import PsicovParser
from conkit.io.fasta import FastaParser
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from components import NavBar, Header, PathIndex
from app import app, cache
import pandas as pd
import json
from io import StringIO
import dash_bootstrap_components as dbc
from components import FastaUploadCard, ContactUploadCard
from Bio import SeqIO


def DataUpload(session_id):
    cache.clear()

    return html.Div([
        Header(),
        NavBar(PathIndex.DATAUPLOAD.value),
        html.Div(
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
                dcc.Link([dbc.Button("Plot", id='plot-button', color="primary", block=True)],
                         href=PathIndex.PLOTDISPLAY.value),
                html.Div(id='_cmap', style={'display': 'none'}),
                html.Div(id='_fasta', style={'display': 'none'}),
            ]
        )
    ])


@app.callback(Output('_cmap', 'children'),
              [Input('upload-contact-map', 'contents')],
              [State('session-id', 'children')])
def upload_contacts(list_of_contents, session_id):
    def parse_contacts(contents):
        content_type, content_string = contents.split(',')

        decoded = base64.b64decode(content_string)
        decoded = str(decoded)

        cmap = PsicovParser().read(f_handle=decoded.split('\\n')).top_map
        return pd.DataFrame(cmap.as_list())

    if list_of_contents is not None:
        cache.set('contacts-{}'.format(session_id), parse_contacts(list_of_contents))
        return None


@app.callback(Output('_fasta', 'children'),
              [Input('upload-fasta', 'contents')],
              [State('session-id', 'children')])
def upload_sequence(list_of_contents, session_id):
    def parse_sequence(contents):
        content_type, content_string = contents.split(',')

        decoded = base64.b64decode(content_string)
        decoded = str(decoded)
        file_handle_like = StringIO(decoded)

        # TODO: Figure out what's wrong here
        # sequence = FastaParser().read(f_handle=file_handle_like).top_sequence.seq

        return json.dumps('DUMMYSEQUENCE')

    if list_of_contents is not None:
        cache.set('fasta-{}'.format(session_id), parse_sequence(list_of_contents))
        return None


# TODO: Need to check user input for contacts!

@app.callback([Output("fasta-text-area", "valid"),
               Output("fasta-text-area", "invalid"),
               Output("fasta-collapse", "is_open")],
              [Input("fasta-text-area", "value")])
def is_valid_fasta(contents):
    if contents is None:
        return False, False, False
    # TODO: Need to capture invalid residues in the sequence
    fasta = SeqIO.parse(StringIO(contents), "fasta")
    if any(fasta):
        return True, False, False
    else:
        return False, True, True


@app.callback([Output("format-badge", "style")],
              [Input("contact-format-select", "value")])
def is_valid_fasta(format_selection):
    if format_selection is not None:
        return [{'display': 'none'}]
    else:
        return [None]
