import dash_bootstrap_components as dbc
import dash_html_components as html
from components import HelpToolTip, GitHubLink, ConPlotLink
from utils import UrlIndex


def Header():
    return dbc.Navbar(
        [
            ConPlotLink(),
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(GitHubLink(), id="navbar-collapse", navbar=True),
        ],
    )


def DisplayControlHeader():
    return html.H4(className="card-text", style={'text-align': "center"},
                   children=HelpToolTip(id='display-control',
                                        text='Display control ',
                                        msg='Here you can adjust the layout of your plot after it is '
                                            'generated. Just adjust the parameters of interest and click on'
                                            ' the refresh button.'))


def AdditionalInputHeader():
    return html.H4(className="card-text", style={'text-align': "center"},
                   children=HelpToolTip(id='additional-input',
                                        text="Additional tracks ",
                                        msg='Here you can upload files with the data for additional tracks of '
                                            'information to be displayed on your plot. Remember that you will need '
                                            'to select a track format before attempting to upload a file!'))


def MandatoryInputHeader():
    return html.H4(className="card-text", style={'text-align': "center"},
                   children=HelpToolTip(id='required-input',
                                        text="Required input ",
                                        example_url=UrlIndex.STATIC_DATA.value,
                                        msg='A sequence and a contact map are the minimum two inputs '
                                            'required to produce a plot. Remember that you need to select a '
                                            'format before attempting to upload the contact map!'))