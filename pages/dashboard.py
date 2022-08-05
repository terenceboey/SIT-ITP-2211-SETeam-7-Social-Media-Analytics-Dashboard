import dash
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from dash import dash_table, dcc, html, Input, Output
import dash_bootstrap_components as dbc

tweets = 0
# Sentiment Data
sentidf_appreciation = pd.read_excel(
    'dashboard/assets/sentiment.xlsx', sheet_name='appreciation')
sentidf_gift = pd.read_excel(
    'dashboard/assets/sentiment.xlsx', sheet_name='gift')
sentidf_donation = pd.read_excel(
    'dashboard/assets/sentiment.xlsx', sheet_name='donation')
sentidf_benefit = pd.read_excel(
    'dashboard/assets/sentiment.xlsx', sheet_name='benefit')
sentidf_support = pd.read_excel(
    'dashboard/assets/sentiment.xlsx', sheet_name='support')

countries = ['Albania', 'Argentina', 'Australia', 'Austria', 'Bangladesh', 'Belgium', 'Bolivia', 'Brazil', 'Bulgaria', 'Canada', 'Chile', 'China', 'Colombia', 'Costa Rica', 'Croatia', 'Czech Republic', 'Denmark', 'Ecuador', 'Egypt', 'El Salvador', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece', 'Guatemala', 'Hong Kong', 'Hungary', 'India', 'Indonesia', 'Iran', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Kazakhstan', 'Kuwait', 'Luxembourg',
             'Malaysia', 'Malta', 'Mexico', 'Morocco', 'Namibia', 'Netherlands', 'New Zealand', 'Nigeria', 'Norway', 'Pakistan', 'Panama', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Serbia', 'Singapore', 'Slovakia', 'Slovenia', 'South Africa', 'South Korea', 'Spain', 'Suriname', 'Sweden', 'Switzerland', 'Taiwan', 'Thailand', 'Trinidad and Tobago', 'Turkey', 'United Kingdom', 'United States', 'Uruguay', 'Venezuela', 'Vietnam', 'Zambia', 'Zimbabwe']
opt = []
for c in countries:
    opt.append({'label': html.Div(
        [c], style={'color': 'orange', 'font-size': 20}), 'value': c})

dash.register_page(__name__)
layout = html.Div([

    html.Div([
        html.Div([
        ],
            className="one-third column",
        ),
        html.Div([
            html.Div([
                html.H3("Campaigns Sentiment Analysis", style={
                        "margin-bottom": "0px", 'color': 'white'}),
                html.H5("",
                        style={"margin-top": "0px", 'color': 'white'}),
            ])
        ], className="one-half column", id="title_senti"),

        html.Div([

        ], className="one-third column", id='title1_senti'),

    ], id="header2", className="row flex-display", style={"margin-bottom": "25px", "textAlign": "center"}),

    html.Div([
        dcc.Dropdown(options=[
            {'label': html.Div(['Appreciation campaign'], style={
                               'color': 'orange', 'font-size': 20}), 'value': 'appreciation'},
            {'label': html.Div(['Gift campaign'], style={
                               'color': 'orange', 'font-size': 20}), 'value': 'gift'},
            {'label': html.Div(['Donation campaign'], style={
                               'color': 'orange', 'font-size': 20}), 'value': 'donation'},
            {'label': html.Div(['Benefit campaign'], style={
                               'color': 'orange', 'font-size': 20}), 'value': 'benefit'},
            {'label': html.Div(['Support campaign'], style={
                               'color': 'orange', 'font-size': 20}), 'value': 'support'},
        ], value='campaign', placeholder="Select a campaign type", id='demo-dropdown', style={"color": "black"}),
        html.Div(id='dd-output-container')
    ]),

    html.Div([
        html.Div([
            html.H6(children='Tweets',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(f"{tweets}", style={
                'textAlign': 'center',
                'color': 'orange',
                'fontSize': 40}, id='tweet_count_senti')
        ], className="card_container three columns",
        ),

        html.Div([
            html.H6(children='Positive Tweets',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(f"35%",
                   style={
                       'textAlign': 'center',
                       'color': 'Chartreuse',
                       'fontSize': 40}, id='positive_tweet_count_senti'
                   ),
            html.P(f'',
                   style={
                       'textAlign': 'center',
                       'color': 'Chartreuse',
                       'fontSize': 18,
                       'margin-top': '-18px'}, id='positive_tweet_count_senti2'
                   )
        ], className="card_container three columns",
        ),

        html.Div([
            html.H6(children='Negative Tweets',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
            html.P("35%",
                   style={
                       'textAlign': 'center',
                       'color': 'red',
                       'fontSize': 40}, id='negative_tweet_count_senti'
                   ),
            html.P(f'',
                   style={
                       'textAlign': 'center',
                       'color': 'red',
                       'fontSize': 18,
                       'margin-top': '-18px'}, id='negative_tweet_count_senti2'
                   )
        ], className="card_container three columns",
        ),

        html.Div([
            html.H6(children='Neutral Tweets',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
            html.P("20%",
                   style={
                       'textAlign': 'center',
                       'color': '#98F5FF',
                       'fontSize': 40}, id='neutral_tweet_count_senti'
                   ),
            html.P(f'',
                   style={
                       'textAlign': 'center',
                       'color': '#98F5FF',
                       'fontSize': 18,
                       'margin-top': '-18px'}, id='neutral_tweet_count_senti2'
                   )
        ], className="card_container three columns")

    ], className="row flex-display"),


    html.Div([
        html.Div([
            html.H6(children='Average Sentiment Score',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(f"{tweets}", style={
                'textAlign': 'center',
                'color': 'gold',
                'fontSize': 40}, id='avg_senti_score')
        ], className="card_container four columns",
        ),

        html.Div([
            html.H6(children='Highest Sentiment Score',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(f"35%",
                   style={
                       'textAlign': 'center',
                       'color': '#00FA9A',
                       'fontSize': 40}, id='high_senti_score'
                   ),
            html.P(f'',
                   style={
                       'textAlign': 'center',
                       'color': '#00FA9A',
                       'fontSize': 18,
                       'margin-top': '-18px'}, id=''
                   )
        ], className="card_container four columns",
        ),

        html.Div([
            html.H6(children='Lowest Sentiment Score',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
            html.P("35%",
                   style={
                       'textAlign': 'center',
                       'color': '#C71585',
                       'fontSize': 40}, id='low_senti_score'
                   ),
            html.P(f'',
                   style={
                       'textAlign': 'center',
                       'color': '#C71585',
                       'fontSize': 18,
                       'margin-top': '-18px'}, id=''
                   )
        ], className="card_container four columns",
        )

    ], className="row flex-display"),

    html.Div([
        dash_table.DataTable(
            columns=[{"name": i, "id": i, }
                     for i in (sentidf_appreciation.columns)],
            editable=False,
            sort_action="native",
            sort_mode="multi",
            column_selectable="single",
            row_deletable=False,
            selected_columns=[],
            selected_rows=[],
            page_action="native",
            style_cell={'textAlign': 'left'},
            style_header={
                'backgroundColor': 'rgb(210, 210, 210)',
                'color': 'black',
                'font-size': '18px',
                'fontWeight': 'bold'
            },
            style_data={
                'color': 'black',
                'backgroundColor': 'white',
                'font-size': '16px',
            },
            id='sentiment_datatable'
        )
    ], className="row", style={"width": "100%", "textAlign": "center", "display": "none"}),

    html.Div([
        html.Div([
        ],
            className="one-third column",
        ),
        html.Div([
            html.Div([
                html.H3("Topic Analysis (BERTopic)", style={
                        "margin-bottom": "0px", 'color': 'white'}),
                html.H5("",
                        style={"margin-top": "0px", 'color': 'white'}),
            ])
        ], className="one-half column", id="title_topic"),

        html.Div([

        ], className="one-third column", id='title1_topic'),

    ], id="header3", className="row flex-display", style={"margin-bottom": "25px", "textAlign": "center"}),

    html.Div([
        dcc.Dropdown(options=opt, value='country',
                     placeholder="Select a country", id='country-dropdown', style={"color": "white"}),
        html.Div(id='country-output-container',
                 style={"paddingBottom": "1.5%"})
    ]),

    html.Div([
        dcc.Dropdown(options=[
            {'label': html.Div(['Appreciation campaign'], style={
                               'color': 'orange', 'font-size': 20}), 'value': 'appreciate'},
            {'label': html.Div(['Gift campaign'], style={
                               'color': 'orange', 'font-size': 20}), 'value': 'gifts'},
            {'label': html.Div(['Donation campaign'], style={
                               'color': 'orange', 'font-size': 20}), 'value': 'donation'},
            {'label': html.Div(['Benefit campaign'], style={
                               'color': 'orange', 'font-size': 20}), 'value': 'benefits'},
            {'label': html.Div(['Support campaign'], style={
                               'color': 'orange', 'font-size': 20}), 'value': 'support'},
        ], value='topic_campaign', placeholder="Select a campaign type", id='topiccamp-dropdown', style={"color": "white"}),
        html.Div(id='topic-camp-output-container',
                 style={"paddingBottom": "1.5%"})
    ]),

    html.Div([
        dcc.Dropdown(options=[
            {'label': html.Div(['Positive Sentiment'], style={
                               'color': 'orange', 'font-size': 20}), 'value': 'positive'},
            {'label': html.Div(['Negative Sentiment'], style={
                               'color': 'orange', 'font-size': 20}), 'value': 'negative'},
            {'label': html.Div(['Neutral'], style={
                               'color': 'orange', 'font-size': 20}), 'value': 'neutral'}
        ], value='topic_senti', placeholder="Choose a sentiment", id='topicsenti-dropdown', style={"color": "white"}),
        html.Div(id='topic-senti-output-container')
    ]),


    html.Div([
        html.Div([
            html.H6(children='Tweets',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(f"", style={
                'textAlign': 'center',
                'color': 'gold',
                'fontSize': 40}, id='tweet_count_topic')
        ], className="card_container six columns",
        ),

        html.Div([
            html.H6(children='No. Of Topics',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(f"35%",
                   style={
                       'textAlign': 'center',
                       'color': '#98F5FF',
                       'fontSize': 40}, id='topic_count'
                   )
        ], className="card_container six columns",
        )

    ], className="row flex-display"),

    html.Div([
        html.Div([
            html.H6(children='Topic Labels & Scores',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
            html.P(children='Topic -1 refers to all outliers and should typically be ignored, select a TopicLabel cell to view word scores',
                   style={
                       'textAlign': 'center',
                       'color': 'white',
                       'paddingBottom': '1em'}
                   ),
            dash_table.DataTable(
                editable=False,
                column_selectable="single",
                row_deletable=False,
                hidden_columns=['WordScore', 'Unnamed: 0', 'Sentiment'],
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
                id='topic_datatable'
            )
        ], className="card_container twelve columns",
        )
    ], className="row flex-display"),


    html.Div([
        html.Div([
            html.H6(children='Intertopic Distance Map',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
            html.Iframe(src="assets/ta_result/appreciate/albania/visualize_topics_appreciate_positive_bert.html",
                        style={
                            'textAlign': 'center',
                            "height": "400px", "width": "100%"
                        },
                        id='intertopic_map'
                        )
        ], className="card_container six columns",
        ),

        html.Div([
            html.H6(children='BERTopic Word Score',
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
                id='topic_datatable_wordscore'
            )
        ], className="card_container six columns",
        ),

    ], className="row flex-display"),

    dcc.Link(html.Button("REGRESSION PAGE", style={
        'textAlign': 'center',
        "width": "100%",
        "color":'black',
        "font-size": 16,
        'backgroundColor': '#98F5FF',
    }), href="/regression", refresh=True),

])


@dash.callback(
    Output('sentiment_datatable', 'data'),
    Input('demo-dropdown', 'value')
)
def update_output(campaign):
    if campaign == 'appreciation':
        return sentidf_appreciation.to_dict(orient='records')
    elif campaign == 'gift':
        return sentidf_gift.to_dict(orient='records')
    elif campaign == 'donation':
        return sentidf_donation.to_dict(orient='records')
    elif campaign == 'benefit':
        return sentidf_benefit.to_dict(orient='records')
    elif campaign == 'support':
        return sentidf_support.to_dict(orient='records')
    else:
        return sentidf_appreciation.to_dict(orient='records')


@dash.callback(
    Output('tweet_count_senti', 'children'),
    Output('positive_tweet_count_senti', 'children'),
    Output('negative_tweet_count_senti', 'children'),
    Output('neutral_tweet_count_senti', 'children'),
    Output('positive_tweet_count_senti2', 'children'),
    Output('negative_tweet_count_senti2', 'children'),
    Output('neutral_tweet_count_senti2', 'children'),
    Output('avg_senti_score', 'children'),
    Output('high_senti_score', 'children'),
    Output('low_senti_score', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output_senti_tweetscount(campaign):

    if campaign == 'appreciation':
        camp = sentidf_appreciation
    elif campaign == 'gift':
        camp = sentidf_gift
    elif campaign == 'donation':
        camp = sentidf_donation
    elif campaign == 'benefit':
        camp = sentidf_benefit
    elif campaign == 'support':
        camp = sentidf_support
    else:
        camp = sentidf_appreciation

    tweetscount = int(camp['Total No. of Tweet'].sum())
    positivetweetscount = "{:,}".format(camp['Positive'].sum())
    negativetweetscount = "{:,}".format(camp['Negative'].sum())
    neutralweetscount = "{:,}".format(camp['Neutral'].sum())

    total = 1805820
    positivetweetscount2 = "(" + str(
        round((camp['Positive'].sum() / tweetscount) * 100, 2)) + "%)"
    negativetweetscount2 = "(" + str(
        round((camp['Negative'].sum() / tweetscount) * 100, 2)) + "%)"
    neutralweetscount2 = "(" + str(
        round((camp['Neutral'].sum() / tweetscount) * 100, 2)) + "%)"

    tweetscount = "{:,}".format(tweetscount)

    avg_senti_score = round(camp['Avg Sentiment Score'].mean(), 2)
    high_senti_score = round(camp['Avg Sentiment Score'].max(), 2)
    low_senti_score = round(camp['Avg Sentiment Score'].min(), 2)

    return tweetscount, positivetweetscount, negativetweetscount, neutralweetscount, positivetweetscount2, negativetweetscount2, neutralweetscount2, avg_senti_score, high_senti_score, low_senti_score


@dash.callback(
    Output('topic_datatable', 'data'),
    Output('tweet_count_topic', 'children'),
    Output('topic_count', 'children'),
    Output('intertopic_map', 'src'),

    Input('country-dropdown', 'value'),
    Input('topiccamp-dropdown', 'value'),
    Input('topicsenti-dropdown', 'value')
)
def update_topic_data(country, topic_campaign, topic_senti):
    try:
        print(country + "," + topic_campaign + "," + topic_senti)
        fileSelected = pd.read_csv('dashboard/assets/ta_result/'+topic_campaign+'/' +
                                   country+'/topicinfo_'+topic_campaign+'_' + country+'_'+topic_senti+'.csv')
        tweetscount = int(fileSelected['Count'].sum())
        no_topics = len(fileSelected.index)
        intertopic_url = 'assets/ta_result/'+topic_campaign+'/' + country + \
            '/visualize_topics_'+topic_campaign+'_'+topic_senti+'_bert.html'
    except:
        fileSelected = pd.DataFrame()
        tweetscount = 0
        no_topics = 0
        intertopic_url = 'about:blank'

    return fileSelected.to_dict(orient='records'), tweetscount, no_topics, intertopic_url


@dash.callback(
    Output('topic_datatable_wordscore', 'data'),
    Input('topic_datatable', 'active_cell'),
    Input('topic_datatable', 'data'))
def update_graphs(active_cell, df_topic_datatable):
    if active_cell:
        ws = df_topic_datatable[active_cell['row']]['WordScore']
        ws = str(ws).replace('[', '').replace(']', '')
        ws = list(eval(ws))

        new_df = pd.DataFrame(ws, columns=['Keyphrase', 'Score'])
        return new_df.to_dict(orient='records')
    else:
        return pd.DataFrame().to_dict(orient='records')
