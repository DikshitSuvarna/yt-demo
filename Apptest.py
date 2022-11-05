import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

colors = {
    'background': '#111111',
    'bodyColor': '#F2DFCE',
    'text': '#7FDBFF'
}


def get_page_heading_style ():
    return {'backgroundColor': colors['background']}


def get_page_heading_title ():
    return html.H1 (children='YOUTUBE DATA',
                    style={
                        'textAlign': 'center',
                        'color': colors['text']
                    })


def get_page_heading_subtitle ():
    return html.Div (children='Insight of Youtube channels',
                     style={
                         'textAlign': 'center',
                         'color': colors['text']
                     })


def get_page_color ():
    return {'bodyColor': colors['bodyColor']}  ##Testing Purpose


def generate_page_header ():
    main_header = dbc.Row (
        [
            dbc.Col (get_page_heading_title (), md=12)
        ],
        align="center",
        style=get_page_heading_style ()
    )
    subtitle_header = dbc.Row (
        [
            dbc.Col (get_page_heading_subtitle (), md=12)
        ],
        align="center",
        style=get_page_heading_style ()
    )
    header = (main_header, subtitle_header)
    return header


app = dash.Dash (__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True,
                 update_title='Loading Components... Please wait..',
                 suppress_callback_exceptions=True,
                 # meta_tags=[{'name':'viewport',
                 #             'content':'width=device-width,initial-scale=1.0,maximum-scale=1.2,minimum-scale=0.5,'}],
                 meta_tags=[{"name": "viewport",
                             "content": "width=device-width,initial-scale=1.0,user-scalable=1.0, minimum-scale=1.0, maximum-scale=1.0,orientation=landscape"}]
                 )

server = app.server

page_header = generate_page_header ()
app.layout = html.Div ([
    # get_page_color(),
    page_header[0],
    page_header[1],

    # html.Hr (),
    # html.Div(id='test'),
    html.Div ([
        print (dcc.Link (page['name'] + " | ", href=page['path']))
        # dcc.Link(href=page['path'])
        for page in dash.page_registry.values ()
    ]
    ),
    dcc.Store (id='store-data', data={}, storage_type='session'),
    dash.page_container
]
)

# In[ ]:

if __name__ == '__main__':
    # app.run_server (debug=False,port=3006, threaded=True)
    app.run (debug=False)

# In[ ]:
