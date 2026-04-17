import pandas
from dash import Dash, html, dcc, Input, Output
from plotly.express import line


data = pandas.read_csv("output.csv")
data["Date"] = pandas.to_datetime(data["Date"])
data["Sales"] = pandas.to_numeric(data["Sales"])

app = Dash(__name__)


def make_chart(region_name):
    filtered_data = data

    if region_name != "all":
        filtered_data = data[data["Region"] == region_name]

    chart_data = (
        filtered_data.groupby("Date", as_index=False)["Sales"]
        .sum()
        .sort_values(by="Date")
    )

    figure = line(
        chart_data,
        x="Date",
        y="Sales",
        title="Pink Morsel Sales Over Time",
    )

    figure.update_traces(line_color="#d94f70", line_width=3)
    figure.update_layout(
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        font={"family": "Arial", "color": "#333333"},
        title={"x": 0.5},
        xaxis_title="Date",
        yaxis_title="Sales",
        margin={"l": 40, "r": 20, "t": 70, "b": 40},
    )
    figure.add_vline(x="2021-01-15", line_dash="dash", line_color="#7a3e48")

    return figure


header = html.H1(
    "Soul Foods Pink Morsel Sales Visualiser",
    id="header",
    style={
        "textAlign": "center",
        "marginBottom": "25px",
        "color": "#333333",
    },
)
region_filter = dcc.RadioItems(
    id="region_filter",
    options=[
        {"label": "All", "value": "all"},
        {"label": "North", "value": "north"},
        {"label": "East", "value": "east"},
        {"label": "South", "value": "south"},
        {"label": "West", "value": "west"},
    ],
    value="all",
    inline=True,
    style={"marginBottom": "20px", "textAlign": "center"},
    labelStyle={"marginRight": "15px"},
)
sales_graph = dcc.Graph(
    id="sales_graph",
    figure=make_chart("all"),
)


app.layout = html.Div(
    [
        header,
        region_filter,
        sales_graph
    ],
    style={
        "maxWidth": "1000px",
        "margin": "0 auto",
        "padding": "30px 20px",
        "fontFamily": "Arial, sans-serif",
        "backgroundColor": "#f7f7f7",
        "minHeight": "100vh",
    },
)


@app.callback(
    Output("sales_graph", "figure"),
    Input("region_filter", "value"),
)
def update_chart(selected_region):
    return make_chart(selected_region)


if __name__ == "__main__":
    app.run(debug=True)
