class MoneyBox:
    def __init__(self, capacity):
        self.money = 0
        self.capacity = capacity

    def can_add(self, v):
        if v <= self.capacity - self.money:
            return True
        return False

    def add(self, v):
        if self.can_add(v):
            self.money += v

mon = MoneyBox(50)
print(mon.capacity)
print(mon.money)
print(mon.can_add(40))
mon.add(40)
print(mon.money)
print(mon.can_add(40))
mon.add(40)
print(mon.money)
