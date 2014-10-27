from hero import Hero
from orc import Orc
from weapon import Weapon
from fighting import Fight

import unittest


class TestFight(unittest.TestCase):

    def test_init(self):
        my_Hero = Hero("Ivan", 100, "bad ass")
        my_Orc = Orc("Boko", 100, 1.5)
        fight1 = Fight(my_Hero, my_Orc)
        self.assertEqual(fight1.Hero.name, "Ivan")
        self.assertEqual(fight1.Orc.name, "Boko")

    def test_fight(self):
        my_Hero = Hero("Ivan", 100, "bad ass")
        my_Orc = Orc("Boko", 100, 1.5)
        my_weapon1 = Weapon("Axe1", 31, 0.2)
        my_weapon2 = Weapon("Axe2", 31, 0.2)
        my_Hero.equip_weapon(my_weapon1)
        my_Orc.equip_weapon(my_weapon2)
        fight1 = Fight(my_Hero, my_Orc)
        fight1.simulate_fight()
        self.assertFalse(my_Orc.is_alive() and my_Hero.is_alive())

if __name__ == '__main__':
    unittest.main()
