from sys import stdin


def find(i):
    while i != parents[i]:
        i = parents[i]
    return i


def union(xs, ys, sizes):
    global parents
    parents = [i for i in range(len(sizes))]
    ans = []
    m = max(sizes)
    for i in range(len(xs)):
        x, y = find(xs[i]), find(ys[i])
        if x == y:
            ans.append(m)
        else:
            if sizes[x] > sizes[y]:
                parents[y] = x
                sizes[x] += sizes[y]
                if sizes[x] > m:
                    m = sizes[x]
            else:
                parents[x] = y
                sizes[y] += sizes[x]
                if sizes[y] > m:
                    m = sizes[y]

            ans.append(m)
    return ans


def main():
    tables, requests = map(int, stdin.readline().split())
    sizes = list(map(int, stdin.readline().split()))
    xs, ys = [], []
    for _ in range(requests):
        x, y = map(int, stdin.readline().split())
        xs.append(x - 1)
        ys.append(y - 1)
    print(*union(xs, ys, sizes), sep='\n')


def test():
    tables = 5
    requests = 5
    sizes = [1, 1, 1, 1, 1]
    #sizes = [10, 0, 5, 0, 3, 3]
    xs = [2, 1, 0, 4, 4]
    #xs = [5, 5, 4, 3]
    ys = [4, 3, 3, 3, 2]
    #ys = [5, 4, 3, 2]
    print(*union(xs, ys, sizes), sep='\n')

if __name__ == '__main__':
    #main()
    test()