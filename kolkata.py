import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import geopandas as gpd
import plotly.express as px

# Load the Shapefile
shapefile_path = r"C:\Users\91956\Desktop\SEMESTER 3\kolk_data\kolk_data\kolk_data.shp"
gdf = gpd.read_file(shapefile_path)

# Set up the Dash app
app = dash.Dash(__name__)

# Define initial variables for visualization
initial_variable1 = 'Avg_Temp'
variable2 = 'Slum_pop'

# Create an interactive scatter plot on the map
scatter_fig = px.scatter_mapbox(
    gdf,
    lat=gdf.geometry.centroid.y,
    lon=gdf.geometry.centroid.x,
    color=initial_variable1,
    size=variable2,
    hover_name=gdf['Borough1'],
    hover_data={initial_variable1: True, 'FVI': True, variable2: True},
    mapbox_style="carto-positron",
    zoom=10,
)

# Define the layout of the Dash app
app.layout = html.Div([
    html.H1("Kolkata Metropolitan Data", style={'textAlign': 'center'}),
    dcc.Graph(figure=scatter_fig, id='scatter-plot'),
    dcc.Dropdown(
        id='variable-dropdown',
        options=[
            {'label': 'Avg_Temp', 'value': 'Avg_Temp'},
            {'label': 'Urban_Wate', 'value': 'Urban_Wate'},
            {'label': 'Water_Avai', 'value': 'Water_Avai'},
            {'label': 'FVI', 'value': 'FVI'},
        ],
        value=initial_variable1,
        style={'width': '50%'}
    ),
])

# Define callback to update the scatter plot based on variable selection
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('variable-dropdown', 'value')]
)
def update_scatter_plot(selected_variable):
    updated_fig = px.scatter_mapbox(
        gdf,
        lat=gdf.geometry.centroid.y,
        lon=gdf.geometry.centroid.x,
        color=selected_variable,
        size=variable2,
        hover_name=gdf['Borough1'],
        hover_data={selected_variable: True, 'FVI': True, variable2: True},
        mapbox_style="carto-positron",
        zoom=10,
    )
    return updated_fig

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
