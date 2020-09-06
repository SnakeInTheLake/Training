import sys


def in_order(tree, root):
    if tree[root][0] != -1:
        in_order(tree, tree[root][0])
    if tree[root][0] == -1:
        lst.append([tree[root][1], -1])
    else:
        lst.append([tree[root][1], tree[tree[root][0]][1]])
    if tree[root][2] != -1:
        in_order(tree, tree[root][2])
    return ''


def checker(lst):
    for i in range(1, len(lst)):
        if lst[i][0] < lst[i-1][0]:
            return 'INCORRECT'
        elif lst[i][0] == lst[i-1][0] and lst[i][0] == lst[i][1]:
            return 'INCORRECT'
    return 'CORRECT'


def main():
    global lst
    lst = []
    tree = []
    elements = int(input())
    for _ in range(elements):
        key, left, right = map(int, input().strip().split())
        tree.append([left, key, right])
    if tree:
        in_order(tree, 0)
    print(checker(lst))


def test():
    with open('1.txt', 'r') as inp:
        elements = int(inp.readline().strip())
        tree = []
        for line in inp:
            key, left, right = map(int, line.strip().split())
            tree.append([left, key, right])

    print(tree)
    global lst
    lst = []
    if tree:
        in_order(tree, 0)
    print(lst)
    print(checker(lst))


if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    #main()
    test()