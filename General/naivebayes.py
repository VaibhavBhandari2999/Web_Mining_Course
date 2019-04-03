# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 16:52:04 2018

@author: vbhan
"""

#%%

from sklearn.datasets import fetch_20newsgroups

data = fetch_20newsgroups()
data.target_names
#%%
train = fetch_20newsgroups(subset='train')
test = fetch_20newsgroups(subset='test')
#%%

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

model = make_pipeline(TfidfVectorizer(), MultinomialNB())
#%%
model.fit(train.data, train.target)
labels = model.predict(test.data)
#%%
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
mat = confusion_matrix(test.target, labels)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=train.target_names, yticklabels=train.target_names)
plt.xlabel('true label')
plt.ylabel('predicted label');
#%%
def predict_category(s, train=train, model=model):
    pred = model.predict([s])
    return train.target_names[pred[0]]
#%%
predict_category('discussing islam vs atheism')