import os
import geopandas as gpd
import plotly.express as px

data_path = os.path.join("data", "KAMX_N0V_20210131_000000.shp")
data = gpd.read_file(data_path)

df = data.to_crs("WGS84")

# color_index = df['colorIndex']
# sensed = df['value']
# loc = df['geometry']

# vmin = color_index.min()
# vmax = color_index.max()


# def plot_data(colormap):
#     fig, ax = plt.subplots(figsize=(10, 10))
#     fig.suptitle('Miami Doppler Radar (KAMX), NEXRAD LEVEL III, Base Velocity', fontsize=16)
    
#     df.plot(column='colorIndex',
#             alpha=0.8,
#             cmap=colormap,
#             ax=ax)
    
#     ax.set_title('01/31/2021 00:01:01')
#     ax.set_xlabel('Long')
#     ax.set_ylabel('Lat')
    
#     normalize = mcolors.TwoSlopeNorm(vmin=vmin, vcenter=8, vmax=vmax)
    
#     scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=colormap)
#     scalarmappaple.set_array(labels)
    
#     cbar = plt.colorbar(scalarmappaple)
#     cbar.set_ticks([vmin, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, vmax])
#     cbar.set_ticklabels(['-64', '-50', '-36', '-26', '-20', '-10', '-1', '0', 
#                          '10', '20', '26', '36', '50', '64', 'RF'])
#     cbar.set_label('kts')
    
#     ctx.add_basemap(ax, zoom=10, source=ctx.providers.Stamen.TonerLite)
    
#     plt.show()


# cmap = ListedColormap(['#03dffc', '#0328fc', '#3903fc', '#03fca9', '#02d402', 
#                        '#005c00', '#a39c8e', '#5e5e5e', '#ff8c00', '#ffc800',
#                        '#f6ff00', '#8B0000', '#964B00', '#ff0000', '#4B0082'])

# plot_data(cmap)

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
   fig.show()

color_index = df['colorIndex']
palette = ['#03dffc', '#0328fc', '#3903fc', '#03fca9', '#02d402', '#005c00', 
            '#a39c8e', '#5e5e5e', '#ff8c00', '#ffc800', '#f6ff00', '#8B0000', 
            '#964B00', '#ff0000', '#4B0082']

plot_radar_data(palette, color_index.min(), color_index.max())
