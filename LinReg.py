# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 20:03:45 2021

@author: Jmen3
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv("AreaPriceData.csv")

plt.xlabel('area (sqr ft)')
plt.ylabel('price in US $')
plt.scatter(df.area, df.price, color = 'green', marker = '+')

reg = linear_model.LinearRegression()
reg.fit(df[['area']],df.price)

#result = reg.predict([[3300]])
#print(result)

print("coefficient")
print(reg.coef_)
print("intercept")
print(reg.intercept_)
