import heapq
from sys import stdin


def process(processors, times):
    q, ans = [], []
    heapq.heapify(q)
    i = 0
    while i < processors and times:
        for el in times:
            if el == 0:
                ans.append([str(i), str(0)])
                times.remove(el)
                break
            else:
                heapq.heappush(q, [el, i])
                times.remove(el)
                ans.append([str(i), str(0)])
                i += 1
                break
        if not q and not times:
            return ans


    for el in times:
        t = heapq.heappop(q)
        heapq.heappush(q, [el + t[0], t[1]])
        ans.append([str(t[1]), str(t[0])])
    return ans




def main():
    processors, tasks = map(int, stdin.readline().split())
    times = list(map(int, stdin.readline().split()))
    ans = process(processors, times)
    print('\n'.join(map(' '.join, ans)))

def test():
    processors = 2
    #processors = 4
    tasks = 5
    times = [1, 2, 3, 4, 5]
    times = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    times = [0, 0, 1, 0, 0, 0, 2, 1, 2, 3, 0, 0, 0, 2, 1]
    times = [0,0,0,0,1]
    ans = process(processors, times)
    print('\n'.join(map(' '.join, ans)))

if __name__ == '__main__':
    main()
    #test()