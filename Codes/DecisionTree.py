import matplotlib. pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear model
from sklearn import tree
from os import system


def func (x):
  try :
    return int(x)
  except ValueError:
    return x


clf = tree.DecisionTreeClassifier()
with open ("C:\\Users\\..\\DTreeData.csv") as f:
  table_data = [[func(x) for x in line.split()] for line in f]

data = pd.read_csv("C:\\Users\\..\\DTreeData2.csv")
Y = data.price.tolist()
#inputs: score rank,owners
#output: price

print (len (Y))
print (len (table_data))
clf = clf.fit(table_data, Y)
prediction = clf.predict([[60, 3000000]])

clf	= tree.DecisionTreeClassifier() 
clf	= clf.fit(table_data, Y)

tree.export_graphviz(clf, filled=True, rounded=True, impurity=False, out_file= 'tree.dot')
