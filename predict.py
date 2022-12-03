# -*- coding: utf-8 -*-
"""Predict.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FjA_O4u7H2to-VQfB8_DwJ2X6Ub85RBf
"""

import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

"""# Loading data"""

df = pd.read_parquet('/content/drive/MyDrive/Data/BMTC.parquet.gzip', engine='pyarrow') # This command loads BMTC data into a dataframe. 
                                                                      # In case of error, install pyarrow using: 
                                                                      # pip install pyarrow
dfInput = pd.read_csv('/content/drive/MyDrive/Data/Input.csv')
dfGroundTruth = pd.read_csv('/content/drive/MyDrive/Data/GroundTruth.csv')

"""# EDA"""

g1=df.groupby('BusID')
unique=df.BusID.unique()

d1 = df.drop_duplicates(subset=['Latitude','Longitude','Speed'],keep=("first"),inplace=False)
d2 = df.drop_duplicates(subset=['Latitude','Longitude','Speed'],keep=("last"),inplace=False)
d3 = pd.concat([d1,d2.loc[set(d2.index) - set(d1.index)]])

import numpy as np
#haversine
from numpy import radians, cos, sin, arcsin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """

    #Convert decimal degrees to Radians:
    lon1 = np.radians(lon1.values)
    lat1 = np.radians(lat1.values)
    lon2 = np.radians(lon2.values)
    lat2 = np.radians(lat2.values)

    #Implementing Haversine Formula: 
    dlon = np.subtract(lon2, lon1)
    dlat = np.subtract(lat2, lat1)

    a = np.add(np.power(np.sin(np.divide(dlat, 2)), 2),  
                          np.multiply(np.cos(lat1), 
                                      np.multiply(np.cos(lat2), 
                                                  np.power(np.sin(np.divide(dlon, 2)), 2))))
    c = np.multiply(2, np.arcsin(np.sqrt(a)))
    r = 6371

    return c*r

from datetime import datetime
def time_delta(initial,final):
                       # Now
  final1=datetime(final)
  initial1=datetime(initial)
  duration = final1-initial1                        # For build-in functions
  duration_in_s = duration.total_seconds()
        # Total number of seconds between dates
  return duration_in_s

d4=d3.loc[:,["Latitude",'Longitude']]
d7=d3.shift(1)
d5=d4.shift(periods=1, freq=None, axis=0)
d5.rename(columns = {'Latitude':'Source_Lat', 'Longitude':'Source_Long'}, inplace = True)
d4.rename(columns = {'Latitude':'Dest_Lat', 'Longitude':'Dest_Long'}, inplace = True)
d6=pd.concat([d5,d4], axis=1)
distance=haversine(d4['Dest_Long'],d4['Dest_Lat'],d5['Source_Long'],d5['Source_Lat'])
time=d3['Timestamp']-d7['Timestamp']
time=time.apply(lambda x: x.seconds/60)
d6['Distance']=distance
d6['Duration']=time


# speed=d6['Distance']/d6['Duration']
# d6['Speed']=speed

d6.columns

d6.columns

d6.head()

d6.replace([np.inf, -np.inf], np.nan, inplace=True)
d6.drop(d6.tail(2).index,
        inplace = True)
d6.drop(d6.head(2).index,
        inplace = True)

pd.set_option('mode.use_inf_as_na', True)
d6.dropna(how='any', inplace=True)
# check = d6[d6.isna().any(axis=1)]
# check
# yy=d6['Duration']
# d6.drop(['Duration'],axis=1)

d6

from sklearn.linear_model import LinearRegression

X_train=d6.drop(['Duration'],axis=1)

X_train

y_train=d6['Duration']

y_train

test_df=pd.read_csv('/content/drive/MyDrive/Data/Input.csv')
distance1=haversine(test_df['Dest_Long'],test_df['Dest_Lat'],test_df['Source_Long'],test_df['Source_Lat'])
test_df['Distance']=distance1
print(test_df.columns)
test_df.drop("Unnamed: 0",axis=1,inplace=True)

X_test=test_df

X_test
X = X_test['Distance'].isna()
c=0
for i in X:
  if i :
    print(X_test[c])
  c+=1
print(c)

X_test.replace([np.inf, -np.inf], np.nan, inplace=True)
# X_test.drop(X_test.tail(2).index,
#         inplace = True)
# X_test.drop(X_test.head(2).index,
#         inplace = True)

#pd.set_option('mode.use_inf_as_na', True)

y_test=pd.read_csv('/content/drive/MyDrive/Data/GroundTruth.csv')
print(y_test.columns)
y_test.drop("Unnamed: 0",axis=1,inplace=True)

X_test=pd.concat([X_test,y_test], axis=1)
X_test.dropna(how='any', inplace=True)

y_test=X_test['TT']
X_test.drop('TT',axis=1,inplace=True)

"""# Linear Regression Model"""

reg_model=LinearRegression()

reg_model.fit(X_train, y_train)

print(reg_model.score(X_test, y_test))

"""# Random Forest Model"""

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from tqdm import tqdm
import time

from sklearn.model_selection import train_test_split
Xtrain,Xtest,ytrain,ytest = train_test_split(X_train,y_train, train_size = 0.006, random_state=42)

forest_model = RandomForestRegressor(random_state=1,oob_score=True,)
forest_model.fit(Xtrain,ytrain)
print("yes")

melb_preds = forest_model.predict(X_test)
print(mean_absolute_error(y_test, melb_preds))