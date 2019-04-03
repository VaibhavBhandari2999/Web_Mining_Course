import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
import itertools
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


dataset = pd.read_csv('wine.data.csv')
print(dataset.head())

X = dataset.iloc[:,:14].values
y = dataset.iloc[:,:14].values

print(X)
#print(y)



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 82)
nvclassifier = GaussianNB()
nvclassifier.fit(X_train, y_train)
