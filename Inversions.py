import random

def merge(arr1, arr2):
    merged = []
    global inv
    while arr1 and arr2:
        if arr1[0] > arr2[0]:
            inv += len(arr1)
            # print(inv)
            merged.append(arr2.pop(0))
        else:
            merged.append(arr1.pop(0))
    if not arr1:
        merged += arr2
    else:
        merged += arr1

    return merged


def mergesort(x):
    """ Function to sort an array using merge sort algorithm """
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x) // 2
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
        return merge(a, b)


def main():
    # n = int(input())
        # arr = list(map(int, input().split()))
    arr = [random.randint(0, 10**9) for _ in range(random.randint(0, 10**5))]
    # arr = [2, 3, 9, 2, 9]
    mergesort(arr)
    print(inv)


if __name__ == '__main__':
    inv = 0
    main()