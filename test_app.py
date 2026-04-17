from mainapp import app

def test_header_exists(dash_duo):
    dash_duo.start_server(app, port=8050)
    dash_duo.wait_for_element("#header", timeout=10)


def test_visualization_exists(dash_duo):
    dash_duo.start_server(app, port=8051)
    dash_duo.wait_for_element("#sales_graph", timeout=10)


def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app, port=8052)
    dash_duo.wait_for_element("#region_filter", timeout=10)
