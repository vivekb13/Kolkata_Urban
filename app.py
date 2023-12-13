import streamlit as st
import geopandas as gpd
import plotly.express as px

# Load the Shapefile
shapefile_path = r"C:\Users\91956\Desktop\SEMESTER 3\kolk_data\kolk_data\kolk_data.shp"
gdf = gpd.read_file(shapefile_path)

# Define initial variables for visualization
variable2 = 'Slum_pop'
# Define Streamlit app
st.title("Kolkata Metropolitan Data")
# Dropdown for variable selection
selected_variable = st.selectbox(
    "Select Variable",
    ['Avg_Temp', 'Urban_Wate', 'Water_Avai', 'FVI'],
    index=0  # Set the initial index
)

# Create an interactive scatter plot on the map based on the selected variable
scatter_fig = px.scatter_mapbox(
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

# Display the scatter plot
st.plotly_chart(scatter_fig)
