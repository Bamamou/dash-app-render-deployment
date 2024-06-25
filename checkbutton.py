from dash import Dash, html, dcc, callback, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        dcc.Checklist(
            id='checklist-1',
            options=[{'label': 'Check 1', 'value': 'check1'}],
            value=[]
        ),
        html.Div(id='output-1')
    ]),
    html.Div([
        dcc.Checklist(
            id='checklist-2',
            options=[{'label': 'Check 2', 'value': 'check2'}],
            value=[]
        ),
        html.Div(id='output-2')
    ]),
    html.Div([
        dcc.Checklist(
            id='checklist-3',
            options=[{'label': 'Check 3', 'value': 'check3'}],
            value=[]
        ),
        html.Div(id='output-3')
    ])
])

@callback(
    Output('output-1', 'children'),
    Input('checklist-1', 'value')
)
def update_output1(value):
    if 'check1' in value:
        return 'Check 1 is checked'
    return 'Check 1 is unchecked'

@callback(
    Output('output-2', 'children'),
    Input('checklist-2', 'value')
)
def update_output2(value):
    if 'check2' in value:
        return 'Check 2 is checked'
    return 'Check 2 is unchecked'

@callback(
    Output('output-3', 'children'),
    Input('checklist-3', 'value')
)
def update_output3(value):
    if 'check3' in value:
        return 'Check 3 is checked'
    return 'Check 3 is unchecked'

if __name__ == '__main__':
    app.run_server(debug=True)