from sklearn import svm
import pandas as pd
import numpy as np
import pickle

data = pd.read_csv("heart.csv") 

X = data.drop(['target'], axis = 1).values
y = data['target'].values

clf = svm.SVC()
clf.fit(X,y)

pickle.dump(clf, open('svm_heart,pkl', 'wb'))

