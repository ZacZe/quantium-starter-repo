import pandas
from dash import Dash, html, dcc
from plotly.express import line

data = "./output.csv"

app = Dash(__name__)

data = pandas.read_csv(data)
data = data.sort_values(by="Date")
line_chart = line(data, x="Date", y="Sales", title="Pink Morsel Sales")
visualization = dcc.Graph(
    id="visualization",
    figure=line_chart
)

header = html.H1(
    "Pink Morsel Visualizer",
    id="header"
)

app.layout = html.Div(
    [
        header,
        visualization
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
