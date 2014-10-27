class Weapon:

    def __init__(self, typeW, damage, critical_strike_percent):
        self.type = typeW
        self.damage = damage
        if critical_strike_percent < 0:
            self.critical_strike_percent = 0
        elif critical_strike_percent > 1:
            self.critical_strike_percent = 1
        else:
            self.critical_strike_percent = critical_strike_percent

    def critical_hit(self):
        if self.damage * 2 == self.damage * (self.critical_strike_percent + 1):
            return True
        else:
            return False

