from dash import Dash, html, dcc, callback, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.Button('Button 1', id='btn-1', n_clicks=0),
    html.Button('Button 2', id='btn-2', n_clicks=0),
    html.Button('Button 3', id='btn-3', n_clicks=0),
    html.Div(id='output-1'),
    html.Div(id='output-2'),
    html.Div(id='output-3')
])

@callback(
    Output('output-1', 'children'),
    Input('btn-1', 'n_clicks')
)
def update_output1(n_clicks):
    if n_clicks > 0:
        return f'Button 1 has been clicked {n_clicks} times.'
    return 'Button 1 has not been clicked yet.'

@callback(
    Output('output-2', 'children'),
    Input('btn-2', 'n_clicks')
)
def update_output2(n_clicks):
    if n_clicks > 0:
        return f'Button 2 has been clicked {n_clicks} times.'
    return 'Button 2 has not been clicked yet.'

@callback(
    Output('output-3', 'children'),
    Input('btn-3', 'n_clicks')
)
def update_output3(n_clicks):
    if n_clicks > 0:
        return f'Button 3 has been clicked {n_clicks} times.'
    return 'Button 3 has not been clicked yet.'

if __name__ == '__main__':
    app.run_server(debug=True)