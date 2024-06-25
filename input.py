from dash import Dash, html, dcc, callback, Input, Output

app = Dash(__name__)
# Create a basic Dash app structure: with the layout
app.layout = html.Div([
    dcc.Input(id='my-input', value='initial value', type='text'),
    html.Div(id='my-output')
])
#Define a callback function using the @callback decorator:
@callback(
    Output('my-output', 'children'),
    Input('my-input', 'value')
)
def update_output(value):
    return f'You entered: {value}'

#Run the app:
if __name__ == '__main__':
    app.run_server(debug=True)