import csv
import pandas as pd


#need to see which rows correspond to necessary data 
with open('feederwatch_2021-2024.csv', mode='r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    #print(headers)

import pandas as pd
df = pd.read_csv('feederwatch_2021-2024.csv')

#selecting rows corresponding to lat, long, month, day, year, species_code
col_feederwatch = df[[
    'LATITUDE',
    'LONGITUDE',
    'SUBNATIONAL1_CODE',
    'Month',
    'Day',
    'Year',
    'SPECIES_CODE'
]]


#filter csv further by rows including species list and us-code
species_list = ['calhum', 'brthum', 'bkchum', 'rufhum']
states_list = ['US-AZ', 'US-CO', 'US-ID', 'US-MT', 'US-NV', 'US-NM', 'US-UT', 'US-WY']
obs_months = [2, 3, 4]

filtered_list = df.loc[
    (df['SPECIES_CODE'].isin(species_list)) &
    (df['SUBNATIONAL1_CODE'].isin(states_list)) &
    (df['Month'].isin(obs_months)),
    ['LATITUDE', 'LONGITUDE', 'SUBNATIONAL1_CODE','Month', 'Day', 'Year', 'SPECIES_CODE']
]

filtered_list.to_csv('filtered_fw.csv', index=False)

#convert day, month, year to datetime to take average 
fw = pd.read_csv('filtered_fw.csv')
fw['DATE'] = pd.to_datetime(fw[['Year', 'Month', 'Day']])
fw.to_csv('filtered_datetime.csv', index=False)

print(fw['Month'].unique()) #check to make sure data is filtered to months 2-4 to address arrival dates

#spring observation months filter
spring_obs = fw[fw['Month'].isin([2,3,4])]
spring_obs['DOY'] = spring_obs['DATE'].dt.dayofyear
mean_spring_obs = spring_obs.groupby('SPECIES_CODE')['DOY'].mean()

print(mean_spring_obs)

#mean of all spring obs to get general mean for all 4 species
print(spring_obs['DOY'].mean(), 2)

#output => 103.68 which correlates to approx. April 14th


