from sys import stdin


def count_sort(original):
    counter = [0 for _ in range(max(original) + 1)]
    ans = [0 for _ in range(len(original))]

    for j in range(len(original)):
        counter[original[j]] += 1

    for i in range(1, max(original) + 1):
        counter[i] += counter[i - 1]

    for j in reversed(range(0, len(original))):
        ans[counter[original[j]] - 1] = original[j]
        counter[original[j]] -= 1

    return ans


def main():
    n = int(stdin.readline().strip())
    nums = list(map(int, stdin.readline().split()))
    print(*count_sort(nums))


def test():
    n = 5
    nums = [2, 3, 9, 2, 9]
    print(count_sort(nums))

if __name__ == '__main__':
    main()
    # test()