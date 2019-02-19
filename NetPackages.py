from collections import deque
from sys import stdin


def processing(size, num_of_packages, time_of_arrival, processing_time):
    q = deque(maxlen=size)
    ans = []
    for i in range(num_of_packages):
        if len(q) == 0:
            q.append(time_of_arrival[i] + processing_time[i])
            ans.append(time_of_arrival[i])

        elif len(q) in range(1, size):
            if time_of_arrival[i] < q[-1]:
                ans.append(q[-1])
                q.append(q[-1] + processing_time[i])
            else:
                ans.append(time_of_arrival[i])
                q.append(time_of_arrival[i] + processing_time[i])

        elif len(q) == size:
            if time_of_arrival[i] >= q[-1]:
                ans.append(time_of_arrival[i])
                q.append(time_of_arrival[i] + processing_time[i])
            elif time_of_arrival[i] in range(q[0], q[-1]):
                ans.append(q[-1])
                q.append(q[-1] + processing_time[i])
            else:
                ans.append(-1)
    return ans


def main():
    time_of_arrival, processing_time = [], []
    size, num_of_packages = map(int, stdin.readline().split())
    for _ in range(num_of_packages):
        t, p = map(int, stdin.readline().split())
        time_of_arrival.append(t)
        processing_time.append(p)
    print(*processing(size, num_of_packages, time_of_arrival, processing_time), sep='\n')


def test():
    time_of_arrival, processing_time = [], []
    with open('1.txt', 'r') as inp:
        size, num_of_packages = map(int, inp.readline().strip().split())
        for line in inp:
            t, p = map(int, line.strip().split())
            time_of_arrival.append(t)
            processing_time.append(p)

    print(processing(size, num_of_packages, time_of_arrival, processing_time))


if __name__ == '__main__':
    #main()
    test()