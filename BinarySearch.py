def search(arr: list, num):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return mid + 1
        elif arr[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def main():
    arr = list(map(int, input().split()))[1:]
    to_find = list(map(int, input().split()))[1:]
    for num in to_find:
        print(search(arr, num), end=' ')


if __name__ == '__main__':
    main()