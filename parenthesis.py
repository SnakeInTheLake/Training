def check(s):
    symbols = []
    sup = []
    index = 1
    for ch in s:
        if ch == '(' or ch == '[' or ch == '{':
            symbols.append(ch)
            sup.append(index)
        elif (ch == ')' or ch == ']' or ch == '}') and len(symbols) == 0:
            return index
        elif ((ch == ')' and symbols[-1] == '(')
              or (ch == ']' and symbols[-1] == '[')
              or (ch == '}' and symbols[-1] == '{')):
            symbols.pop()
            sup.pop()
        elif ((ch == ')' and symbols[-1] != '(')
              or (ch == ']' and symbols[-1] != '[')
              or (ch == '}' and symbols[-1] != '{')):
            return index
        # print(symbols)
        index += 1
    if not symbols:
       return 'Success'
    else:
        return sup[-1]


def main():
    s = input()
    print(check(s))

def test():
    #s = '{[]}()'
    #s = ']{{[()]]'
    #s = '[foo(bar)]'
    #s = 'foo(bar[i)'
    # print(check(s))
    assert check("([](){([])})") == 'Success'
    assert check("()[]}") == 5
    assert check("{{[()]]") == 7
    assert check("{{{[][][]") == 3
    assert check("{*{{}") == 3
    assert check("[[*") == 2
    assert check("{*}") == 'Success'
    assert check("{{") == 2
    assert check("{}") == 'Success'
    assert check("") == 'Success'
    assert check("}") == 1
    assert check("*{}") == 'Success'
    assert check("{{{**[][][]") == 3

if __name__ == '__main__':
    #main()
    test()