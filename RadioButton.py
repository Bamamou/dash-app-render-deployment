from dash import Dash, html, dcc, callback, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        dcc.RadioItems(
            id='radio-1',
            options=[
                {'label': 'Option 1A', 'value': '1A'},
                {'label': 'Option 1B', 'value': '1B'},
                {'label': 'Option 1C', 'value': '1C'}
            ],
            value=''
        ),
        html.Div(id='output-1')
    ]),
    html.Div([
        dcc.RadioItems(
            id='radio-2',
            options=[
                {'label': 'Option 2A', 'value': '2A'},
                {'label': 'Option 2B', 'value': '2B'},
                {'label': 'Option 2C', 'value': '2C'}
            ],
            value=''
        ),
        html.Div(id='output-2')
    ]),
    html.Div([
        dcc.RadioItems(
            id='radio-3',
            options=[
                {'label': 'Option 3A', 'value': '3A'},
                {'label': 'Option 3B', 'value': '3B'},
                {'label': 'Option 3C', 'value': '3C'}
            ],
            value=''
        ),
        html.Div(id='output-3')
    ])
])

@callback(
    Output('output-1', 'children'),
    Input('radio-1', 'value')
)
def update_output1(value):
    if value:
        return f'You selected: {value} from Radio 1'
    return 'Please select an option from Radio 1'

@callback(
    Output('output-2', 'children'),
    Input('radio-2', 'value')
)
def update_output2(value):
    if value:
        return f'You selected: {value} from Radio 2'
    return 'Please select an option from Radio 2'

@callback(
    Output('output-3', 'children'),
    Input('radio-3', 'value')
)
def update_output3(value):
    if value:
        return f'You selected: {value} from Radio 3'
    return 'Please select an option from Radio 3'

if __name__ == '__main__':
    app.run_server(debug=True)