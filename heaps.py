import heapq


def main():
    n = int(input())
    instructions, numbers = [], []
    for i in range(n):
        instructions.append(input().split())
    print(instructions)
    for el in instructions:
        if el[0] == 'Insert':
            heapq.heappush(numbers, -int(el[1]))
            print(numbers)
        else:
            print(-heapq.heappop(numbers))


if __name__ == '__main__':
    main()
