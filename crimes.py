import csv
from collections import Counter

crimes_list = []
with open('Crimes.csv') as crimes:
    content = csv.reader(crimes)
    for row in content:
        if '2015' in row[2]:
            crimes_list.append(row[5])

d = dict(Counter(crimes_list))
print(max(d.keys(), key=lambda key: d[key]))
print(Counter(d).most_common(1))
