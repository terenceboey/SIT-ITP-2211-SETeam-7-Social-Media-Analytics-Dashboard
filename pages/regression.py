import dash
import os
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from dash import dash_table, dcc, html, Input, Output
import dash_bootstrap_components as dbc

dash.register_page(__name__)

layout = html.Div([

    html.Div([
        html.Div([
        ],
            className="one-third column",
        ),
        html.Div([
            html.Div([
                html.H3("Weighted Regression Analysis", style={
                        "margin-bottom": "0px", 'color': 'white', 'font-weight': 'bold'})
            ])
        ], className="twelve column", id="title"),

        html.Div([

        ], className="one-third column", id='title1'),

    ], id="header", className="row flex-display", style={"margin-bottom": "25px"}),

    html.Div([
        dcc.Dropdown(options=[
            {'label': html.Div(['Overall Healthcare Workers'], style={
                               'color': 'orange', 'font-size': 20}), 'value': 'hw'},
            {'label': html.Div(['Appreciation campaign'], style={
                               'color': 'orange', 'font-size': 20}), 'value': 'Appreciate'},
            {'label': html.Div(['Gift campaign'], style={
                               'color': 'orange', 'font-size': 20}), 'value': 'Gift'},
            {'label': html.Div(['Donation campaign'], style={
                               'color': 'orange', 'font-size': 20}), 'value': 'Donation'},
            {'label': html.Div(['Benefit campaign'], style={
                               'color': 'orange', 'font-size': 20}), 'value': 'Benefit'},
            {'label': html.Div(['Support campaign'], style={
                               'color': 'orange', 'font-size': 20}), 'value': 'Support'},
        ], value='reg_model', placeholder="Choose an option", id='reg-dropdown', style={"color": "white"}),
        html.Div(id='reg-output-container', style={"paddingBottom": "1.5%"})
    ]),

    html.Div([
        dcc.Dropdown(options=[], value='reg_plot', placeholder="Choose a bubble plot graph",
                     id='plot-dropdown', style={"color": "white"}),
        html.Div(id='plot-output-container')
    ]),

    html.Div([
        html.Img(id='plot-img', src='about:blank', style={'width': '100%'})
    ], className="card_container twelve columns",
    ),

    html.Div([
        html.H6(children='Hofstede Dimensions Weighted CSV (1)',
                style={
                    'textAlign': 'center',
                    'color': 'white'}
                ),
        dash_table.DataTable(
            editable=False,
            column_selectable="single",
            row_deletable=False,
            style_cell={
                'textAlign': 'left',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
                'maxWidth': 100
            },
            style_header={
                'backgroundColor': 'paleturquoise',
                'color': 'black',
                'font-size': '18px',
                'fontWeight': 'bold'
            },
            style_data={
                'color': 'black',
                'backgroundColor': 'lavender',
                'font-size': '16px',
            },
            id='reg_datatable1'
        ),
        html.P(f'HPD = Hofstede Power Distance; HUA = Hofstede Uncertainty Avoidance; HIC = Hofstede Individualism vs Collectivism; HMF = Hofstede Masculinity vs Feminity; HLSO = Hofstede Longterm vs Shortterm Orientation;',
               style={
                   'textAlign': 'center',
                   'color': 'white'}
               )

    ], className="card_container twelve columns",
    ),

    html.Div([
        html.H6(children='GLOBE Practices Dimensions Weighted CSV (2)',
                style={
                    'textAlign': 'center',
                    'color': 'white'}
                ),
        dash_table.DataTable(
            editable=False,
            column_selectable="single",
            row_deletable=False,
            style_cell={
                'textAlign': 'left',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
                'maxWidth': 100
            },
            style_header={
                'backgroundColor': 'paleturquoise',
                'color': 'black',
                'font-size': '18px',
                'fontWeight': 'bold'
            },
            style_data={
                'color': 'black',
                'backgroundColor': 'lavender',
                'font-size': '16px',
            },
            id='reg_datatable2'
        ),
        html.P(f'GAP = GLOBE Assertiveness Practice; GICP = GLOBE Institutional Collectivism Practices; GIGCP = GLOBE In-Group Collectivism Practices; GFOP = GLOBE Future Orientation Practices; GGEP = GLOBE Gender Egalitarian Practices; GHOP = GLOBE Human Orientation Practices; GPOP = GLOBE Performance Orientation Practices; GPDP = GLOBE Power Distance Practices; GUAP = GLOBE Uncertainty Avoidance Practices',
               style={
                   'textAlign': 'center',
                   'color': 'white'}
               )
    ], className="card_container twelve columns",
    ),

    html.Div([
        html.H6(children='GLOBE Values Dimensions Weighted CSV (3)',
                style={
                    'textAlign': 'center',
                    'color': 'white'}
                ),
        dash_table.DataTable(
            editable=False,
            column_selectable="single",
            row_deletable=False,
            style_cell={
                'textAlign': 'left',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
                'maxWidth': 100
            },
            style_header={
                'backgroundColor': 'paleturquoise',
                'color': 'black',
                'font-size': '18px',
                'fontWeight': 'bold'
            },
            style_data={
                'color': 'black',
                'backgroundColor': 'lavender',
                'font-size': '16px',
            },
            id='reg_datatable3'
        ),
        html.P(f'GAV = GLOBE Assertiveness Values; GICV = GLOBE Institutional Collectivism Values; GIGCV = GLOBE In-Group Collectivism Values; GFOV = GLOBE Future Orientation Values; GGEV = GLOBE Gender Egalitarian Values; GHOV = GLOBE Human Orientation Values; GPOV = GLOBE Performance Orientation Values; GPDV = GLOBE Power Distance Values; GUAV = GLOBE Uncertainty Avoidance Values',
               style={
                   'textAlign': 'center',
                   'color': 'white'}
               )
    ], className="card_container twelve columns",
    ),

    html.Div([
        html.H6(children='Schwartz Dimensions Weighted CSV (4)',
                style={
                    'textAlign': 'center',
                    'color': 'white'}
                ),
        dash_table.DataTable(
            editable=False,
            column_selectable="single",
            row_deletable=False,
            style_cell={
                'textAlign': 'left',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
                'maxWidth': 100
            },
            style_header={
                'backgroundColor': 'paleturquoise',
                'color': 'black',
                'font-size': '18px',
                'fontWeight': 'bold'
            },
            style_data={
                'color': 'black',
                'backgroundColor': 'lavender',
                'font-size': '16px',
            },
            id='reg_datatable4'
        ),
        html.P(f'SCHA = Schwartz Harmony; SCEM = Schwartz Embedded; SCHI = Schwartz Hierarchy; SCM = Schwartz Mastery; SCAA = Schwartz Affective Autonomy; SCIA = Schwartz Intellectual Autonomy; SCEG = Schwartz Eglitarianism',
               style={
                   'textAlign': 'center',
                   'color': 'white'}
               )
    ], className="card_container twelve columns",
    ),

    dcc.Link(html.Button("DASHBOARD PAGE", style={
        'textAlign': 'center',
        "width": "100%",
        "color": 'black',
        "font-size": 16,
        'backgroundColor': '#98F5FF',
    }), href="/dashboard", refresh=True),
])


