#%%
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
#%%
from sklearn.datasets import make_blobs
X,y=make_blobs(100,2,centers=2,random_state=2,cluster_std=1.5)
plt.scatter(X[:,0],X[:,1],c=y,s=50,cmap='RdBu');
#%%
plt.show()
from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(X,y);

#%%
plt.scatter(X[:,0],X[:,1],c=y,s=50,cmap='RdBu')
lim=plt.axis()
plt.scatter(Xnew[:,0],Xnew[:,1],c=ynew,s=20,cmap='RdBu',alpha=0.1)
plt.axis(lim)
plt.show()

#%%
yprob=model.predict_proba(Xnew)
yprob[-8:].round(2)