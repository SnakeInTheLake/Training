def components(number: int):
    comps = []
    item = 1
    while number > 0:
        comps.append(item)
        number -= item
        item += 1
        if item > number:
            comps.append(comps.pop() + number)
            break
    return comps

def main():
    n = int(input())
    ans = components(n)
    print(len(ans))
    print(*ans)

if __name__ == '__main__':
    main()

