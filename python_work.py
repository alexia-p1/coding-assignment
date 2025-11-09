##lists, dictionaries, forloops##
l = [1, 2, 'a', True, 0.5]
for element in l:
    print(element)

l2= [3,4, False, 'c', 2.5]

l3 = l + l2
print(l3)

l3.remove(False)
print(l3)

christmas_market_stalls= {
        'Rathausplatz':96,
        'Belvedere':42,
        'Schonbrunn': 99,
          }

type(christmas_market_stalls)


for key, value in christmas_market_stalls.items():
    print('The number of stalls in the', key, 'Christmas market is', value, '.')

#changing directory to where the data is stored
import os
current_directory = os.getcwd()
current_directory
#print(os.getcwd())
#new_directory = 'coding_assignment\coding-assignment'
#os.chdir(new_directory)
print(os.getcwd())

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

##cleaning data
data = pd.read_csv('hotels-vienna.csv')
df = data.assign(nnights = 1)
del data
print(df.columns)

print(df['accommodation_type'].dtype)
print(df['accommodation_type'].value_counts(dropna=False))

df['rating'] = df['rating'].astype(float)
df['rating'].dtypes
df['rating'].value_counts()

#filtering observations 
df.shape
df.loc[df['accommodation_type'] == 'Apartment']
df['accommodation_type'].loc[df['accommodation_type'] == 'Apartment'].value_counts()
print(df['rating'].isnull().sum())
df = df.loc[df['rating'].notnull()]
df = df.dropna(subset=['rating'])
df.shape

print(df.duplicated().sum())

# filtering variables
columns_keep = ['price', 'accommodation_type', 'rating', 'stars']
df1 = df[columns_keep]
print(df1.columns)
print(df1.describe())

# creating new variable
df['distcat'] = np.where(df['distance'] < 1,'close','far')
print(df['distcat'].value_counts())


#graph
df1.price.hist(bins=30)
plt.xlabel('Price in Euro')
plt.ylabel('Number of accommodations')

#import os
#os.mkdir("python_output")
df.to_csv('python_output/hotels-clean.csv', index=False)