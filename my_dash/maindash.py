import dash

app = dash.Dash(
    __name__,
    meta_tags=[{"name":"viewport", "content":"width=device-width, initial-scale=1"}],
    external_stylesheets=["https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css"],
    title="WeatherBoard"
)