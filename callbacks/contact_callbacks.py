from dash.dependencies import Input, Output
from app import app


@app.callback(Output('bug-alert', 'is_open'),
              [Input('issue-select', 'value')])
def toggle_alert(value):
    if value is not None and value == '1':
        return True
    else:
        return False
