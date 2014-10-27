from weapon import Weapon


class Entity:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = Weapon("", 0, 0)

    def get_health(self):
        return self.health

    def is_alive(self):
        if self.health == 0:
            return False
        return True

    def take_damage(self, damage):
        if self.health < damage:
            self.health = 0
        else:
            self.health -= damage

    def take_healing(self, healing):
        if self.health == 100:
            pass
        elif self.health == 0:
            return False
        else:
            self.health += healing
            return True

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def has_weapon(self):
        if self.weapon.type == "" and self.weapon.damage == 0:
            return False
        else:
            return True

    def attack(self):
        damage = self.weapon.damage * (1 + self.weapon.critical_strike_percent)
        return damage
