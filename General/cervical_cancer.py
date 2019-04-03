#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
import itertools
from sklearn import svm, datasets
dataset = pd.read_csv('risk_factors_cervical_cancer.csv')
#%%
dataset.head()
X = dataset.iloc[:,:33].values
y = dataset.iloc[:,33].values
#%%
X
Y
#%%
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 80)
nvclassifier = GaussianNB()
nvclassifier.fit(X_train, y_train)
y_pred = nvclassifier.predict(X_test)
print(y_pred)
#%%
from sklearn.metrics import confusion_matrix
confmat = confusion_matrix(y_test, y_pred)
np.set_printoptions(precision=2)
print(confmat)
#%%
a = confmat.shape
corrPred = 0
falsePred = 0

for row in range(a[0]):
    for c in range(a[1]):
        if row == c:
            corrPred +=confmat[row,c]
        else:
            falsePred += confmat[row,c]
print('Correct predictions: ', corrPred)
print('False predictions', falsePred)
print ('\n\nAccuracy of the Naive Bayes Clasification is: ', corrPred/(confmat.sum()))
