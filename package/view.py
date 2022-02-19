from dash import dcc, html, Input, Output, State
import plotly.graph_objects as go

from my_dash.maindash import app
from package.args import arguments
from weather_api.weatherApiQuery import weather_api_query

def make_layout():
    return html.Div(children=[
        html.Nav(children=[
            html.Div(children=[
                html.Div(children=[
                    html.Img(src="https://i.imgur.com/X5Ge0PN.png"),    
                ], className="navbar-item"),
            ], className="navbar-brand"),

            html.Div(children=[
                html.Div(children=[
                    html.Div(children=[
                        html.Span(children=[
                            dcc.Input(id="input_city", placeholder="City", value="New York", className="input"),
                        ], className="control"),
                        html.Span(children=[
                            html.Button("Search", id="submit_city", n_clicks=0, className="button is-link"),
                        ], className="control"),
                    ], className="field has-addons"),
                ], className="navbar-item"),
            ], className="navbar-start"),

            html.Div(children=[
                html.Div(children=[
                        html.A("API Used", href="https://openweathermap.org/", target="_blank", className="button is-success"),
                ], className="navbar-item"),
            ], className="navbar-end"),
        ], className="navbar is-info"),
        
        html.Div(children=[
            html.Div(children=[
                dcc.Dropdown(["today", "yesterday", "before yesterday", "3 days ago"], "today", clearable=False, id="input_dropdown_date"),
                html.Br(),
                # temperature part
                html.Div(children=[
                    html.H2(id="output_h2_city", className="title is-5 has-text-centered"), 
                    dcc.Graph(id="output_history_graph_temp"),
                
                    html.Table(children=[
                        html.Thead(children=[
                            html.Th(children=["Mean Temperature"]),
                            html.Th(children=["🔥 Max Temperature "]),
                            html.Th(children=["🧊 Min Temperature "]),
                        ]),
                        html.Tbody(children=[
                            html.Td(id="output_td_mean_temp"),
                            html.Td(id="output_td_max_temp"),
                            html.Td(id="output_td_min_temp"),
                        ]),
                        html.Thead(children=[
                            html.Th(children=["Felt"]),
                            html.Th(children=["Felt"]),
                            html.Th(children=["Felt"]),
                        ]),
                        html.Tbody(children=[
                            html.Td(id="output_td_mean_temp_felt"),
                            html.Td(id="output_td_max_temp_felt"),
                            html.Td(id="output_td_min_temp_felt"),
                        ])
                    ], className="table"),
                ], className="box"),
            ], className="container"),
        ], className="section"),

        html.Section(children=[
            html.Div(children=[
                html.Div(children=[

                    # humidity part
                    html.Div(children=[
                        html.Div(children=[
                            dcc.Graph(id="output_history_graph_humidity"),
                            html.Table(children=[
                                html.Thead(children=[
                                    html.Th(children=["Mean Humidity"]),
                                    html.Th(children=["Max Humidity"]),
                                    html.Th(children=["Min Humidity"])
                                ]),
                                html.Tbody(children=[
                                    html.Td(id="output_td_mean_humidity"),
                                    html.Td(id="output_td_max_humidity"),
                                    html.Td(id="output_td_min_humidity")
                                ]),
                            ], className="table"),
                        ], className="box"),
                    ], className="column"),

                    # pressure part
                    html.Div(children=[
                        html.Div(children=[
                            dcc.Graph(id="output_history_graph_pressure"),
                            html.Table(children=[
                                html.Thead(children=[
                                    html.Th(children=["Mean Pressure"]),
                                    html.Th(children=["Max Pressure"]),
                                    html.Th(children=["Min Pressure"])
                                ]),
                                html.Tbody(children=[
                                    html.Td(id="output_td_mean_pressure"),
                                    html.Td(id="output_td_max_pressure"),
                                    html.Td(id="output_td_min_pressure")
                                ]),
                            ], className="table"),
                        ], className="box"),
                    ], className="column"),
                ], className="columns"),
            ], className="container"),
        ], className="section has-background-light"),

        # wind speed part
        html.Section(children=[
            html.Div(children=[
                html.Div(children=[
                    dcc.Graph(id="output_history_graph_win_speed"),
                    html.Table(children=[
                        html.Thead(children=[
                            html.Th(children=["Mean Wind Speed"]),
                            html.Th(children=["Max Wind Speed"]),
                            html.Th(children=["Min Wind Speed"]),
                        ]),
                        html.Tbody(children=[
                            html.Td(id="output_td_mean_wind_speed"),
                            html.Td(id="output_td_max_wind_speed"),
                            html.Td(id="output_td_min_wind_speed"),
                        ]),
                    ], className="table"),
                ], className="box")
            ], className="container")
        ], className="section"),

        html.Footer(children=[
            html.Div(children=[
                html.P(children=["Author : Fayred"], className="title is-5"),
                html.A("My Github", href="https://github.com/Fayred", className="subtitle is-6 button is-text"),
            ])
        ], className="footer has-text-centered"),
    ], className="content")