@dash.callback(
    Output('plot-img', 'src'),
    Input('plot-dropdown', 'value')
)
def update_plot_img(imgFileName):
    return imgFileName


@dash.callback(
    Output('reg_datatable1', 'data'),
    Output('reg_datatable2', 'data'),
    Output('reg_datatable3', 'data'),
    Output('reg_datatable4', 'data'),
    Output('plot-dropdown', 'options'),
    Input('reg-dropdown', 'value')
)
def update_reg_data(reg):
    if reg == "hw":
        imgList = os.listdir(
            f"dashboard/assets/Regression Analysis Graphs/Regression Analysis Graphs/overall healthcare worker bubble plot pictures/")
        items = []
        x = 1
        for img in imgList:
            items.append(
                {'label': html.Div([img], style={
                    'color': 'orange', 'font-size': 20}), 'value': 'assets/Regression Analysis Graphs/Regression Analysis Graphs/overall healthcare worker bubble plot pictures/'+img}
            )
            x += 1
        camp = 'Overall healthcare worker'
        fileSelected1 = pd.read_csv('dashboard/assets/WeightedCSV/WeightedCSV/'+camp +
                                    '/Table of Healthcare Worker Tweet Sentiments Regression Model (All Countries +  Weighted Proportion)1 - Sheet1.csv')
        fileSelected2 = pd.read_csv('dashboard/assets/WeightedCSV/WeightedCSV/'+camp +
                                    '/Table of Healthcare Worker Tweet Sentiments Regression Model (All Countries +  Weighted Proportion)2 - Sheet1.csv')
        fileSelected3 = pd.read_csv('dashboard/assets/WeightedCSV/WeightedCSV/'+camp +
                                    '/Table of Healthcare Worker Tweet Sentiments Regression Model (All Countries +  Weighted Proportion)3 - Sheet1.csv')
        fileSelected4 = pd.read_csv('dashboard/assets/WeightedCSV/WeightedCSV/'+camp +
                                    '/Table of Healthcare Worker Tweet Sentiments Regression Model (All Countries +  Weighted Proportion)4 - Sheet1.csv')
        return fileSelected1.to_dict(orient='records'), fileSelected2.to_dict(orient='records'), fileSelected3.to_dict(orient='records'), fileSelected4.to_dict(orient='records'), items
    else:
        try:

            items = []
            camp = reg
            imgList = os.listdir(
                f'dashboard/assets/Regression Analysis Graphs/Regression Analysis Graphs/'+camp+' bubble plot pictures/')
            x = 1
            for img in imgList:
                items.append(
                    {'label': html.Div([img], style={
                        'color': 'orange', 'font-size': 20}), 'value': 'assets/Regression Analysis Graphs/Regression Analysis Graphs/'+camp+' bubble plot pictures/'+img}
                )
                x += 1
            fileSelected1 = pd.read_csv('dashboard/assets/WeightedCSV/WeightedCSV/'+camp +
                                        '/Table of Campaigns Regression Model ('+camp+' Campaign + Weighted Proportion)1 - Sheet1.csv')
            fileSelected2 = pd.read_csv('dashboard/assets/WeightedCSV/WeightedCSV/'+camp +
                                        '/Table of Campaigns Regression Model ('+camp+' Campaign + Weighted Proportion)2 - Sheet1.csv')
            fileSelected3 = pd.read_csv('dashboard/assets/WeightedCSV/WeightedCSV/'+camp +
                                        '/Table of Campaigns Regression Model ('+camp+' Campaign + Weighted Proportion)3 - Sheet1.csv')
            fileSelected4 = pd.read_csv('dashboard/assets/WeightedCSV/WeightedCSV/'+camp +
                                        '/Table of Campaigns Regression Model ('+camp+' Campaign + Weighted Proportion)4 - Sheet1.csv')
            return fileSelected1.to_dict(orient='records'), fileSelected2.to_dict(orient='records'), fileSelected3.to_dict(orient='records'), fileSelected4.to_dict(orient='records'), items
        except:
            items = []
            fileSelected1 = pd.DataFrame()
            fileSelected2 = pd.DataFrame()
            fileSelected3 = pd.DataFrame()
            fileSelected4 = pd.DataFrame()

            return fileSelected1.to_dict(orient='records'), fileSelected2.to_dict(orient='records'), fileSelected3.to_dict(orient='records'), fileSelected4.to_dict(orient='records'), items
