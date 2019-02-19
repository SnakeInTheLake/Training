import sys, numpy as np


def diff(str1, ind1, str2, ind2):
    if str1[ind1] == str2[ind2]:
        return 0
    return 1


def distance(str1, str2):
    table = np.zeros((len(str2) + 1, len(str1) + 1), dtype=int)
    table[0, :] = np.linspace(0, len(str1), len(str1) + 1)
    table[:, 0] = np.linspace(0, len(str2), len(str2) + 1)
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            table[i, j] = min(table[i - 1, j] + 1,
                              table[i, j - 1] + 1,
                              table[i - 1, j - 1] + diff(str1, j - 1, str2, i - 1))
    return table[-1, -1]



def test():
    str1 = 'short'
    str2 = 'ports'
    print(distance(str1, str2))


def main():
    str1 = sys.stdin.readline()
    str2 = sys.stdin.readline()
    print(distance(str1, str2))

if __name__ == '__main__':
    main()
    #test()