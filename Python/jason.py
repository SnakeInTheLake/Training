import json


def parents(child):
    for values in inheritance[child]:
        for i in range(len(inheritance[values])):
            if inheritance[values][i] not in inheritance[child]:
                inheritance[child].append(inheritance[values][i])


inp = '[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, ' \
      '{"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]' #input()
classes = json.loads(inp)
inheritance = {}
ans = {}

for element in classes:
    inheritance[element['name']] = element['parents']

for ch in inheritance:
    parents(ch)

for keys in inheritance:
    children = 1
    for i in list(inheritance.values()):
        if keys in i:
            children += 1
    ans[keys] = children

for key in sorted(ans):
    print(f'{key} : {ans[key]}')

