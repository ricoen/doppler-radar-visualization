import os
import geopandas as gpd
import plotly.express as px
import plotly.io as pio


pio.renderers.default = "browser"

data_path = os.path.join("data", "KAMX_N0V_20210131_000000.shp")
data = gpd.read_file(data_path)

df = data.to_crs("WGS84")

def plot_radar_data(color_map, vmin, vmax):
   fig = px.choropleth_mapbox(df, geojson = df.geometry, locations = df.index, 
                              color = "colorIndex", 
                              color_continuous_scale = color_map, 
                              range_color = (vmin, vmax), 
                              mapbox_style = "carto-positron",
                              zoom = 9, center = {"lat": 25.6353, "lon": -80.4171},
                              hover_data = ["value", "colorIndex"],
                              labels={'colorIndex':'Color Index'}
                           )
   fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
   pio.show(fig)

color_index = df['colorIndex']
palette = ['#03dffc', '#0328fc', '#3903fc', '#03fca9', '#02d402', '#005c00', 
            '#a39c8e', '#5e5e5e', '#ff8c00', '#ffc800', '#f6ff00', '#8B0000', 
            '#964B00', '#ff0000', '#4B0082']

plot_radar_data(palette, color_index.min(), color_index.max())
