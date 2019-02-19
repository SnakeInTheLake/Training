import sys, numpy as np


def max_carry(capacity, number_of_items, weights):
    table = np.zeros((number_of_items + 1, capacity + 1), dtype=int)
    for i in range(1, number_of_items + 1):
        for w in range(1, capacity + 1):
            table[i, w] = table[i-1, w]
            if weights[i-1] <= w:
                table[i, w] = max(table[i, w], table[i-1, w - weights[i-1]] + weights[i-1])
    return table[-1, -1]


def main():
    capacity, number_of_items = map(int, sys.stdin.readline().split())
    weights = list(map(int, sys.stdin.readline().split()))
    print(max_carry(capacity, number_of_items, weights))


def test():
    capacity = 10
    number_of_items = 3
    weights = [1, 4 ,8]
    print(max_carry(capacity, number_of_items, weights))


if __name__ == '__main__':
    main()
    #test()