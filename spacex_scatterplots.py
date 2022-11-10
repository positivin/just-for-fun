# andas is a software library written for the Python programming language for data manipulation and analysis.
import pandas as pd
#NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
import numpy as np
# Matplotlib is a plotting library for python and pyplot gives us a MatLab like plotting framework. We will use this in our plotter function to plot data.
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime

df=pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv")
#with open('spacex_part_2.csv') as file:
    #df=pd.read_csv(file)

#plt.scatter(y=df["PayloadMass"], x=df["FlightNumber"], c = df["Class"]) # it works as (y="PayloadMass", x="FlightNumber", data=df)
#plt.xlabel("Flight Number",fontsize=20)
#plt.ylabel("Pay load Mass (kg)",fontsize=20)
#plt.show()

#plt.scatter(y=df["LaunchSite"], x=df["FlightNumber"], c = df["Class"]) # it works as (y="PayloadMass", x="FlightNumber", data=df)
#plt.xlabel("Flight Number",fontsize=20)
#plt.ylabel("LaunchSite",fontsize=20)
#plt.show()

#plt.scatter(y=df["LaunchSite"], x=df["PayloadMass"], c = df["Class"]) # it works as (y="PayloadMass", x="FlightNumber", data=df)
#plt.xlabel("Pay load Mass (kg)",fontsize=20)
#plt.ylabel("LaunchSite",fontsize=20)
#plt.show()

orbit = df['Class'].groupby(df['Orbit']).mean()

#orbit.plot(kind='bar')

#plt.scatter(y=df['Orbit'], x=df["FlightNumber"], c = df["Class"]) # it works as (y="PayloadMass", x="FlightNumber", data=df)
#plt.xlabel("FlightNumber",fontsize=20)
#plt.ylabel("Orbit",fontsize=20)
#plt.show()

#plt.scatter(y=df['Orbit'], x=df["PayloadMass"], c = df["Class"]) # it works as (y="PayloadMass", x="FlightNumber", data=df)
#plt.xlabel("Pay load Mass (kg)",fontsize=20)
#plt.ylabel("Orbit",fontsize=20)
#plt.show()

years = [datetime.strptime(i, '%Y-%m-%d').year for i in list(df['Date'])]
df['Years'] = years

years_success = df['Class'].groupby(df['Years']).mean()

#years_success.plot()
#plt.ylabel("Rate of Success",fontsize=20)
#plt.show()

features = df[['FlightNumber', 'PayloadMass', 'Orbit', 'LaunchSite', 'Flights', 'GridFins', 'Reused', 'Legs', 'LandingPad', 'Block', 'ReusedCount', 'Serial']]

features_one_hot = pd.get_dummies(features[['Orbit', 'LaunchSite', 'LandingPad', 'Serial']])

features_one_hot = features_one_hot.astype('float64')

features_one_hot = pd.concat([features, features_one_hot], axis = 1)
features_one_hot.to_csv('dataset_part_3.csv', index=False)