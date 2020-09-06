from collections import deque
from sys import stdin

def moving_max(arr_length, arr, window_size):
    if window_size == 1:
        return arr
    ans = deque()
    sup1 = deque()
    sup2 = deque(maxlen=window_size)
    sup3 = deque()
    left, right = 0, window_size
    while left < arr_length:
        for i in range(left, right):
            if not sup1 or i == left:
                sup1.append(arr[i])
            elif arr[i] > sup1[-1]:
                sup1.append(arr[i])
            else:
                sup1.append(sup1[i-1])

        for j in reversed(range(left, right)):
            if not sup2 or j == right - 1 :
                sup2.appendleft(arr[j])
            elif arr[j] > sup2[0]:
                sup2.appendleft(arr[j])
            else:
                sup2.appendleft(sup2[0])
        sup3.extend(sup2)
        sup2.clear()
        if (right + window_size) >= arr_length:
            left, right = right, arr_length
        else:
            left, right = right, right + window_size

    left, right = 0, window_size - 1
    while right < arr_length:
        ans.append(max(sup1[right], sup3[left]))
        left += 1
        right += 1
    return ans


def main():
    arr_length = int(stdin.readline())
    arr = deque(map(int, stdin.readline().split()))
    window_size = int(stdin.readline())
    print(*moving_max(arr_length, arr, window_size))

def test():
    arr_length = 8
    #arr = deque([[2, 2], [7, 7], [3, 7], [1, 7], [5, 7], [2, 7], [6, 7], [2, 7]])
    arr = deque([2, 7, 3, 1, 5, 2, 6, 2])
    window_size = 4
    # ans = moving_max(arr_length, arr, window_size)
    # print(' '.join(ans))
    print(*moving_max(arr_length, arr, window_size))


if __name__ == '__main__':
    main()
    #test()