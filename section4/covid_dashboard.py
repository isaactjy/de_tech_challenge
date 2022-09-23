from datetime import datetime
from msilib.schema import Font
from tkinter import font
from dash import Dash, html, dcc
import plotly.express as px
import requests
import pandas as pd

start_date = '2020-01-01T00:00:00Z'
end_date = datetime.now().isoformat()

response = requests.get(f'https://api.covid19api.com/country/singapore/status/confirmed?from={start_date}&to={end_date}')
df = pd.DataFrame.from_dict(response.json(), orient = 'columns')
df['NewCases'] = df['Cases'].shift(1)
df['NewCases'] = df['NewCases'].fillna(0)
df['NewCases'] = df['Cases'] - df['NewCases']
df.to_csv('section4/covid19_sg.csv')

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
total_cases_fig = px.bar(df, x="Date", y="Cases").update_layout(
    xaxis = {
        'rangeselector': {
            'buttons': [
                {
                    'count': 1,
                    'label': '1m',
                    'step': 'month',
                    'stepmode': 'backward'
                },
                {
                    'count': 3,
                    'label': '3m',
                    'step': 'month',
                    'stepmode': 'backward'
                },
                {
                    'count': 6,
                    'label': '6m',
                    'step': 'month',
                    'stepmode': 'backward'
                },
                {
                    'count': 1,
                    'label': 'YTD',
                    'step': 'year',
                    'stepmode': 'backward'
                },
            ]
        },
        'rangeslider': {'visible': True}
    }
)

new_cases_fig = px.bar(df, x="Date", y="NewCases").update_layout(
    xaxis = {
        'rangeselector': {
            'buttons': [
                {
                    'count': 1,
                    'label': '1m',
                    'step': 'month',
                    'stepmode': 'backward'
                },
                {
                    'count': 3,
                    'label': '3m',
                    'step': 'month',
                    'stepmode': 'backward'
                },
                {
                    'count': 6,
                    'label': '6m',
                    'step': 'month',
                    'stepmode': 'backward'
                },
                {
                    'count': 5,
                    'label': 'YTD',
                    'step': 'year',
                    'stepmode': 'backward'
                },
            ]
        },
        'rangeslider': {'visible': True}
    }
)

app.layout = html.Div(children=[
    html.H2(children='Confirmed Covid Cases in Singapore Over Time'),
    dcc.Graph(
        id = 'total-cases-graph',
        figure = total_cases_fig
    ),
    dcc.Graph(
        id = 'new-cases-graph',
        figure = new_cases_fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)