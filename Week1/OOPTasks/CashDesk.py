class CashDesk:

    def __init__(self):
        self.money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def take_money(self, amount):
        for value in amount:
            self.money[value] += amount[value]
        return

    def total(self):
        suma = 0
        for value in self.money:
            suma += self.money[value]
        return suma

    def can_withdraw_money(self, amount):
        if self.total() < amount:
            return False
        