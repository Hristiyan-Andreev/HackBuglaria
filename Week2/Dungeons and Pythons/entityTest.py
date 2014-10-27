from entity import Entity
from weapon import Weapon
import unittest


class TestEntity(unittest.TestCase):

    def test_Entity_init(self):
        my_Entity = Entity("Ivan", 100)
        self.assertEqual(my_Entity.name, "Ivan")
        self.assertEqual(my_Entity.health, 100)

    def test_hero_get_health(self):
        my_Entity = Entity("Ivan", 100)
        self.assertEqual(my_Entity.get_health(), 100)

    def test_Entity_is_alive(self):
        my_Entity = Entity("Ivan", 100)
        self.assertTrue(my_Entity.is_alive())

    def test_Entity_is_alive_dead(self):
        my_Entity = Entity("Ivan", 100)
        my_Entity.health = 0
        self.assertFalse(my_Entity.is_alive())

    def test_Entity_take_damage(self):
        my_Entity = Entity("Ivan", 100)
        my_Entity.take_damage(50)
        self.assertEqual(my_Entity.get_health(), 50)

    def test_Entity_take_damage_float(self):
        my_Entity = Entity("Ivan", 100)
        my_Entity.take_damage(50.5)
        self.assertEqual(my_Entity.get_health(), 49.5)

    def test_Entity_take_healing(self):
        my_Entity = Entity("Ivan", 100)
        my_Entity.health = 50
        my_Entity.take_healing(30)
        self.assertEqual(my_Entity.get_health(), 80)

    def test_Entity_take_healing_dead(self):
        my_Entity = Entity("Ivan", 100)
        my_Entity.health = 0
        self.assertFalse(my_Entity.take_healing(30))
        self.assertEqual(my_Entity.get_health(), 0)

    def test_Entity_take_healing_maxhealing(self):
        my_Entity = Entity("Ivan", 100)
        my_Entity.health = 100
        my_Entity.take_healing(10)
        self.assertEqual(my_Entity.get_health(), 100)

    def test_Entity_equip_weapon_no_weapon(self):
        my_weapon = Weapon("Axe", 31, 0.2)
        my_Entity = Entity("Ivan", 100)
        my_Entity.equip_weapon(my_weapon)
        self.assertEqual(my_Entity.weapon.type, "Axe")
        self.assertEqual(my_Entity.weapon.damage, 31)
        self.assertEqual(my_Entity.weapon.critical_strike_percent, 0.2)

    def test_Entity_has_weapon(self):
        my_weapon = Weapon("Axe", 31, 0.2)
        my_Entity = Entity("Ivan", 100)
        my_Entity.equip_weapon(my_weapon)
        self.assertTrue(my_Entity.has_weapon())

    def test_Entity_equip_weapon_with_weapon(self):
        my_weapon = Weapon("Axe", 31, 0.2)
        my_weapon2 = Weapon("Sword", 20, 0.5)
        my_Entity = Entity("Ivan", 100)
        my_Entity.equip_weapon(my_weapon)
        my_Entity.equip_weapon(my_weapon2)
        self.assertEqual(my_Entity.weapon.type, "Sword")
        self.assertEqual(my_Entity.weapon.damage, 20)
        self.assertEqual(my_Entity.weapon.critical_strike_percent, 0.5)

    def test_Entity_attack_with_weapon(self):
        my_weapon = Weapon("Axe", 31, 0.2)
        my_Entity = Entity("Ivan", 100)
        my_Entity.equip_weapon(my_weapon)
        attack = my_weapon.damage * (1 + my_weapon.critical_strike_percent)
        true_attack = my_Entity.attack()
        self.assertEqual(attack, true_attack)

    def test_Entity_attack_no_weapon(self):
        my_Entity = Entity("Ivan", 100)
        attack = 0
        true_attack = my_Entity.attack()
        self.assertEqual(attack, true_attack)

if __name__ == '__main__':
    unittest.main()
