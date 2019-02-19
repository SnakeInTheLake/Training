def in_order(tree, root):
    if tree[root][0] != -1:
        in_order(tree, tree[root][0])
    print(tree[root][1], end=' ')
    if tree[root][2] != -1:
        in_order(tree, tree[root][2])
    return ''


def pre_order(tree, root):
    print(tree[root][1], end=' ')
    if tree[root][0] != -1:
        pre_order(tree, tree[root][0])
    if tree[root][2] != -1:
        pre_order(tree, tree[root][2])
    return ''


def post_order(tree, root):
    if tree[root][0] != -1:
        post_order(tree, tree[root][0])
    if tree[root][2] != -1:
        post_order(tree, tree[root][2])
    print(tree[root][1], end=' ')
    return ''


def main():
    elements = int(input())
    tree = []
    for _ in range(elements):
        key, left, right = map(int, input().strip().split())
        tree.append([left, key, right])
    print(in_order(tree, 0))
    print(pre_order(tree, 0))
    print(post_order(tree, 0))


def test():
    with open('1.txt', 'r') as inp:
        elements = int(inp.readline().strip())
        tree = []
        for line in inp:
            key, left, right = map(int, line.strip().split())
            tree.append([left, key, right])

    print(tree)
    print(in_order(tree, 0))
    print(pre_order(tree, 0))
    print(post_order(tree, 0))


if __name__ == '__main__':
    main()
    #test()