from dash import Dash, html, dcc, callback, Input, Output

app = Dash(__name__)

# Sample options for dropdowns
options = ['Option 1', 'Option 2', 'Option 3', 'Option 4']

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id='dropdown-1',
            options=[{'label': opt, 'value': opt} for opt in options],
            placeholder="Select an option for Dropdown 1"
        ),
        html.Div(id='output-1')
    ]),
    html.Div([
        dcc.Dropdown(
            id='dropdown-2',
            options=[{'label': opt, 'value': opt} for opt in options],
            placeholder="Select an option for Dropdown 2"
        ),
        html.Div(id='output-2')
    ]),
    html.Div([
        dcc.Dropdown(
            id='dropdown-3',
            options=[{'label': opt, 'value': opt} for opt in options],
            placeholder="Select an option for Dropdown 3"
        ),
        html.Div(id='output-3')
    ])
])

@callback(
    Output('output-1', 'children'),
    Input('dropdown-1', 'value')
)
def update_output1(value):
    if value:
        return f'You selected: {value} from Dropdown 1'
    return 'Please select an option from Dropdown 1'

@callback(
    Output('output-2', 'children'),
    Input('dropdown-2', 'value')
)
def update_output2(value):
    if value:
        return f'You selected: {value} from Dropdown 2'
    return 'Please select an option from Dropdown 2'

@callback(
    Output('output-3', 'children'),
    Input('dropdown-3', 'value')
)
def update_output3(value):
    if value:
        return f'You selected: {value} from Dropdown 3'
    return 'Please select an option from Dropdown 3'

if __name__ == '__main__':
    app.run_server(debug=True)