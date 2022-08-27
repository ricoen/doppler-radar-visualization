import os
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import contextily as ctx
import matplotlib.colors as mcolors
# from matplotlib.colors import ListedColormap


data_path = os.path.join("data", "TJUA_V06_20220810_000211.shp")
data = gpd.read_file(data_path)

df = data.to_crs(epsg=3857)

# print(df["value"])

sensed = df["value"]

def plot_data(colormap):
    vmin = sensed.min()
    vmax = sensed.max()

    fig, ax = plt.subplots(figsize=(10, 10))
    fig.suptitle("San Juan (TJUA), NEXRAD LEVEL II", fontsize=16)
    
    df.plot(column="value",
            alpha=0.8,
            cmap=colormap,
            ax=ax)
    
    ax.set_title("08/10/2022 00:02:11")
    ax.set_xlabel("Long")
    ax.set_ylabel("Lat")
    
    normalize = mcolors.TwoSlopeNorm(vmin=vmin, vcenter=8, vmax=vmax)
    
    scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=colormap)
    scalarmappaple.set_array(sensed)
    
    cbar = plt.colorbar(scalarmappaple)
    # cbar.set_ticks([vmin, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, vmax])
    # cbar.set_ticklabels(["-64", "-50", "-36", "-26", "-20", "-10", "-1", "0", 
    #                      "10", "20", "26", "36", "50", "64", "RF"])
    cbar.set_label("dBZ")
    
    ctx.add_basemap(ax, zoom=10, source=ctx.providers.Stamen.TonerLite)
    
    plt.show()


# cmap = ListedColormap(["#03dffc", "#0328fc", "#3903fc", "#03fca9", "#02d402", 
#                        "#005c00", "#a39c8e", "#5e5e5e", "#ff8c00", "#ffc800",
#                        "#f6ff00", "#8B0000", "#964B00", "#ff0000", "#4B0082"])

cmap = "jet"

plot_data(cmap)
