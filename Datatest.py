
from dash import dash_table


def table(data):
    testdata1 = data.copy ()
    appenddate=[]
    def display_links ():
        rows = []
        links = testdata1['url'].to_list ()
        for x in links:
            link = "<a href='{}/' target='_blank'>{}/</a>".format (x, x)
            rows.append (link)
        return rows

    for i in testdata1['Published_Date']:
        some = i.split ('T')[0]
        appenddate.append(some)

    testdata1['Published_Date'] = appenddate
    testdata1['url'] = display_links ()

    df = dash_table.DataTable (testdata1.to_dict ('records'),
                               export_format="csv",
                               sort_action='native',
                               columns=[
                                   {"id": i, "name": i, "presentation": "markdown"} if i == 'url' else {"id": i,
                                                                                                        "name": i} for i
                                   in testdata1.columns
                               ],
                               markdown_options={"html": True},

                               page_size=50,
                               style_data_conditional=[
                                   {
                                       'if':
                                           {
                                               'filter_query': '{Videos_with_Mill} =1',
                                               'column_id': 'View_count'
                                           },
                                       'color': 'green',
                                       'fontWeight': 'bold'
                                   }, ],
                               style_cell={'textAlign': 'left'},
                               style_data={'border': '1px solid black',
                                           'backgroundColor': 'rgb(50, 50, 50)',
                                           'color': 'white'
                                           },
                               fixed_columns={'headers': True, 'data': 2},
                               style_table={'minWidth': '100%'},
                               style_header={'border': '1px solid black'},

                               ),

    return df




