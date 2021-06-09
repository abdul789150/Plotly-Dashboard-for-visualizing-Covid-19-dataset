# Libraries to be used
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from random import shuffle


df = pd.read_csv('world_map_data.csv')
world_df = pd.read_csv('owid-covid-data.csv')
world_df = world_df[world_df.location == "World"]


# -----------------------------------------------------------------------
# 
#           BOX PLOTS
# 
# -----------------------------------------------------------------------

def create_box_plot_figure(df, Y):
    figure = go.Figure()
    colors = ['#FF851B', '#FF4136', '#3D9970', 'indianred', 'lightseagreen']
    shuffle(colors)
    for variable, color in zip(Y, colors):
        figure.add_trace(go.Box(
            y=df[variable],
            name=variable,
            marker_color=color,
            boxmean=True # represent mean
        ))

    figure.update_layout(
        plot_bgcolor = "#222222",
        paper_bgcolor = "#222222",
        template="plotly_dark",
    )

    return figure


# -----------------------------------------------------------------------
# 
#           TIME SERIES PLOTS
# 
# -----------------------------------------------------------------------

def create_time_series_figure(df, X, Y):
    figure = px.line(df, x=X, y=Y, hover_data={"date": "|%B %d, %Y"})
    figure.update_xaxes(
        dtick="M1",
        tickformat="%b\n%Y")

    figure.update_layout(
        plot_bgcolor = "#222222",
        paper_bgcolor = "#222222",
        template="plotly_dark",
    )

    return figure



# -----------------------------------------------------------------------
# 
#           FIRST PAGE MAIN DASHBOARD
#                   LAYOUT 1
# 
# -----------------------------------------------------------------------


# Side panel
panel = html.Div([
    dbc.Card(body=True, children=[
        dbc.Col(html.H5("About this app", className="ml-n3")), 
        html.Br(),
        dbc.Row([
            html.P("Data Source: "),
            html.A("Our World in Data", href="https://ourworldindata.org/coronavirus-source-data", className="ml-2"),
        ], className="pl-3"),
        html.P("""This application provides the visualizations for Covid-19 dataset.
                The dataset for Covid-19 cases has been taken from Our World in Data website.
                This dataset has about 52k entries and it is daily updated by the team of Our 
                World in Data. This dataset is last updated on 26 OCT, 2020.
                """),
        html.P("""
            Here in this page you can see a Choropleth World Map, this map is generated according
            to the number of total Covid-19 cases in each country. For more visualizations click
            on a country in a map, after that you will be able to see more detailed visualization
            for each feature according to a selected country. 
            """),
    ])
])


total_cases_card = html.Div([
    dbc.Card(body=True, children=[
        html.H4("43,140,173", style={"font-weight":"600"}),
        html.P("World Wide Total Cases"),
    ], className="text-white bg-warning"),
])

total_deaths_card = html.Div([
    dbc.Card(body=True, children=[
        html.H4("1,155,235", style={"font-weight":"600"}),
        html.P("World Wide Total Deaths"),
    ], className="text-white bg-danger"),
])

new_cases_card = html.Div([
    dbc.Card(body=True, children=[
        html.H4("383,258", style={"font-weight":"600"}),
        html.P("New Cases on Oct 26, 2020"),
    ], className="text-white bg-light"),
])


fig = go.Figure(data=go.Choropleth(
    locations = df['Code'],
    z = df['Total Cases'],
    text = df['Country'],
    colorscale = 'Reds',
    autocolorscale=False,
    reversescale=False,
    marker_line_color='black',
    marker_line_width=0.5,
    colorbar_title = 'Covid Cases',
))


fig.update_layout(
    plot_bgcolor = "#060606",
    paper_bgcolor = "#060606",
    margin={"r":0,"t":0,"l":0,"b":0},
    template="plotly_dark",
    geo=dict(
        showframe=True,
        showcoastlines=False,
        projection_type='equirectangular'
    )
)

map_card = html.Div([
    dcc.Graph(
        id="world_map",
        config={"displayModeBar": False},
        figure = fig,
        className="text-white bg-light mt-3 mb-3"
    )
])


########################################################3
time_series_new_cases_deaths = html.Div([
    dbc.Card(body=True, children=[
        html.H6("Time Series graph for Daily Cases and Deaths", style={"font-weight":"600"}),
        dcc.Graph(
            figure = create_time_series_figure(df=world_df, X="date", Y=["new_cases", "new_deaths"]),
        )
    ], className="text-white bg-light"),
])

