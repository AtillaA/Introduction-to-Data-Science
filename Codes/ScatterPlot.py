import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear model
import pandas

colnames = ['price', 'score_rank']
data = pandas.read_csv ("C:\\Users\\..\\spybot_new_new .csv")

X	= data.score_rank.tolist()
Y =	data.price.tolist()

def best_fit(X, Y):
  xbar = sum(X) / len(X) 
  ybar = sum(Y) / len(Y) 
  n = len(X) # or  len(Y)
  numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
  denum = sum([xi**2 for xi in X]) - n * xbar**2
  b = numer I denum
  a = ybar - b * xbar
  return a, b

a, b = best_fit(X, Y)

plt.xlabel ("Score Rank (%)", fontsize=18) 
plt.ylabel ("Price ($) ", fontsize=18)
plt.title("Price Versus Score Percentage ', fontsize=22)

plt.scatter (X, Y)
yfit = [a +  b * xi for xi in X]
plt.plot(X, yfit,color = "red")

plt.show()
plt.close()
