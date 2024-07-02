import dash
from dash import html, dcc, callback, Output, Input, State
import base64
import io
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Button("Upload", id="upload-button", n_clicks=0),
    dcc.Upload(
        id="upload-data",
        children=[html.Div(["Drag and Drop or ", html.A("Select Files")])],
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'display': 'none',
        },
        multiple=False
    ),
    html.Div(id="output-data-upload"),
    html.Div([
        dcc.Dropdown(id='column-selector', multi=True, placeholder="Select columns to plot"),
        dcc.Graph(id='line-plot')
    ], style={'display': 'none'}, id='plot-container')
])

@callback(
    Output("upload-data", "style"),
    Input("upload-button", "n_clicks"),
    prevent_initial_call=True
)
def open_file_dialog(n_clicks):
    if n_clicks > 0:
        return {'width': '100%', 'height': '60px', 'lineHeight': '60px', 'borderWidth': '1px',
                'borderStyle': 'dashed', 'borderRadius': '5px', 'textAlign': 'center', 'display': 'block'}

@callback(
    Output("output-data-upload", "children"),
    Output("column-selector", "options"),
    Output("plot-container", "style"),
    Input("upload-data", "contents"),
    State("upload-data", "filename")
)
def update_output(contents, filename):
    if contents is None:
        return "No file uploaded yet.", [], {'display': 'none'}
    
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    
    try:
        if 'txt' in filename:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')), sep=';')
        else:
            return "Please upload a CSV file.", [], {'display': 'none'}
    except Exception as e:
        return f"There was an error processing this file: {e}", [], {'display': 'none'}

    columns = [{'label': col, 'value': col} for col in df.columns]

    return html.Div([
        html.H5(f"File: {filename}"),
        html.H6("Data Preview:"),
        dash.dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns],
            page_size=10
        ),
        dcc.Store(id='dataframe-store', data=df.to_json(date_format='iso', orient='split'))
    ]), columns, {'display': 'block'}

@callback(
    Output('line-plot', 'figure'),
    Input('column-selector', 'value'),
    Input('dataframe-store', 'data')
)
def update_graph(selected_columns, json_data):
    if not selected_columns or not json_data:
        return px.line()  # Return an empty figure if no columns are selected or no data is available

    df = pd.read_json(json_data, orient='split')
    fig = px.line(df, y=selected_columns)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)