# ########################################################3
time_series_new_deaths = html.Div([
    dbc.Card(body=True, children=[
        html.H6("Time Series graph for Daily Deaths", style={"font-weight":"600"}),
        dcc.Graph(
            figure = create_time_series_figure(df=world_df, X="date", Y=["new_deaths"])
        )
    ], className="text-white bg-light"),
])
##########################################################################33
total_confirmed_cases = html.Div([
    dbc.Card(body=True, children=[
        html.H6("Time Series graph for total Confirmed Cases", style={"font-weight":"600"}),
        dcc.Graph(
            figure = create_time_series_figure(df=world_df, X="date", Y=["total_cases"])
        )
    ], className="text-white bg-light"),
])

######################################################################### 
total_deaths = html.Div([
    dbc.Card(body=True, children=[
        html.H6("Time Series graph for Total Deaths", style={"font-weight":"600"}),
        dcc.Graph(
            figure = create_time_series_figure(df=world_df, X="date", Y=["total_deaths"])
        )
    ], className="text-white bg-light"),
])


row_1 = html.Div([
    dbc.Row([
        dbc.Col(html.Div([time_series_new_cases_deaths]), width=6),
        dbc.Col(html.Div(time_series_new_deaths), width=6),
    ], className="")
])

row_2 = html.Div([
    dbc.Row([
        dbc.Col(html.Div([total_confirmed_cases]), width=6),
        dbc.Col(html.Div([total_deaths]), width=6),
    ], className="mt-4 mb-4")
])

input_form = html.Div([
    dbc.Row([
        dbc.Col(html.Div([total_cases_card]), width=4),
        dbc.Col(html.Div([total_deaths_card]), width=4),
        dbc.Col(html.Div([new_cases_card]), width=4),
    ]),
    dbc.Row([
        dbc.Col(html.Div([map_card]), width=12),
    ]),
])

# Adding everything in a div 
row = html.Div(
    [
        html.Div([
            html.Br(),
            dbc.Col(html.H3("Covid-19 Dataset Visualization"), style={'text-align': 'center'}), 
            html.Br(),html.Br()
        ]),
        dbc.Row(
            [
                dbc.Col(html.Div([panel]), width=3),
                dbc.Col(html.Div([input_form]), width=8),
            ]
        ),
        html.Div([
            html.Br(),
            dbc.Col(html.H4("Time Series Plots"), style={'text-align': 'left'}), 
            html.Br(),html.Br()
        ]),
        row_1,
        row_2,
    ]
)


layout1 = dbc.Container(fluid=True, children=
    [
        row,
    ],
)

# -----------------------------------------------------------------------
# 
#           SECOND PAGE COUNTRIES VISUALIZATION
#                   LAYOUT 2
# 
# -----------------------------------------------------------------------

# maps for second page
def create_map(df, variable, title):
    fig = go.Figure(data=go.Choropleth(
        locations = df['iso_code'],
        z = df[variable],
        text = df['location'],
        colorscale = 'Reds',
        autocolorscale=False,
        reversescale=False,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_title = title, 
    ))

    fig.update_layout(
        plot_bgcolor = "#222222",
        paper_bgcolor = "#222222",
        margin={"r":0,"t":0,"l":0,"b":0},
        template="plotly_dark",
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular',
        )
    )

    return fig
# 




