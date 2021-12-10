import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import scipy
from scipy.stats.kde import gaussian_kde
import pandas as pd
import numpy as np


df = px.data.election()
geojson = px.data.election_geojson()
candidates = df.winner.unique()

app = dash.Dash(__name__)
bw_list = [0.1, 0.5, 0.9]

app.layout = html.Div([
    html.Div([html.P("Candidate: ", style={'display': 'inline-block'}),
    dcc.RadioItems(
        id='candidate', 
        options=[{'value': x, 'label': x} 
                 for x in candidates],
        value=candidates[0],
        style={'display': 'inline-block'}
    )]),
    html.Div([
        dcc.Graph(id="map", style={'width': '50%', 'display': 'inline-block'}, clear_on_unhover=True),
        dcc.Graph(id="piechart", style={'width': '50%', 'display': 'inline-block'})
        ]),

], style={'width': '100%', 'display': 'inline-block'})

#callback for map
#listening from candidate ratio buttons
@app.callback(
    Output("map", "figure"), 
    [Input("candidate", "value")])
def display_choropleth(candidate):
    #print(candidate)
    fig = px.choropleth(
        df, geojson=geojson, color=candidate,
        locations="district", featureidkey="properties.district",
        range_color=[0, 6500],
        title = "Vote distribution of 58 districts")
    fig.update_geos(fitbounds="locations", visible=True)
    return fig

#Call back for piechart
#listening from two inputs (candidate radio buttons and map)
@app.callback(
    Output("piechart", "figure"), 
    [Input("candidate", "value"),
     Input("map", "hoverData")])
def county_piechart(candidate, hoverData):
    if hoverData is None:
        votes_sum = df.sum(numeric_only=True)
        votes = [votes_sum[x] for x in candidates]
        title = "Vote distribution"
    else:
        district = hoverData['points'][0]['location']
        row = df.loc[df['district'] == district]    
        votes = [row.iloc[0][x] for x in candidates]        
        title = "Vote distribution in " + district
    pull = [0.1 if x == candidate else 0 for x in candidates]
    fig = go.Figure(data=[go.Pie(labels=candidates, values=votes,
                                 title=title,
                                 pull=pull,
                                 textinfo='label+value+percent')])
    return fig




app.run_server(debug=False, host='0.0.0.0', port=80XX,
               threaded=True)
