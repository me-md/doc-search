# %matplotlib inline

import geopandas as gpd
# from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt
import pandas as pd
import os
import folium
# plt.rcParams['figure.figsize'] = (10,8)

data_pth = "./Data/"
usa= gpd.read_file(os.path.join(data_pth, 'states.shp'))

def state_plotter(states, us_map=True):
    fig, ax = plt.subplots(figsize=(10,10))

    if us_map:
        if 'HI' in states:
            usa[0:50].plot(ax=ax, alpha = 0.3)
        elif 'AK' in states:
            usa[1:51].plot(ax=ax, alpha = 0.3)
        elif 'AK' and 'HI' in states:
            usa[0:51].plot(ax=ax, alpha = 0.3)
        else:
            usa[1:50].plot(ax=ax, alpha = 0.3)
        #ax=ax makes the map plot on the initial matplotlib figure
        for n in states:
            usa[usa.STATE_ABBR == f'{n}'].plot(ax=ax, edgecolor='y', linewidth = 1)

    elif us_map == False:
        for n in states:
            usa[usa.STATE_ABBR == f'{n}'].plot(ax=ax, edgecolor='y', linewidth =2)

# m = folium.Map(location=[45.5236, -122.6750])

# usa[usa.STATE_ABBR == 'TX'].plot()
# usa[usa.SUB_REGION == 'East North Central'].plot()
state_plotter(['LA', 'AR'])


# usa.plot()
plt.show(m)



# import geopandas as gpd
# import matplotlib.pyplot as plt
# plt.rcParams['figure.figsize'] = (10,8)
# from shapely.geometry import Point, Polygon
# import pandas as pd
# import descartes
# import shapely
# import os

# import folium
# data_pth = "./Data/"
# fig, ax = plt.subplots(1, 1)

# world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# northAmerica = world.query('continent == "North America"')
# usa = northAmerica.query('name == "United States of America"')
# cities = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))
# cities = gpd.read_file(os.path.join(data_pth, "ne_10m_populated_places.shp"))
# usa= gpd.read_file(os.path.join(data_pth, 'states.shp'))

# world['gdp_per_cap'] = world.gdp_md_est / world.pop_est


# world.plot(color='lightgrey', linewidth=0.5, edgecolor='white', figsize=(15,10))
# base = usa.plot()
# base = usa.plot(column='pop_est', ax=ax, legend=True, figsize=(20,10))

# base = world.plot(column='pop_est', ax=ax, legend=True, figsize=(15,10))
# cities.plrot(ax=base,figsize=(15,10), color='orange', markersize= 1)
