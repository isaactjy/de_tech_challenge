from datetime import datetime
from msilib.schema import Font
from tkinter import font
from dash import Dash, html, dcc
import plotly.express as px
import requests
import pandas as pd

start_date = '2020-01-01T00:00:00Z'
end_date = datetime.now().isoformat()

response = requests.get(f'https://api.covid19api.com/country/singapore?from={start_date}&to={end_date}')
df = pd.DataFrame.from_dict(response.json(), orient = 'columns')
df.to_csv('covid19_sg.csv')

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
fig = px.scatter(df, x="Date", y="Confirmed")

app.layout = html.Div(children=[
    html.H2(children='Confirmed Covid Cases in Singapore Over Time'),
    dcc.Graph(
        id = 'cases-graph',
        figure = fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)