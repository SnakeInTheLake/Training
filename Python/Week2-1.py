import pandas as pd, numpy as np
from sklearn.model_selection import KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import scale


names = ['Class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols',
         'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue',
         'OD280/OD315 of diluted wines', 'Proline']
full_data = pd.read_csv('wine.data', header=None, names=names, index_col=False)
classes = full_data[['Class']]
y = classes.values.ravel()
props = full_data.loc[:, 'Alcohol':]

kf = KFold(n_splits=5, shuffle=True, random_state=42)

props_norm = scale(props)

scores = []
for i in range(1, 51):
    neigh = KNeighborsClassifier(n_neighbors=i)
    cvs = cross_val_score(neigh, props_norm, y, cv=kf)
    scores.append(cvs.mean())
scores = np.asarray(scores)
print(scores)
print(scores.max(), scores.argmax() + 1)