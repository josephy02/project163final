import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import os
os.environ['SHAPE_RESTORE_SHX'] = 'YES'


def load_in_data() -> gpd.GeoDataFrame:
    data = pd.read_csv('merged.csv')
    global_data = gpd.read_file('geo_data/ne_110m_admin_0_countries.shp')
    global_data.dropna()
    global_data['NAME'] = global_data['NAME'].replace({'United States of America': 'United States'})
    #print(global_data['NAME'].head(20))
    global_data = global_data[['NAME', 'geometry']] #delete all columns except name and geometry  
    merged_global = global_data.merge(data, left_on='NAME', right_on='country', how="left")
    #only_na = merged_global['NAME'] != merged_global['country']
    #merged_global = merged_global[only_na] #current issue filtering out too many countries 
    #merged_global = merged_global.drop(['geometry'], axis = 1)
    #Emerged_global.to_csv('missing_countries.csv', index=False) # We already have this file 
    #print(merged_global)
    #na_index = merged_global.index[only_na]
    #print(na_index)
    #merged_global.dropna(subset=['NAME'], inplace=True)
    #print(merged_global['country'].equals(merged_global['NAME']))
    #merged = merged_global.drop(['NAME'], axis=1)
    #merged.sort_values(by=['country'])
    #merged.to_csv('final_map_merged_data.csv', index=False) # We already have this file 
    #print(merged.columns)
    #print(merged.head())
    #merged.plot()
    #merged_data = global_data.merge(data,'')
    #print(global_data['NAME'].head())
    #global_data.plot()
    #plt.savefig('world.png')
    #merge_data = global_data.merge(data, how='outer')
    #return merge_data with both combined together 
    return(merged_global)

def plot_map_global(global_data: gpd.GeoDataFrame) -> None: #this makes the map globally 
    global_map = gpd.read_file('geo_data/ne_110m_admin_0_countries.shp') 
    global_map.dropna()
    global_map.plot()
    plt.title('Plot of the global map around the world')
    #plt.savefig('global_map.png')

def depression(global_data: gpd.GeoDataFrame) -> None:
    fig, ax = plt.subplots(1) 
    #dissolved_gdf = filtered_gdf.dissolve(by='country', aggfunc='mean')
    #dissolved_gdf.plot(ax=ax, column='Drug use disorders (%)', legend=True) 
    global_data = global_data[['country', 'year', 'geometry', 'Depression (%)']]
    choose_year = global_data['year'] == 2000
    year_data = global_data[choose_year]
    grouping = year_data.dissolve(by='country', aggfunc='sum')
    global_data.plot(ax=ax, color='#EEEEEE')
    grouping.plot(ax=ax, column='Depression (%)', legend=True) 
    plt.title('Global Percentage of Depression in 2000')
    plt.savefig('depression.png')
    

#def updated_map_global(global_map: gpd.GeoDataFrame) -> None:
#     global_map = global_map['country', 'year']
#     filter_year = global_map['year'] == 1991
#     filter_map = filter_map[filter_year & filter_map.unique()]
#     filter_map.plot()
#     plt.title('updated map around world')
#     plt.savefig('updated_global_map.png')

#increment years by 5 -> 1995 2000 2010 2015 and compare constrast different data 

#compare gdp vs. depression 

def plot_gdp_global(global_map: gpd.GeoDataFrame) -> None:
    #just 2000 2005 2010 2015
    #ORIGINAL ATTEMPT WORKS FOR YEAR 2000
    fig, ax = plt.subplots(1)
    filter_data = global_map[['gdp_per_capita ($)', 'year', 'country', 'geometry']]
    filter_year = filter_data['year'] == 2000
    #filter_gdp = filter_data['gdp_per_capita ($)']
    updated_data = filter_data[filter_year] #access just your year and gdp of that year
    updated_data = updated_data.dissolve(by='country', aggfunc='mean')
    global_map.plot(color='#EEEEEE', ax=ax)
    updated_data.plot(column='gdp_per_capita ($)', legend=True, ax=ax)
    plt.title('GDP of 2000 globally')
    plt.savefig('GDP_2000_global')
   
    
    
    
    

def plot_global_drug_use(global_data: gpd.GeoDataFrame) -> None:
    #for the years 2000 2005 2010 2015
    fig, ax = plt.subplots(1) 
    gdf = global_data[['year', 'geometry', 'country', 'Drug use disorders (%)']]
    filtered_gdf = gdf[gdf['year'] == 2000]
    dissolved_gdf = filtered_gdf.dissolve(by='country', aggfunc='mean')
    global_data.plot(ax=ax, color='#EEEEEE')
    dissolved_gdf.plot(ax=ax, column='Drug use disorders (%)', legend=True) 
    plt.title('Global Percentage of Drug Use in 2000')
    plt.savefig('drugs.png')

    
    
def plot_map_gdp() -> None:
    pass
#steps of ACTION:
#1) merge maps with our dataset 
#2) Plot our map to see what we have currently
#3) make a method that layers or plots and shows the difference between GDP and country 
#4) make a method that shows suicide rate changes with a legend in differenet time frames 

def main():
    global_data = load_in_data() #global_map  or can assign global map variable and pass it in 
    plot_map_global('geo_data/ne_110m_admin_0_countries.shp')
    plot_gdp_global(global_data)
    depression(global_data)
    #updated_map_global(global_map)
    plot_global_drug_use(global_data)
    



if __name__ == '__main__':
    main()