import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps.layouts import layout1, get_layout_2

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=[
        layout1
    ])
])

@app.callback(Output('page-content', 'children'),
    [Input('url', 'pathname'),
    Input('world_map', 'clickData')])
def display_page(url, world_map):
    
    if world_map is not None:  
        try:
            print(world_map['points'][0]["text"])
            name = world_map['points'][0]["text"]
            return get_layout_2(country_name=name)
        except Exception:
            pass
    else:
        return layout1
    
    return '404 Error'

if __name__ == '__main__':
    app.run_server(debug=True)