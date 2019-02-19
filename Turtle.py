n = int(input())
d = {'север': 0, 'юг': 0, 'запад': 0, 'восток': 0}
l = []
for i in range(n):
    l.append(input().split())

for i in range(n):
    if l[i][0] in d:
        d[l[i][0]] += int(l[i][1])

destination = [0, 0]
for key in d:
    if key == 'север':
        destination[1] += d.get(key)
    elif key == 'юг':
        destination[1] -= d.get(key)
    elif key == 'восток':
        destination[0] += d.get(key)
    else:
        destination[0] -= d.get(key)
print(*destination)
