def decode(code: dict, encoded: str):
    decoded = ''
    while encoded:
        for key in code:
            if encoded.startswith(key):
                decoded += code[key]
                encoded = encoded[len(key):]
    return decoded


def main():
    n, length = map(int, input().split())
    d = {}
    for i in range(n):
        codes = input().strip()
        d[codes[3:]] = codes[:1]
    s = input()
    print(decode(d, s))


if __name__ == '__main__':
    main()