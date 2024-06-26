import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import plotly.express as px


# Create a sample DataFrame
df = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', end='2023-12-31', freq='D'),
    'Temperature': np.random.randn(365).cumsum(),
    'Humidity': np.random.randn(365).cumsum(),
    'Pressure': np.random.randn(365).cumsum()
})
df.set_index('Date', inplace=True)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("DataFrame Column Plotter"),
    dcc.Dropdown(
        id='column-dropdown',
        options=[{'label': col, 'value': col} for col in df.columns],
        value=df.columns[0],
        clearable=False
    ),
    dcc.Graph(id='line-plot')
])

# Define the callback to update the graph
@app.callback(
    Output('line-plot', 'figure'),
    Input('column-dropdown', 'value')
)
def update_graph(selected_column):
    fig = px.line(df, y=selected_column, title=f'{selected_column} Over Time')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)