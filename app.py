import os
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import time

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#pressure_data = np.random.randint(1000, size=(10, 10))

a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0], [
    2, 3, 1, 4, 8], [4, 7, 9, 3, 2], [5, 7, 2, 9, 1]]
b = [[1, 2, 3, 4, 5], [4, 3, 2, 1, 0], [
    2, 3, 1, 4, 3], [4, 3, 9, 3, 2], [5, 6, 2, 2, 1]]
t = np.zeros((5, 5))

server = app.server

app.layout = html.Div([
    html.H2('Bed Pressure Status'),
    html.Div([
    dcc.Graph(id='bed_pressure'),
    html.Div(id = 'sen_alerts'),
    dcc.Interval(id='graph-update', interval=10000, n_intervals=0)
    ], style={'width': '100%', 'display': 'inline-block', 'padding': '0 20'}),
])

@app.callback(
[dash.dependencies.Output('bed_pressure','figure'),
dash.dependencies.Output('sen_alerts','children')],
[dash.dependencies.Input('graph-update','n_intervals')])
def update_graph(n):
    #pressure_data = np.random.randint(1000, size=(15, 30))
    a = np.random.randint(1000, size=(5, 5))
    alert_msg = detect(a,t)

    sens = html.Ul([html.Li(x) for x in alert_msg ])
    fig = px.imshow(a,color_continuous_scale='Hot_r')
    fig.update_layout(width=int(1000))


    #fig = px.imshow(pressure_data)
    return fig, sens


def detect(arr,t):
    sen_list = []
    for (x, y), element in np.ndenumerate(np.array(arr)):
        if(element > 400 and t[x][y] == 0.0):
            t[x][y] = time.time()
        elif(element > 400 and t[x][y] != 0):
            if(time.time() - t[x][y] > 9):
                sen_list.append("Alert of Sensor placed at " + str(x) + "," + str(y))
        elif(element <= 400):
            t[x][y] = 0.0
    return sen_list



if __name__ == '__main__':
    app.run_server(debug=True)
