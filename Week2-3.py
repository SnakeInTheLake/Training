import pandas as pd, numpy as np
from sklearn.metrics import accuracy_score
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import StandardScaler


full_data_train = pd.read_csv('perceptron-train.csv', header=None, index_col=False)
full_data_test = pd.read_csv('perceptron-test.csv', header=None, index_col=False)

x_train = full_data_train.loc[:, 1:]
y_train = full_data_train[[0]].values.ravel()

x_test = full_data_test.loc[:, 1:]
y_test = full_data_test[[0]].values.ravel()

perc = Perceptron(random_state=241)
perc.fit(x_train, y_train)
predictions = perc.predict(x_test)

acc = accuracy_score(y_test, predictions)
print(acc)

scl = StandardScaler()
x_train_std = scl.fit_transform(x_train)
x_test_std = scl.transform(x_test)

perc.fit(x_train_std, y_train)
predictions_std = perc.predict(x_test_std)
acc_std = accuracy_score(y_test, predictions_std)
print(acc_std)

ans = acc_std - acc
print(ans)
