class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError
        else:
            super().append(x)

if __name__ == "__main__":
    lst = PositiveList([1, 2, 3, 4])
    lst.append(2)
    print(lst)
    try:
        lst.append(-1)
    except NonPositiveError:
        print('Whatever')
    print(lst)


