import os
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot

data_path = os.path.join("data", "KAMX_N0V_20210131_000000.shp")
data = gpd.read_file(data_path)

df = data.to_crs(epsg=3857)

import contextily as ctx

ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
ctx.add_basemap(ax)

plt.show()
