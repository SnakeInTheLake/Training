def fib(n):  # Fibonacci number
    lst = [0, 1]
    for i in range(2, n+1):
        lst.append((lst[i-1] + lst[i-2]) % 5)
        print(lst)
    return lst[n]


def fib_digit(n):  # Last digit of Fibonacci number
    lst = [0, 1]
    for i in range(2, n+1):
        lst.append((lst[i-1] + lst[i-2]) % 10)
    return lst[n]


def pisano(m):  # Pisano period for the divider
    lst = [0, 1]
    i = 2
    if m == 1:
        return [0]
    else:
        while True:
            lst.append((lst[i-1] + lst[i-2]) % m)
            if lst[i] == 1 and lst[i-1] == 0:
                lst = lst[:-2]
                break
            else:
                i += 1
        return lst


def fib_mod(n, m):  # Remainder for n-Fibonacci number division by m
    period = pisano(m)
    if n < len(period):
        return period[n]
    else:
        return period[n % len(period)]


def main():
    n, m = map(int, input().split())
    print(fib(n))
    print(fib_digit(n))
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()