import random
import bisect
from sys import stdin, stdout


def seg_counter(left, right, dots):
    left.sort()
    right.sort()
    for dot in dots:
        l = bisect.bisect_right(left, dot)
        r = bisect.bisect_left(right, dot)
        stdout.write(str(l - r) + ' ')


def main():
    n, m = map(int, stdin.readline().split())
    left, right = [], []
    for i in range(n):
        begin, end = map(int, stdin.readline().split())
        left.append(begin)
        right.append(end)
    dots = list(map(int, stdin.readline().split()))
    print(dots)
    seg_counter(left, right, dots)


def test():
    left = [-2, 0, -1, -1, 0, -2, 1, 2, 1, 2]
    right = [3, 3, 0, 3, 1, -1, 3, 3, 2, 3]
    dots = [-3, -1, 0, 2, 3]
    seg_counter(left, right, dots)
    # left = [random.randint(0, 10**4) for _ in range(50000)]
    # right = [random.randint(10**4 + 1, 10**8) for _ in range(50000)]
    # dots = [random.randint(0, 10**8) for _ in range(random.randint(0, 50000))]
    # seg_counter(left, right, dots)


if __name__ == '__main__':
    test()
    #main()

