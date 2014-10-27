from hero import Hero
import unittest


class TestHero(unittest.TestCase):

    def test_Hero_init(self):
        my_Hero = Hero("Ivan", 100, "bad ass")
        self.assertEqual(my_Hero.name, "Ivan")
        self.assertEqual(my_Hero.health, 100)
        self.assertEqual(my_Hero.nickname, "bad ass")

    def test_Hero_known_as(self):
        my_Hero = Hero("Ivan", 100, "bad ass")
        self.assertEqual(my_Hero.known_as(), "Ivan the bad ass")

    def test_hero_get_health(self):
        my_Hero = Hero("Ivan", 100, "bad ass")
        self.assertEqual(my_Hero.get_health(), 100)

    def test_Hero_is_alive(self):
        my_Hero = Hero("Ivan", 100, "bad ass")
        self.assertTrue(my_Hero.is_alive())

    def test_Hero_is_alive_dead(self):
        my_Hero = Hero("Ivan", 100, "bad ass")
        my_Hero.health = 0
        self.assertFalse(my_Hero.is_alive())

    def test_Hero_take_damage(self):
        my_Hero = Hero("Ivan", 100, "bad ass")
        my_Hero.take_damage(50)
        self.assertEqual(my_Hero.get_health(), 50)

    def test_Hero_take_damage_float(self):
        my_Hero = Hero("Ivan", 100, "bad ass")
        my_Hero.take_damage(50.5)
        self.assertEqual(my_Hero.get_health(), 49.5)

    def test_Hero_take_healing(self):
        my_Hero = Hero("Ivan", 100, "bad ass")
        my_Hero.health = 50
        my_Hero.take_healing(30)
        self.assertEqual(my_Hero.get_health(), 80)

    def test_Hero_take_healing_dead(self):
        my_Hero = Hero("Ivan", 100, "bad ass")
        my_Hero.health = 0
        self.assertFalse(my_Hero.take_healing(30))
        self.assertEqual(my_Hero.get_health(), 0)

    def test_Hero_take_healing_maxhealing(self):
        my_Hero = Hero("Ivan", 100, "bad ass")
        my_Hero.health = 100
        my_Hero.take_healing(10)
        self.assertEqual(my_Hero.get_health(), 100)

if __name__ == '__main__':
    unittest.main()
