import pandas as pd
data = pd.read_csv('titanic.csv', index_col='PassengerId')
sex = data['Sex'].value_counts()

survivors = data['Survived'].value_counts(normalize=True) * 100

clss = data['Pclass'].value_counts(normalize=True) * 100

mean_age = data['Age'].mean()
med_age = data['Age'].median()

sibs = data['SibSp']
parch = data['Parch']

correlation = sibs.corr(parch, method='pearson')

names = data['Name']
first_names = []
for name in names:
    if 'Miss.' in name:
        first_names.append(name.split('Miss.')[1].strip().split()[0])
    if 'Mrs.' in name and '(' not in name:
        first_names.append(name.split('Mrs.')[1].strip().split()[0])
    elif 'Mrs.' in name and '(' in name:
        first_names.append(name.split('(')[1].strip().split()[0].split(')')[0].strip())

fn = pd.DataFrame(first_names)
print(fn[0].value_counts())
# print(names.value_counts())

