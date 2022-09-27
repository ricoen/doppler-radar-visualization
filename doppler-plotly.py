import os
import geopandas as gpd
import plotly.express as px
import plotly.io as pio


pio.renderers.default = "firefox"

data_path = os.path.join("data", "TJUA_V06_20220810_000211.shp")
data = gpd.read_file(data_path)

df = data.to_crs("WGS84")
sensed = df['value']

def plot_radar_data():
   vmin = sensed.min()
   vmax = sensed.max()
   
   fig = px.choropleth_mapbox(df, geojson=df.geometry, locations=df.index, 
                              color="value", 
                              color_continuous_scale="jet", 
                              range_color=(vmin, vmax), 
                              mapbox_style="carto-positron",
                              zoom=9, center={"lat": 18.122793, "lon": -66.082846},
                              labels={'value':'dBZ'}
                           )
   
   fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},
                     title={"text":"San Juan (TJUA), NEXRAD LEVEL II",
                              "xanchor":"center",
                              "yanchor":"top",
                              "x":0.5})
   fig.update_traces(
      hovertemplate=None,
      hoverinfo='skip',
      marker_line_width=0
   )
   
   pio.show(fig)

# palette = ["turbo"]

plot_radar_data()
