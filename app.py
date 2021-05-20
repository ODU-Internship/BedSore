import os
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
pressure_data = np.random.randint(1000, size=(10, 10))
server = app.server

app.layout = html.Div([
    html.H2('Bed Pressure Status'),
    html.Div([
    dcc.Graph(id='bed_pressure'),
    dcc.Interval(id='graph-update', interval=5000, n_intervals=0)
    ], style={'width': '100%', 'display': 'inline-block', 'padding': '0 20'}),
])

@app.callback(
dash.dependencies.Output('bed_pressure','figure'),
[dash.dependencies.Input('graph-update','n_intervals')])
def update_graph(n):
    pressure_data = np.random.randint(1000, size=(15, 30))
    fig = px.imshow(pressure_data,color_continuous_scale='Hot_r')
    fig.update_layout(width=int(1000))

    print(pressure_data)
    #fig = px.imshow(pressure_data)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
