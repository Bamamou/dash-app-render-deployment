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
# Remove the first colunm which has time and date
Data =Data.iloc[:, 1:]
def to_float(x):
    return float(x) if x != '' else np.nan
# Apply the conversion function to the entire DataFrame
Data = Data.map(to_float)
# Let's compute the voltage of each Cell an convert it to V
for col in Data.iloc[:, 29:56]:
    Data[col] =(Data[col]+200)/100
    Data.rename(columns={col:'String'+str(col-29)}, inplace = True)
# Let's also rename the temperature columns
for col in Data.iloc[:, 62:67]:
    Data.rename(columns={col:'Temperature'+str(col-62)}, inplace = True)


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