import random


class Fight:

    def __init__(self, hero, orc):
        self.Hero = hero
        self.Orc = orc
        self.coin = random.random()

    def simulate_fight(self):
        if self.coin < 50:
            self.fight(self.Orc, self.Hero)
        self.fight(self.Hero, self.Orc)

    def fight(self, first, second):
        if not (self.Hero.is_alive() and self.Orc.is_alive()):
            if first.health == 0:
                "{} has won the battle!".format(second.name)
            else:
                "{} has won the battle!".format()
            return
        else:
            second.take_damage(first.attack())
            "{} was hit for {} damage by {} and is now on {} health".format(second.name,
                first.attack(), second.name, second.health)
            self.fight(second, first)
