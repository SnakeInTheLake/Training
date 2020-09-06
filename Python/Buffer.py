class Buffer:
    def __init__(self):
        self.lst = []

    def add(self, *a):
        for arg in a:
            self.lst.append(arg)
        while len(self.lst) >= 5:
            print(sum(self.lst[:5]))
            del self.lst[:5]

    def get_current_part(self):
        return self.lst

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]