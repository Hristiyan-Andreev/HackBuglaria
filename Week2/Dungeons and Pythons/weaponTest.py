from weapon import Weapon
import unittest


class TestWeapon(unittest.TestCase):

    def test_Weapon_init(self):
        my_weapon = Weapon("Axe", 31, 0.2)
        self.assertEqual(my_weapon.typeW, "Axe")
        self.assertEqual(my_weapon.damage, 31)
        self.assertEqual(my_weapon.critical_strike_percent, 0.2)

    def test_Weapon_init_less(self):
        my_weapon = Weapon("Axe", 31, -1)
        self.assertEqual(my_weapon.typeW, "Axe")
        self.assertEqual(my_weapon.damage, 31)
        self.assertEqual(my_weapon.critical_strike_percent, 0)

    def test_Weapon_init_more(self):
        my_weapon = Weapon("Axe", 31, 3)
        self.assertEqual(my_weapon.typeW, "Axe")
        self.assertEqual(my_weapon.damage, 31)
        self.assertEqual(my_weapon.critical_strike_percent, 1)

    def test_Weapon_critical_hit(self):
        my_weapon = Weapon("Axe", 31, 1)
        self.assertTrue(my_weapon.critical_hit())

