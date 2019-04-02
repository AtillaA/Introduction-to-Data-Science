import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear model
from sklearn import tree

def func(x):
  try :
    return float(x)
  except ValueError:
    return x

elf = tree .DecisionTreeClassi fier()
with open ("C:\\Users\\ATILLA\\Desktop\\CS210\\spybot_dtree.csv") as f:
  table_data = [[func(x) for x in line.split()] for line in f]

data = pd .read_csv("C:\\Users\\..\\spybot_edited.csv")
Y = data.score_rank.tolist()

#print (Len(Y))
#print (Len(table_data))
clf = clf.fit(table_data, Y)
prediction = clf.predict([[0, 98000000]])

if prediction > 50:
  print (prediction, '%', " of gamers do like this game.")
elif prediction == 50:
  print ("Gamers are ambivalent about this game.")
else :
  prediction_new = 100 - prediction
  print (prediction_new, '%', " of gamers do not like this game.")
