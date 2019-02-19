import pandas as pd, numpy as np
from sklearn import tree
from sklearn.preprocessing import LabelEncoder


full_data = pd.read_csv('titanic.csv', index_col='PassengerId')
part_data = full_data[['Pclass', 'Fare', 'Age', 'Sex', 'Survived']].dropna()
sample = part_data.loc[:, 'Pclass':'Sex']
target = part_data[['Survived']]

clf = tree.DecisionTreeClassifier(random_state=241)
enc = LabelEncoder()
sample[['Sex']] = sample[['Sex']].apply(enc.fit_transform)
print(sample)

clf.fit(sample, target)
importances = clf.feature_importances_
print(importances)
args = np.argpartition(importances, -2)[-2:]

print(list(sample.columns[args]))


