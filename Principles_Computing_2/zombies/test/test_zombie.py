import unittest
import sys
import os

sys.path.append(os.path.relpath("../"))
import poc_zombies as zombies


class ApocalypseClass(unittest.TestCase):

    def test1(self):
        game = zombies.Apocalypse(4, 5)
        print(game)
        self.assertEqual(1, 1)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
