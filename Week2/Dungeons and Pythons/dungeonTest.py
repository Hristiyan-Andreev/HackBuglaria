from dungeon import Dungeon
from hero import Hero
from orc import Orc
from weapon import Weapon
import unittest


class DungeonTesting(unittest.TestCase):

    def test_dungeon_map(self):
        dungeon1 = Dungeon("dungeon.txt")
        dungeonmap = "S.##......\n#.##..###.\n#.###.###.\n#.....###.\n###.#####S\n"
        self.assertEqual(dungeon1.print_map(), dungeonmap)

    def test_spawn(self):
        dungeon1 = Dungeon("dungeon.txt")
        my_Hero = Hero("Ivan", 100, "bad ass")
        my_Orc = Orc("Boko", 100, 1.5)
        dungeon1.spawn("Harabeisho", my_Hero)

if __name__ == '__main__':
    unittest.main()
