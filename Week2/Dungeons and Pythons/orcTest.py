from orc import Orc
from weapon import Weapon
import unittest


class TestOrc(unittest.TestCase):

    def test_Orc_init(self):
        my_Orc = Orc("Ivan", 100, 1.5)
        self.assertEqual(my_Orc.name, "Ivan")
        self.assertEqual(my_Orc.health, 100)
        self.assertEqual(my_Orc.berserk_factor, 1.5)

    def test_Orc_init_less(self):
        my_Orc = Orc("Ivan", 100, 0.5)
        self.assertEqual(my_Orc.name, "Ivan")
        self.assertEqual(my_Orc.health, 100)
        self.assertEqual(my_Orc.berserk_factor, 1)

    def test_Orc_init_(self):
        my_Orc = Orc("Ivan", 100, 3)
        self.assertEqual(my_Orc.name, "Ivan")
        self.assertEqual(my_Orc.health, 100)
        self.assertEqual(my_Orc.berserk_factor, 2)

    def test_Orc_get_health(self):
        my_Orc = Orc("Ivan", 100, 1.5)
        self.assertEqual(my_Orc.get_health(), 100)

    def test_Orc_is_alive(self):
        my_Orc = Orc("Ivan", 100, 1.5)
        self.assertTrue(my_Orc.is_alive())

    def test_Orc_is_alive_dead(self):
        my_Orc = Orc("Ivan", 100, 1.5)
        my_Orc.health = 0
        self.assertFalse(my_Orc.is_alive())

    def test_Orc_take_damage(self):
        my_Orc = Orc("Ivan", 100, 1.5)
        my_Orc.take_damage(50)
        self.assertEqual(my_Orc.get_health(), 50)

    def test_Orc_take_damage_float(self):
        my_Orc = Orc("Ivan", 100, 1.5)
        my_Orc.take_damage(50.5)
        self.assertEqual(my_Orc.get_health(), 49.5)

    def test_Orc_take_healing(self):
        my_Orc = Orc("Ivan", 100, 1.5)
        my_Orc.health = 50
        my_Orc.take_healing(30)
        self.assertEqual(my_Orc.get_health(), 80)

    def test_Orc_take_healing_dead(self):
        my_Orc = Orc("Ivan", 100, 1.5)
        my_Orc.health = 0
        self.assertFalse(my_Orc.take_healing(30))
        self.assertEqual(my_Orc.get_health(), 0)

    def test_Orc_take_healing_maxhealing(self):
        my_Orc = Orc("Ivan", 100, 1.5)
        my_Orc.health = 100
        my_Orc.take_healing(10)
        self.assertEqual(my_Orc.get_health(), 100)

    def test_Orc_attack_with_weapon(self):
        my_weapon = Weapon("Axe", 31, 0.2)
        my_Orc = Orc("Ivan", 100, 1.5)
        my_Orc.equip_weapon(my_weapon)
        attack = my_weapon.damage * (1 + my_weapon.critical_strike_percent) * my_Orc.berserk_factor
        true_attack = my_Orc.attack()
        self.assertEqual(attack, true_attack)

    def test_Orc_attack_no_weapon(self):
        my_Orc = Orc("Ivan", 100, 1.5)
        attack = 0
        true_attack = my_Orc.attack()
        self.assertEqual(attack, true_attack)

if __name__ == '__main__':
    unittest.main()
