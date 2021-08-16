import os
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import geopandas as gpd
from matplotlib import cm
from matplotlib.colors import ListedColormap

data_path = os.path.join("data", "KAMX_N0V_20210131_000000.shp")
data = gpd.read_file(data_path)

# print(data.head(10))

color_index = data['colorIndex']
labels = data['value']
vmin = color_index.min()
vmax = color_index.max()

def plot_data(cmap):
    fig, ax = plt.subplots(figsize=(10, 10))
    data.plot(column='colorIndex',
            cmap=cmap,
            ax=ax)
    fig.suptitle('Miami Doppler Radar (KAMX), NEXRAD LEVEL III, Base Velocity', fontsize=16)
    ax.set_title('01/31/2021 00:01:01')
    ax.set_xlabel('Long')
    ax.set_ylabel('Lat')
    
    normalize = mcolors.TwoSlopeNorm(vmin=vmin, vcenter=8, vmax=vmax)
    
    scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=cmap)
    scalarmappaple.set_array(labels)
    cbar = plt.colorbar(scalarmappaple)
    cbar.set_ticks([vmin, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, vmax])
    cbar.set_ticklabels(['-64', '-50', '-36', '-26', '-20', '-10', '-1', '0', 
                         '10', '20', '26', '36', '50', '64', 'RF'])
    cbar.set_label('kts')
    
    plt.show()

cmap = ListedColormap(['#03dffc', '#0328fc', '#3903fc', '#03fca9', '#02d402', 
                       '#005c00', '#a39c8e', '#5e5e5e', '#ff8c00', '#ffc800',
                       '#f6ff00', '#8B0000', '#964B00', '#ff0000', '#4B0082'])

plot_data(cmap)
