def hashing(string):
    code = 0
    for ch in string:
        code += ord(ch)
    return code


def main():
    sub = input()
    string = input()

    chs = []
    for ch in string:
        chs.append(ord(ch))

    left = len(string) - len(sub) - 1
    right = len(string) - 2

    sub_hash = hashing(sub)
    right_hash = hashing(string[left + 1:])

    ans = [[right_hash, left + 1, ]]
    while left >= 0:
        h = right_hash - chs[right + 1] + chs[left]
        ans.append([h, left])
        left -= 1
        right -= 1
        right_hash = h
    print(ans)
    print(sub_hash)

    for el in reversed(ans):
        if el[0] == sub_hash and sub == string[el[1] : el[1] + len(sub)]:
            print(el[1], end=' ')


def test():
    sub = 'Test'
    string = 'testTesttesT'

    chs = []
    for ch in string:
        chs.append(ord(ch))

    left = len(string) - len(sub) - 1
    right = len(string) - 2

    sub_hash = hashing(sub)
    right_hash = hashing(string[left + 1:])

    ans = [[right_hash, left + 1,]]
    while left >= 0:
        h = right_hash - chs[right + 1] + chs[left]
        ans.append([h, left])
        left -= 1
        right -= 1
        right_hash = h
    print(ans)
    print(sub_hash)

    for el in reversed(ans):
        if el[0] == sub_hash and sub[0] == string[el[1]]:
            print(el[1], end=' ')


if __name__ == '__main__':
    #main()
    test()