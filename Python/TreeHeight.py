import sys


def tree_height(parents, root_index):
    depth = []
    add = -1
    for i in range(len(parents)):
        sup = []
        child  = i
        while parents[child] >= 0:
            sup.append(child)
            child = parents[child]
        for el in reversed(sup):
            parents[el] = parents[parents[el]] - 1
    return -min(parents)




def main():
    number_of_elements = int(sys.stdin.readline())
    parents = list(map(int, sys.stdin.readline().split()))
    root_index = parents.index(-1)
    print(tree_height(parents, root_index))


def test():
    number_of_elements = 10
    parents = [9, 7, 5, 5, 2, 9, 9, 9, 2, -1]
    #parents = [4, -1, 4, 1, 1]
    #parents = [-1, 0, 4, 0, 3]
    root_index = parents.index(-1)
    print(tree_height(parents, root_index))


if __name__ == '__main__':
    #main()
    test()