def get_layout_2(country_name):
    display_name = country_name.split(',')[0]
    country_df = pd.read_csv("countries-data/"+country_name+".csv")
    continent_data = pd.read_csv('continent-data/'+country_df.continent[0]+'.csv')

    ########################################################3
    time_series_new_cases_deaths = html.Div([
        dbc.Card(body=True, children=[
            html.H6("Time Series graph for Daily Cases and Deaths", style={"font-weight":"600"}),
            dcc.Graph(
                figure = create_time_series_figure(df=country_df, X="date", Y=["new_cases", "new_deaths"]),
            )
        ], className="text-white bg-light"),
    ])

    # ########################################################3
    time_series_new_cases_new_tests = html.Div([
        dbc.Card(body=True, children=[
            html.H6("Time Series graph for Daily Cases and Tests", style={"font-weight":"600"}),
            dcc.Graph(
                figure = create_time_series_figure(df=country_df, X="date", Y=["new_cases", "new_tests"])
            )
        ], className="text-white bg-light"),
    ])

    ##########################################################################33
    total_confirmed_cases = html.Div([
        dbc.Card(body=True, children=[
            html.H6("Time Series graph for Total Confirmed Cases", style={"font-weight":"600"}),
            dcc.Graph(
                figure = create_time_series_figure(df=country_df, X="date", Y=["total_cases"])
            )
        ], className="text-white bg-light"),
    ])

    ######################################################################### 
    total_deaths = html.Div([
        dbc.Card(body=True, children=[
            html.H6("Time Series graph for Total Deaths", style={"font-weight":"600"}),
            dcc.Graph(
                figure = create_time_series_figure(df=country_df, X="date", Y=["total_deaths"])
            )
        ], className="text-white bg-light"),
    ])
    #######################################################################
    total_tests_taken = html.Div([
        dbc.Card(body=True, children=[
            html.H6("Time Series graph for Total Tests Taken", style={"font-weight":"600"}),
            dcc.Graph(
                figure = create_time_series_figure(df=country_df, X="date", Y=["total_tests"])
            )
        ], className="text-white bg-light"),
    ])

    #####################################################################
    daily_tests_taken = html.Div([
        dbc.Card(body=True, children=[
            html.H6("Time Series graph for Daily Tests Taken", style={"font-weight":"600"}),
            dcc.Graph(
                figure = create_time_series_figure(df=country_df, X="date", Y=["new_tests"])
            )
        ], className="text-white bg-light"),
    ])

    ################################################################# 
    time_series_stringency_index_new_cases = html.Div([
        dbc.Card(body=True, children=[
            html.H6("Time Series graph for Stringency Index and Daily Cases", style={"font-weight":"600"}),
            dcc.Graph(
                figure = create_time_series_figure(df=country_df, X="date", Y=["new_cases", "stringency_index"])
            )
        ], className="text-white bg-light"),
    ])
    ################################################################## 
    time_series_stringency_index = html.Div([
        dbc.Card(body=True, children=[
            html.H6("Time Series graph for Daily Stringency Index", style={"font-weight":"600"}),
            dcc.Graph(
                figure = create_time_series_figure(df=country_df, X="date", Y=["stringency_index"])
            )
        ], className="text-white bg-light"),
    ])

    ####################################################################
    daily_confirmed_cases = html.Div([
        dbc.Card(body=True, children=[
            html.H6("Time Series graph for Daily Confirmed Cases", style={"font-weight":"600"}),
            dcc.Graph(
                figure = create_time_series_figure(df=country_df, X="date", Y=["new_cases"])
            )
        ], className="text-white bg-light"),
    ])

    ###################################################################
    daily_deaths = html.Div([
        dbc.Card(body=True, children=[
            html.H6("Time Series graph for Daily Deaths", style={"font-weight":"600"}),
            dcc.Graph(
                figure = create_time_series_figure(df=country_df, X="date", Y=["new_deaths"])
            )
        ], className="text-white bg-light"),
    ])

    box_plot_cases_deaths_tests = html.Div([
        dbc.Card(body=True, children=[
            html.H6("Box Plot Chart for Daily Cases, Deaths and Tests", style={"font-weight":"600"}),
            dcc.Graph(
                figure = create_box_plot_figure(df=country_df, Y=["new_cases", "new_deaths", "new_tests"])
            )
        ], className="text-white bg-light"),
    ])
    # 
    box_plot_population = html.Div([
        dbc.Card(body=True, children=[
            html.H6("Box Plot Chart for Population", style={"font-weight":"600"}),
            dcc.Graph(
                figure = create_box_plot_figure(df=country_df, Y=["population"])
            )
        ], className="text-white bg-light"),
    ])
    box_plot_stringency_index = html.Div([
        dbc.Card(body=True, children=[
            html.H6("Box Plot Chart for Stringency Index", style={"font-weight":"600"}),
            dcc.Graph(
                figure = create_box_plot_figure(df=country_df, Y=["stringency_index"])
            )
        ], className="text-white bg-light"),
    ])
    box_plot_ages = html.Div([
        dbc.Card(body=True, children=[
            html.H6("Box Plot Chart", style={"font-weight":"600"}),
            dcc.Graph(
                figure = create_box_plot_figure(df=country_df, Y=["median_age", "aged_65_older", "aged_70_older"])
            )
        ], className="text-white bg-light"),
    ])
    box_plot_gdp_density = html.Div([
        dbc.Card(body=True, children=[
            html.H6("Box Plot Chart for Population Density and GDP per capita", style={"font-weight":"600"}),
            dcc.Graph(
                figure = create_box_plot_figure(df=country_df, Y=["population_density", "gdp_per_capita"])
            )
        ], className="text-white bg-light"),
    ])
    box_plot_hospital_handwashing = html.Div([
        dbc.Card(body=True, children=[
            html.H6("Box Plot Chart for Life Expectancy", style={"font-weight":"600"}),
            dcc.Graph(
                figure = create_box_plot_figure(df=country_df, Y=["life_expectancy"])
            )
        ], className="text-white bg-light"),
    ])

    continet_map_deaths = html.Div([
        dbc.Card(body=True, children=[
            html.H6("Deaths in the Continent", style={"font-weight":"600"}),
            dcc.Graph(
                figure = create_map(df=continent_data, variable="total_deaths", title="Deaths")
            )
        ], className="text-white bg-light"),
    ])
    # 
    continet_map_cases = html.Div([
        dbc.Card(body=True, children=[
            html.H6("Cases in the Continent", style={"font-weight":"600"}),
            dcc.Graph(
                figure = create_map(df=continent_data , variable="total_cases", title="Cases")
            )
        ], className="text-white bg-light"),
    ])


    row_1 = html.Div([
        dbc.Row([
            dbc.Col(html.Div([time_series_new_cases_deaths]), width=6),
            dbc.Col(html.Div(time_series_new_cases_new_tests), width=6),
        ], className="")
    ])

    row_2 = html.Div([
        dbc.Row([
            dbc.Col(html.Div([total_confirmed_cases]), width=6),
            dbc.Col(html.Div([daily_confirmed_cases]), width=6),
        ], className="mt-4")
    ])

    row_3 = html.Div([
        dbc.Row([
            dbc.Col(html.Div([total_deaths]), width=6),
            dbc.Col(html.Div([daily_deaths]), width=6),
        ], className="mt-4")
    ])
    row_4 = html.Div([
        dbc.Row([
            dbc.Col(html.Div([total_tests_taken]), width=6),
            dbc.Col(html.Div([daily_tests_taken]), width=6),
        ], className="mt-4")
    ])

    row_5 = html.Div([
        dbc.Row([
            dbc.Col(html.Div([time_series_stringency_index]), width=6),
            dbc.Col(html.Div([time_series_stringency_index_new_cases]), width=6),
        ], className="mt-4")
    ])

    row_6 = html.Div([
        dbc.Row([
            dbc.Col(html.Div([continet_map_cases]), width=6),
            dbc.Col(html.Div([continet_map_deaths]), width=6),
        ], className="")
    ])

    # Box plots
    row_7 = html.Div([
        dbc.Row([
            dbc.Col(html.Div([box_plot_cases_deaths_tests]), width=6),
            dbc.Col(html.Div([box_plot_ages]), width=6),
        ], className="")
    ])
    row_8 = html.Div([
        dbc.Row([
            dbc.Col(html.Div([box_plot_population]), width=6),
            dbc.Col(html.Div([box_plot_gdp_density]), width=6),
        ], className="mt-4")
    ])
    row_9 = html.Div([
        dbc.Row([
            dbc.Col(html.Div([box_plot_stringency_index]), width=6),
            dbc.Col(html.Div([box_plot_hospital_handwashing]), width=6),
        ], className="mt-4 mb-4")
    ])

    layout2 = dbc.Container(fluid=True, children=
        [
            html.Div([
                html.Br(),
                dbc.Col(html.H3("Data Visualization For "+display_name), style={'text-align': 'center'}), 
                html.Br(),html.Br()
            ]),
            html.Div([
                html.Br(),
                dbc.Col(html.H4("Time Series Plots for different features"), style={'text-align': 'left'}), 
                html.Br(),html.Br()
            ]),
            row_1,
            row_2,
            row_3,
            row_4,
            row_5,
            html.Div([
                html.Br(),
                dbc.Col(html.H4("Choropleth Map for Continent"), style={'text-align': 'left'}), 
                html.Br(),html.Br()
            ]),
            row_6,
            html.Div([
                html.Br(),
                dbc.Col(html.H4("Box Plots for detecting outliers"), style={'text-align': 'left'}), 
                html.Br(),html.Br()
            ]),
            row_7,
            row_8,
            row_9
        ],
    )

    return layout2