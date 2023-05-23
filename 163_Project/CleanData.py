import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd


def main():
    suicide = pd.read_csv('suicide.csv')
    mental_health = pd.read_csv('mental_health.csv', low_memory=False)
    #print(mental_health.iloc[6468]['Year'])
    #mental_health['Year'].astype(str).str.isdigit()
    #mental_health['Year'].astype(str).astype(int)3
    #RN: convert a object to a int 
    mental_health.dropna(inplace=True)
    #print(mental_health['Year'].head())
    mental_health['Year'] = pd.to_numeric(mental_health['Year'])
    #print(mental_health.loc[[6468]])
    #pd.to_numeric(mental_health['Year'])
    #print specific rows and seeing year 
    #print('at our specific index 6468', mental_health.loc[6468,:]) 
    #ValueError: Unable to parse string "Year" at position 6468
    #print('this is our dtype:', mental_health['Year'].dtypes) #now we have int64 
    #print(mental_health.head())
    suicide['country'] = suicide['country'].replace({'Russian Federation': 'Russia'})
    merged = suicide.merge(mental_health, left_on=['country', 'year'], right_on=['Entity', 'Year'])
    # only_na = merged['country'] != merged['Entity']
    # merged = merged[only_na] #current issue filtering out too many countries 
    #merged_global = merged_global.drop(['geometry'], axis = 1)

    merged.to_csv('merged.csv', index=False) # We already have this file 
    #USE MERGED FROM NOW ON BECUASE IT IS MERGED TOGETHER 
    merged = merged.drop(['Entity', 'Year'], axis=1) #SINGLE AXIS
    #print(len(merged.columns))

    #the idea: Try clean and make same type for both years to be the same thing 
    #now we have merged our data so it will be easy to implement later 
    
if __name__ == '__main__':
    main()
