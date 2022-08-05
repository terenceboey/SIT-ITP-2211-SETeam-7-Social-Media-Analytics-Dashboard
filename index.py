import dash
import os
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from dash import dash_table, dcc, html, Input, Output
import dash_bootstrap_components as dbc

assets_path = os.getcwd() + 'assets'

app = dash.Dash(__name__, use_pages=True, meta_tags=[
                {"name": "viewport", "content": "width=device-width"}])
camp = pd.read_excel('dashboard/assets/overall_countries_health_worker_statistics_for_regression_analysis.xlsx')

tweetscount = int(camp['Total No. of Tweet'].sum())
positivetweetscount = "{:,}".format(camp['Positive Sentiment'].sum())
negativetweetscount = "{:,}".format(camp['Negative Sentiment'].sum())
neutralweetscount = "{:,}".format(camp['Neutral Sentiment'].sum())
avg_senti_score = camp['Avg Sentiment Score'].sum()
avg_senti_score = round((float(avg_senti_score) / 79.0),2)

positivetweetscount2 = "(" + str(
    round((camp['Positive Sentiment'].sum() / tweetscount) * 100, 2)) + "%)"
negativetweetscount2 = "(" + str(
    round((camp['Negative Sentiment'].sum() / tweetscount) * 100, 2)) + "%)"
neutralweetscount2 = "(" + str(
    round((camp['Neutral Sentiment'].sum() / tweetscount) * 100, 2)) + "%)"

tweetscount = "{:,}".format(tweetscount)

app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(id='twitter-img', src='assets/twitter.png',
                     style={'width': '100px', 'textAlign': 'center'}),

        ],
            className="one-third column",
        ),
        html.Div([
            html.Div([
                html.H3("Social Media Data Analytics towards Healthcare Workers", style={
                        "margin-bottom": "0px", 'color': 'white', 'font-weight': 'bold'}),
                html.H5("SIT-ITP-2211-SETeam-7",
                        style={"margin-top": "0px", 'color': 'white'}),
            ])
        ], className="twelve column", id="title"),

        html.Div([
            html.Img(id='py-img',src='assets/py.png', style={'width': '100px','textAlign': 'center'}),

        ], className="one-third column", id='title1'),

    ], id="header", className="row flex-display", style={"margin-bottom": "25px"}),

    html.Div([
        html.Div([
            html.H6(children='Total Tweets',
                    style={
                        'textAlign': 'center',
                        'color': 'white'},
                    ),

            html.P(f"6,438,158", style={
                'textAlign': 'center',
                'color': 'orange',
                'fontSize': 40})
        ], className="card_container three columns",
        ),

        html.Div([
            html.H6(children='Countries',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(f"79",
                   style={
                       'textAlign': 'center',
                       'color': 'yellow',
                       'fontSize': 40}
                   )
        ], className="card_container three columns",
        ),

        html.Div([
            html.H6(children='Overall Avg Sentiment Score',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ), html.P(f"{avg_senti_score}",
                              style={
                                  'textAlign': 'center',
                                  'color': 'orange',
                                  'fontSize': 40}
                              )
        ], className="card_container three columns",
        ),

        html.Div([
            html.H6(children='Period',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P("Dec 2019 - Jun 2022",
                   style={
                       'textAlign': 'center',
                       'color': 'gold',
                       'fontSize': 30}
                   )
        ], className="card_container three columns")

    ], className="row flex-display"),


    html.Div([

        html.Div([
            html.H6(children='Positive Tweets',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
            html.P(f"{positivetweetscount}",
                   style={
                       'textAlign': 'center',
                       'color': 'Chartreuse',
                       'fontSize': 40}, id='positive_tweet_count'
                   ),
            html.P(f'{positivetweetscount2}',
                   style={
                       'textAlign': 'center',
                       'color': 'Chartreuse',
                       'fontSize': 18,
                       'margin-top': '-18px'}, id='positive_tweet_count2'
                   )
        ], className="card_container four columns",
        ),

        html.Div([
            html.H6(children='Negative Tweets',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
            html.P(f"{negativetweetscount}",
                   style={
                       'textAlign': 'center',
                       'color': 'red',
                       'fontSize': 40}, id='negative_tweet_count'
                   ),
            html.P(f'{negativetweetscount2}',
                   style={
                       'textAlign': 'center',
                       'color': 'red',
                       'fontSize': 18,
                       'margin-top': '-18px'}, id='negative_tweet_count2'
                   )
        ], className="card_container four columns",
        ),

        html.Div([
            html.H6(children='Neutral Tweets',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
            html.P(f"{neutralweetscount}",
                   style={
                       'textAlign': 'center',
                       'color': '#98F5FF',
                       'fontSize': 40}, id='neutral_tweet_count'
                   ),
            html.P(f'{neutralweetscount2}',
                   style={
                       'textAlign': 'center',
                       'color': '#98F5FF',
                       'fontSize': 18,
                       'margin-top': '-18px'}, id='neutral_tweet_count2'
                   )
        ], className="card_container four columns")

    ], className="row flex-display"),

    dash.page_container

], id="mainContainer",
    style={"display": "flex", "flex-direction": "column"})



# @dash.callback(
#     Output('tweet_count', 'children'),
#     Output('positive_tweet_count', 'children'),
#     Output('negative_tweet_count', 'children'),
#     Output('neutral_tweet_count', 'children'),
#     Output('positive_tweet_count2', 'children'),
#     Output('negative_tweet_count2', 'children'),
#     Output('neutral_tweet_count2', 'children'),
#     # Output('avg_senti_score', 'children'),
#     # Output('high_senti_score', 'children'),
#     # Output('low_senti_score', 'children'),
#     Input('demo-dropdown', 'value')
# )
def update_output_tweetscount():
    camp = pd.read_excel('dashboard/assets/overall_countries_health_worker_statistics_for_regression_analysis.xlsx')

    tweetscount = int(camp['Total No. of Tweet'].sum())
    positivetweetscount = "{:,}".format(camp['Positive Sentiment'].sum())
    negativetweetscount = "{:,}".format(camp['Negative Sentiment'].sum())
    neutralweetscount = "{:,}".format(camp['Neutral Sentiment'].sum())

    positivetweetscount2 = "(" + str(
        round((camp['Positive Sentiment'].sum() / tweetscount) * 100, 2)) + "%)"
    negativetweetscount2 = "(" + str(
        round((camp['Negative Sentiment'].sum() / tweetscount) * 100, 2)) + "%)"
    neutralweetscount2 = "(" + str(
        round((camp['Neutral Sentiment'].sum() / tweetscount) * 100, 2)) + "%)"

    tweetscount = "{:,}".format(tweetscount)

    return tweetscount, positivetweetscount, negativetweetscount, neutralweetscount, positivetweetscount2, negativetweetscount2, neutralweetscount2


if __name__ == '__main__':
    app.run_server(debug=True)
