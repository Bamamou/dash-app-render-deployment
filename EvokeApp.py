import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import plotly.express as px


df = pd.read_csv('Balistron1.txt')
# Iterate through each column
for col in df.columns:
    Data =df[col].str.split(';', expand=True)
# All the 28 Strings voltages
for col in df.columns:
    Strings = ((Data.iloc[:, 30:57].astype(float))+200)/100
# All 6 temp probe and the max, min temp 
for col in df.columns:
    Temperatures = Data.iloc[:, 63:68].astype(float)
# Rename some of the data for easy access
Data.rename(columns = {29:'Pack Voltage', 9:'boardTemperature', 10:'boardSupplyVoltage', 11:'odometerKm', 12:'tripKm', 13:'speedKmh',
                       14:'maximumSpeed',  16: 'efficiency', 17:'vehicleStatuByte1', 18:'vehicleStatuByte2', 69:'SOC', 62:'Pack_DSG_Current',
                       85:'Invt_Temp', 83:'RPM', 81:'MCU_Voltage', 84:'Motor_Temp'}, inplace = True)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("Evoke Motorcylces Data visualization"),
    dcc.Dropdown(
        id='column-dropdown',
        options=[{'label': col, 'value': col} for col in Data.columns],
        value=Data.columns[15],
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
    fig = px.line(Data, y=selected_column, title=f'{selected_column} Over Time')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)