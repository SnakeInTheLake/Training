def finder(seg: list):
    row = 0
    while row < len(seg) - 1:
        if max(seg[row]) >= min(seg[row + 1]):
            seg[row] = [max(min(seg[row]), min(seg[row + 1])),
                                 min(max(seg[row]), max(seg[row + 1]))]
            segments.remove(seg[row + 1])
        else:
            row += 1
    return seg


n = int(input()) # Number of segments
segments = []
for i in range(n):
    start, finish = map(int, input().split())
    segments.append([start, finish])

segments.sort()

ans = finder(segments)
print(len(ans))
for row in ans:
    print(row[0], end=' ')
