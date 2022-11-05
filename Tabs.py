
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import YoutubeAnalyticsTest as YTA
import Datatest as dt


def functionoflayout (data1,subs,name):
    global Home_layout
    global Trend_layout
    global Datatable_layout
    colors = {
        'background': '#111111',
        'bodyColor': '#F2DFCE',
        'text': '#7FDBFF'
    }

    def generate_card_content (card_header, card_value):
        card_head_style = {'textAlign': 'center', 'fontSize': '150%'}
        card_body_style = {'textAlign': 'center', 'fontSize': '200%'}
        card_header = dbc.CardHeader (card_header, style=card_head_style)
        card_body = dbc.CardBody (
            [
                html.H5 (f"{int (card_value):,}", className="card-title", style=card_body_style),

            ]
        )
        card = [card_header, card_body]
        return card

    def generate_cards ():
        Total_videos = data1.shape[0]
        Total_View = data1['View_count'].sum ()
        CN = name
        cards = html.Div (
            [
                dbc.Row (
                    [
                        html.H2 ("Channel Name:" + CN, style={'textAlign': 'center', 'color': 'Red'}),
                        html.Hr (),
                        dbc.Col (
                            dbc.Card (generate_card_content ("Total View Count", Total_View), color="success",
                                      inverse=True),
                            md=dict (size=2, offset=3)),
                        dbc.Col (
                            dbc.Card (generate_card_content ("Total Videos", Total_videos), color="warning",
                                      inverse=True),
                            md=dict (size=2)),
                        dbc.Col (dbc.Card (generate_card_content ("Total Subscribers", subs), color="dark", inverse=True),
                                 md=dict (size=2)),
                    ],
                    className="mb-4",
                ),
            ], id='card1'
        )
        return cards

    def tab1 ():
        tab1_content = dbc.Card (
            dbc.CardBody (
                [

                    generate_cards (),

                ]
            ),
        )
        return tab1_content

    def tab2 ():
        tab2_content = dbc.Card (
            dbc.CardBody (
                [
                    YTA.teslayout (data1)

                ]
            ),
        )
        return tab2_content

    def tab3 ():
        tab3_content = dbc.Card (
            dbc.CardBody (
                [
                    html.Div (
                        dbc.Row (
                            [

                                dbc.Label ("1.Videos with Million Views will be highlighted in Green Color",
                                           color='Red'),
                                dbc.Label ("2.Any Column Fields can be Sorted(Ascending/Descending) using Arrorw Mark",
                                           color='Red'),
                                html.Br(),

                                dbc.Col (

                                    dt.table (data1)

                                )
                            ])
                    )

                ]
            ),
        )
        return tab3_content

    # -----------------------------------------------------------------------------------------------------

    def app_tabs ():
        app_tabs = html.Div ([
            dbc.Tabs ([
                dbc.Tab (label="Home", tab_id='Home_Tab'),
                dbc.Tab (label="Trends", tab_id='Trend_Tab'),
                dbc.Tab (label="DataTable", tab_id='DataTable_Tab'),
            ],
                id="tabs",
                active_tab="Home_Tab"
            ),
        ], className="mt-3"
        )
        return app_tabs

    def Home_layout ():
        Home_layout = html.Div (
            dbc.Row (
                [
                    dbc.Col (
                        dcc.Loading (children=tab1 (), type='graph', fullscreen=True, )

                    )

                ])
        )
        return Home_layout

    def Trend_layout ():
        Trend_Layout = html.Div (

            dbc.Row (
                [
                    dbc.Col (
                        # tab2_content
                        tab2 ()
                        #dcc.Loading (children=tab2 (), type='graph', fullscreen=True, )
                        # html.Label('This should be return for Trend layout')

                    ),

                ])
        )
        return Trend_Layout

    def Datatable_layout ():
        Datatable_layout = html.Div (
            dbc.Row (
                [
                    dbc.Col (
                        tab3 ()
                    ),

                ])
        )
        return Datatable_layout

    # --------------------------------------------------------------------------------------------------
    def generatelayout ():
        layout = dbc.Container (
            [
                dbc.Row (
                    dbc.Col (app_tabs (), width=12), className="mt-3"),
                html.Div (id='content1'),
            ], fluid=True, style={'backgroundColor': colors['bodyColor']}
        )
        return layout

    layout = generatelayout ()
    return layout