@app.callback(
    [
        # h2 city title
        Output("output_h2_city", "children"),

        # temperature part
        Output("output_history_graph_temp", "figure"),
        Output("output_td_mean_temp" , "children"), Output("output_td_max_temp", "children"), Output("output_td_min_temp", "children"),
        Output("output_td_mean_temp_felt", "children"), Output("output_td_max_temp_felt", "children"), Output("output_td_min_temp_felt", "children"),

        # humidity part
        Output("output_history_graph_humidity", "figure"),
        Output("output_td_mean_humidity", "children"),
        Output("output_td_max_humidity", "children"),
        Output("output_td_min_humidity", "children"),

        # pressure part
        Output("output_history_graph_pressure", "figure"),
        Output("output_td_mean_pressure", "children"),
        Output("output_td_max_pressure", "children"),
        Output("output_td_min_pressure", "children"),

        # wind speed part
        Output("output_history_graph_win_speed", "figure"),
        Output("output_td_mean_wind_speed", "children"),
        Output("output_td_max_wind_speed", "children"),
        Output("output_td_min_wind_speed", "children"),
    ],
    [
        Input("input_dropdown_date", "value"),

        Input("submit_city", "n_clicks"),
        State("input_city", "value"),
    ]
)
def update_data(date, clicks, city):
    # h2 city title
    content_h2_city = f"Weather of '{city}' {date} :"
    # query to get informations about weather
    weather_data_structure = weather_api_query(city, date, debug=arguments.debug)

    # temperature part
    temp_data = []
    for name in weather_data_structure.columns[5:7]:
        temp_data.append(go.Scatter(
            x=weather_data_structure["Time"],
            y=weather_data_structure[name],
            mode="lines+markers",
            name="(°C) "+name
        ))
    temp_stat = {"data": temp_data, "layout": {"title": "🌡️ Temperatures"}}

    content_td_mean_temp = f"{round(weather_data_structure['Temperature'].mean(), 2)}°C"
    content_td_max_temp = f"{weather_data_structure['Temperature'].max()}°C"
    content_td_min_temp = f"{weather_data_structure['Temperature'].min()}°C"

    content_td_mean_temp_felt = f"{round(weather_data_structure['Temperature Felt'].mean(), 2)}°C"
    content_td_max_temp_felt = f"{weather_data_structure['Temperature Felt'].max()}°C"
    content_td_min_temp_felt = f"{weather_data_structure['Temperature Felt'].min()}°C"

    # humidity part
    humidity_data = [go.Scatter(
        x=weather_data_structure["Time"],
        y=weather_data_structure["Humidity"],
        mode="lines+markers",
        line_color="#6ac582"
    )]
    humidity_stat = {"data": humidity_data, "layout": {"title": "🌿 Humidity"}}

    content_td_mean_humidity = f"{round(weather_data_structure['Humidity'].mean(), 2)}%"
    content_td_max_humidity = f"{weather_data_structure['Humidity'].max()}%"
    content_td_min_humidity = f"{weather_data_structure['Humidity'].min()}%"

    # pressure part
    pressure_data = [go.Scatter(
        x=weather_data_structure["Time"],
        y=weather_data_structure["Pressure"],
        mode="lines+markers",
        line_color="#d62d20"
    )]
    pressure_stat = {"data": pressure_data, "layout": {"title": "📈 Pressure"}}

    content_td_mean_pressure = f"{round(weather_data_structure['Pressure'].mean(), 2)}hPa"
    content_td_max_pressure = f"{weather_data_structure['Pressure'].max()}hPa"
    content_td_min_pressure = f"{weather_data_structure['Pressure'].min()}hPa"

    # wind speed part
    wind_speed_data = [go.Scatter(
        x=weather_data_structure["Time"],
        y=weather_data_structure["Wind Speed"],
        mode="lines+markers",
        line_color="#6f7d7b"
    )]
    wind_speed_stat = {"data": wind_speed_data, "layout": {"title": "💨 Wind Speed"}}

    content_td_mean_wind_speed = f"{round(weather_data_structure['Wind Speed'].mean(), 2)}km/h"
    content_td_max_wind_speed = f"{weather_data_structure['Wind Speed'].max()}km/h"
    content_td_min_wind_speed = f"{weather_data_structure['Wind Speed'].min()}km/h"

    return (
        # return h2 main title
        content_h2_city,

        # return temperature part
        temp_stat,

        content_td_mean_temp,
        content_td_max_temp,
        content_td_min_temp,

        content_td_mean_temp_felt,
        content_td_max_temp_felt,
        content_td_min_temp_felt,

        # return humidity part
        humidity_stat,
        content_td_mean_humidity,
        content_td_max_humidity,
        content_td_min_humidity,

        # return pressure part
        pressure_stat,
        content_td_mean_pressure,
        content_td_max_pressure,
        content_td_min_pressure,

        # return wind speed part
        wind_speed_stat,
        content_td_mean_wind_speed,
        content_td_max_wind_speed,
        content_td_min_wind_speed
    )