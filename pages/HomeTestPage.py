

import importlib

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output,Input
from dash import  callback

import dash_bootstrap_components as dbc
import dash_extensions as de

import sys

import sys
#sys.path.insert(0, 'D:\\Complete DataScience\\YTWebsiteDeploy\\pages\\Documents\\   Packages')
sys.path.insert(0,'D:\\Complete DataScience\\RenderDeploy')
import Tabs as tb
import pandas as pd
import time



url='https://assets4.lottiefiles.com/packages/lf20_3fuksula.json'
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))


dash.register_page(__name__,)


layout=html.Div([
            html.Div(de.Lottie(options=options, width="50%", height="50%", url=url),id='Loitte',hidden=False),
            dcc.Loading(children=[dbc.Row(id='testforlayout')],color='#119DFF',type="graph",fullscreen=True)


])



@callback(
         Output("content1", "children"),
         [Input("tabs", "active_tab")],
)
def switch_tab (tab_choosen):
    print('callback test')
    if tab_choosen == 'Home_Tab':
        return tb.Home_layout()
    elif tab_choosen == 'Trend_Tab':
        time.sleep (10)
        return tb.Trend_layout()
    elif tab_choosen == 'DataTable_Tab':
        time.sleep (10)
        return tb.Datatable_layout()



@dash.callback(
    Output("Loitte","hidden"),
    Output("testforlayout", "children"),
    Input("store-data",component_property='data'),
    #prevent_initial_call=True
)
#
def update(data):
     name=data.get('name')
     some=data.get("data")
     subcount=data.get("subscount")
     data1=pd.DataFrame(some)
     return True,tb.functionoflayout(data1,subcount,name)




