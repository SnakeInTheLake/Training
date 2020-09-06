def hashing(string, size):
    x, p = 263, 1_000_000_007
    sup = []
    code = 0
    for ch in string:
        sup.append(ord(ch))
    for i in range(len(sup)):
        code += sup[i] * x**i
    code %= p
    code %= size
    return code

def add(table, string, code):
    if table[code] is None:
        table[code] = [string]
    elif string not in table[code]:
        table[code].insert(0, string)
    return table

def find(table, string, code):
    if table[code] is not None and string in table[code]:
        return 'yes'
    return 'no'


def delete(table, string, code):
    if table[code] is not None and string in table[code]:
        table[code].remove(string)
    return table


def check(table, ind):
    if table[ind] is None:
        return ''
    return table[ind]


def main():
    size = int(input())
    table = [None] * size
    reqs = int(input())
    for _ in range(reqs):
        line = input()
        if line.startswith('add'):
            _, string = line.strip().split()
            code = hashing(string, size)
            add(table, string, code)

        if line.startswith('find'):
            _, string = line.strip().split()
            code = hashing(string, size)
            print(find(table, string, code))

        if line.startswith('del'):
            _, string = line.strip().split()
            code = hashing(string, size)
            delete(table, string, code)

        if line.startswith('check'):
            _, ind = line.strip().split()
            print(*check(table, int(ind)))


def test():
    with open('1.txt', 'r') as inp:
        size = int(inp.readline().strip())
        table = [None] * size
        reqs = int(inp.readline().strip())
        for line in inp:
            if line.startswith('add'):
                _, string = line.strip().split()
                code = hashing(string, size)
                add(table, string, code)

            if line.startswith('find'):
                _, string = line.strip().split()
                code = hashing(string, size)
                print(find(table, string, code))

            if line.startswith('del'):
                _, string = line.strip().split()
                code = hashing(string, size)
                delete(table, string, code)

            if line.startswith('check'):
                _, ind = line.strip().split()
                print(*check(table, int(ind)))



if __name__ == '__main__':
    main()
    #test()