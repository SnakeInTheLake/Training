import pandas as pd, numpy as np
from sklearn.model_selection import KFold
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import scale
from sklearn import datasets


data = datasets.load_boston()
x = data.data
y = data.target
x = scale(x)

kf = KFold(n_splits=5, shuffle=True, random_state=42)
kf.split(x)

scores = []
for i in np.linspace(1, 10, 200):
    neigh_regr = KNeighborsRegressor(n_neighbors=5, weights='distance', p=i)
    cvs = cross_val_score(neigh_regr, x, y, scoring='neg_mean_squared_error', cv=kf)
    scores.append(cvs.mean())
scores = np.asarray(scores)
print(scores)
print(scores.max(), scores.argmax() + 1)
