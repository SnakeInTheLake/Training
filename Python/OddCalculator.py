from sys import stdin
import math

def operations(num):
    arr = [math.inf for _ in range(num + 1)]
    arr[1] = 0
    for i in range(1, num):
        if i * 3 <= num:
            arr[i * 3] = min(arr[i * 3], arr[i] + 1)
        if i * 2 <= num:
            arr[i * 2] = min(arr[i * 2], arr[i] + 1)
        if i + 1 <= num:
            arr[i + 1] = min(arr[i + 1], arr[i] + 1)
    return arr

def recovery(num, arr):
    ans = [num]
    i = num
    while i > 1:
        if arr[i] == arr[i-1] + 1:
            ans.append(i - 1)
            i -= 1
        elif i % 2 == 0 and arr[i] == arr[i//2] + 1:
            ans.append(i // 2)
            i = i // 2
        else:
            ans.append(i // 3)
            i = i // 3
    return ans


def main():
    num = int(stdin.readline())
    arr = operations(num)
    ans = recovery(num, arr)
    print(arr[-1])
    print(*reversed(ans))


def test():
    num = 1
    arr = operations(num)
    ans = recovery(num, arr)
    print(arr[-1])

    print(*reversed(ans))

if __name__ == '__main__':
    #main()
    test()