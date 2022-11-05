# coding: utf-8

# In[13]:
import importlib
import dash
from dash import callback
from dash import html
from dash import dcc
from dash.dependencies import Output, Input, State

import dash_bootstrap_components as dbc
import sys
#sys.path.insert(0, 'D:\\Complete DataScience\\YTWebsiteDeploy\\pages\\Documents\\Packages')
sys.path.insert(0,'D:\\Complete DataScience\\RenderDeploy')
import Yotube_Module as YT

dash.register_page (__name__, path='/')

layout = html.Div (
    [
        html.H5 ("Here We Go....!!!",
                 style={"display": "flex", "justifyContent": "center", "color":"blue"}),
        dbc.InputGroup (
            [
                dbc.Input (
                    id="ticker-search3",
                    placeholder="Enter Channel ID",
                    style={"maxWidth": 400},
                ),
            ],
            style={"display": "flex", "justifyContent": "center",
                   "padding": "10px", "border-radius": "10px", "width": "100%"},
        ),
        html.Br (),
        html.Div ([
            dcc.Link (
                dbc.Button (children="submit", n_clicks=0, id="ticker-search2-btn"),
                id="ticker-search2-link",
                href="/",
            ),
        ],
            style={"display": "flex", "justifyContent": "center"},
        ),
        dbc.Row (
            dbc.Col (
                dcc.Loading (children=[
                    dbc.Col (id='table', style={"display": "flex", "justifyContent": "center","padding": "10px","color":"Red"})],
                    color='#119DFF',
                    type="dot", fullscreen=True)

            )
        ),
        html.P (
            [
                html.Span (
                    "How to get Channel ID",
                    id="tooltip-target",
                    style={"textDecoration": "underline", "cursor": "pointer"},
                ),
            ],
            style={"display": "flex", "justifyContent": "center", "padding": "10px"},
        ),
            dbc.Tooltip (
            "Go Youtube channel Which You want to see Data..."
            "Right click=>View Page Source..."
            "Press CTRL+F and type channelid click on '˅' symbol..."
            "Copy the content of Channel ID",
            target="tooltip-target",
            placement= 'right'
        ),
        html.A ("Didn't Get Watch here...", href="https://www.youtube.com/watch?v=D12v4rTtiYM", target="_blank",
                style={"display": "flex", "justifyContent": "center"}),
        dash.html.Footer(children='--Dikshit🤓',style={"clear": "both","position":"relative","margin-top": "350px",
                                                   "text-align": "center","font-size": "20px",
                                                    "color":"#FF4C11","font-family":"monospace"}),

    ],style={"background-image":"url('/assets/SM.png')","height":"100vh"}

)


@callback (
    Output ("ticker-search2-link", "href"),
    Output ("table", component_property='children'),
    Output ("ticker-search2-btn", component_property='children'),
    Output ("store-data", component_property='data'),
    [Input ("ticker-search2-btn", "n_clicks")],
    [State ('ticker-search3', component_property='value')],
    prevent_initial_call=True
)
def search (n_clicks, ticker):
    if ticker is None or ticker == "":

        return "", "Please Enter Channel ID", dash.no_update, ""
    else:
        try:
            dataframe=YT.getinfo(ticker)
            name=YT.getchannelname(ticker)
            subscount = YT.subscribercount (ticker)
            value = 'Success'
            store = {
                "data": dataframe.to_dict ("records"),
                "name":name,
                "subscount": subscount
            }
        except:

            return "", "Something Went Wrong", dash.no_update, ""

    return '/pages/hometestpage', value, "Click on to See...Results", store
