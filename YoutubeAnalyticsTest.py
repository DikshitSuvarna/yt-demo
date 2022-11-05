

import dash
import plotly.express as px
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import GraphsModule12 as GM




app = dash.Dash(__name__)
def teslayout(value):
    data=value
    testdf=data.groupby('Year').sum().reset_index()
    #Years
    videos_Uploaded_in_Year=GM.Videos_Uploaded_in_Year(data)
    Views_in_Year=GM.Views_in_Year(data)
    Average_views=GM.Average_views(data)
    LikeRatio=dbc.Col([dcc.Graph(figure=px.pie(data_frame=testdf,names='Year',values='LikeRatio',title='Total No Views By Like count in given Year'))],width=6)

    #Months
    Videos_uploaded_in_Month=GM.formonths(data)
    Videos_Viewd_in_Month=GM.formonthsViews(data)

    #Weeks
    Videos_Uploaded_in_Week=GM.Videos_Uploaded_in_Week(data)
    Million_view_in_Week=GM.Million_per_weeks(data)

    #Duration
    Video_Duration_count=GM.showDurationsum(data)
    Video_Duration_view=GM.showDurationViews(data)

    Analytics_layout=html.Div([
        
        dbc.Row(
            [

                html.H3('All About Year',style={"color":"Red"}),
                dbc.Col([dcc.Graph(figure=videos_Uploaded_in_Year)],width=6),
                LikeRatio,
                html.Hr()
        
                ]
                
            
         ),
        dbc.Row(
            [
               dbc.Col([dcc.Graph(figure=Views_in_Year)],width=6),
               dbc.Col([dcc.Graph(figure=Average_views)],width=6),
               html.Hr()
            ]
                
        ),
        dbc.Row(
            [
               html.H3('All About Months',style={"color":"Red"}),
               dbc.Col([dcc.Graph(figure=Videos_uploaded_in_Month)],width=6),
               dbc.Col([dcc.Graph(figure=Videos_Viewd_in_Month)],width=6),
               html.Hr()
            ]
                
        ),
        dbc.Row(
            [
               html.H3('All About Weeks',style={"color":"Red"}),
               dbc.Col([dcc.Graph(figure=Videos_Uploaded_in_Week)],width=6),
               dbc.Col([dcc.Graph(figure=Million_view_in_Week)],width=6),
               html.Hr()
            ]
                
        ),
         dbc.Row(
            [
               html.H3('All About Video Duration',style={"color":"Red"}),
               dbc.Label('**N/A Videos is less than 1 Minute',style={"color":"green"}),
               dbc.Label('**Short Videos is approx 10 Minutes',style={"color":"green"}),
               dbc.Label('**Medium is 10-20 Mins and Long is 20 and more respectively',style={"color":"green"}),
               dbc.Label('**Ultimate is 1 Hour or more than that..',style={"color":"green"}),
               dbc.Col([dcc.Graph(figure=Video_Duration_count)],width=6),
               dbc.Col([dcc.Graph(figure=Video_Duration_view)],width=6),
               html.Hr()
            ]
                
        ),
        
        
        
    ])
    return Analytics_layout




