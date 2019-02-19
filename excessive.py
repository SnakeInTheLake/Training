import sys
sys.stdin = open("input.txt", "r")

def parents(err):
    for values in base[err]:
        for i in range(len(base[values])):
            if base[values][i] not in base[err]:
                base[err].append(base[values][i])

def checker(arr):
    while len(arr) > 0:
        x = arr.pop()
        for e in arr:
            if e in base[x]:
                out.append(x)
                return(checker(arr))

base = {}
out = []

for com in [input().strip().split() for i in range(int(input()))]:
    base[com[0]] = com[2:len(com)]

order = [input().strip() for j in range(int(input()))]
print(order)
for child in order:
    parents(child)
print(base)
checker(order)


