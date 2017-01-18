import unittest
import sys
import os

sys.path.append(os.path.relpath("../"))
import poc_zombies as zombies


class ApocalypseClass(unittest.TestCase):

    def testInit1(self):
        obstacle_list = [(1, 2), (3, 4)]
        zombies_list = [(1, 3), (1, 4)]
        humans_list = [(3, 1), (3, 3)]
        game = zombies.Apocalypse(4, 5, obstacle_list, zombies_list, humans_list)
        game.add_zombie(1, 0)
        game.add_human(1, 4)
        self.assertEqual(game._zombie_list, [(1, 3), (1, 4), (1, 0)])
        self.assertEqual(game._human_list, [(3, 1), (3, 3), (1, 4)])
        game.clear()
        self.assertEqual(game._zombie_list, [])
        self.assertEqual(game._human_list, [])

    def testGenerator1(self):
        obstacle_list = [(1, 2), (3, 4)]
        zombies_list = [(1, 3), (1, 4)]
        humans_list = [(3, 1), (3, 3)]
        game = zombies.Apocalypse(4, 5, obstacle_list, zombies_list, humans_list)
        zombies_gen = []
        for zombie in game.zombies():
            zombies_gen.append(zombie)
        self.assertEqual(zombies_gen, zombies_list)
        humans_gen = []
        for human in game.humans():
            humans_gen.append(human)
        self.assertEqual(humans_gen, humans_list)

    def testGeneratorZombies1(self):
        obstacle_list = [(1, 2), (3, 4)]
        game = zombies.Apocalypse(4, 5, obstacle_list)
        zombies_gen = []
        game.add_zombie(1, 1)
        game.add_zombie(2, 3)
        for zombie in game.zombies():
            zombies_gen.append(zombie)
        self.assertEqual(zombies_gen, [(1, 1), (2, 3)])

    def testGeneratorZombies2(self):
        obstacle_list = [(1, 2), (3, 4)]
        game = zombies.Apocalypse(4, 5, obstacle_list)
        zombies_gen = []
        game.add_zombie(2, 3)
        game.add_zombie(1, 1)
        for zombie in game.zombies():
            zombies_gen.append(zombie)
        self.assertEqual(zombies_gen, [(2, 3), (1, 1)])

    def testDistanceField1(self):
        game = zombies.Apocalypse(4, 5)
        game.add_zombie(2, 3)
        game.add_zombie(1, 1)


    def testDistanceField2(self):
        game = zombies.Apocalypse(4, 5)
        game.add_zombie(1, 0)
        game.add_zombie(3, 4)
        field = game.compute_distance_field(7)
#        game.print_distance_field(field)

    def testDistanceField3(self):
        obstacle_list = [[2, 2]]
        game = zombies.Apocalypse(4, 5, obstacle_list)
        game.add_zombie(1, 0)
        field = game.compute_distance_field(7)
        self.assertEqual(field[2][2], 4 * 5)
        self.assertEqual(field[1][1], 1)
        self.assertEqual(field[1][2], 2)

    def testDistanceField4(self):
        obstacle_list = [[2, 2], [3, 4]]
        game = zombies.Apocalypse(5, 6, obstacle_list)
        game.add_zombie(1, 0)
        field = game.compute_distance_field(7)
        self.assertEqual(field[2][2], game.get_grid_height() * game.get_grid_width())
        self.assertEqual(field[3][4], game.get_grid_height() * game.get_grid_width())
        self.assertEqual(field[1][1], 1)
        self.assertEqual(field[1][2], 2)

    def testMoveHuman(self):
        game = zombies.Apocalypse(4, 5)
        game.add_zombie(1, 0)
        game.add_human(2, 1)
        game.move_humans(game.compute_distance_field(7))
        self.assertEqual(game._human_list, [(3, 2)])

    def testMoveHuman2(self):
        game = zombies.Apocalypse(4, 5)
        game.add_zombie(0, 0)
        game.add_human(0, 1)
        game.move_humans(game.compute_distance_field(7))
        self.assertEqual(game._human_list, [(1, 2)])

    def testMoveHuman3(self):
        game = zombies.Apocalypse(4, 5)
        game.add_zombie(3, 4)
        game.add_human(1, 1)
        game.move_humans(game.compute_distance_field(7))
        self.assertEqual(game._human_list, [(0, 0)])

    def testMoveHuman4(self):
        game = zombies.Apocalypse(4, 5)
        game.add_zombie(3, 4)
        game.add_human(0, 0)
        game.move_humans(game.compute_distance_field(7))
        self.assertEqual(game._human_list, [(0, 0)])

    def testMoveHuman5(self):
        game = zombies.Apocalypse(4, 5)
        game.add_zombie(0, 0)
        game.add_human(3, 4)
        game.move_humans(game.compute_distance_field(7))
        self.assertEqual(game._human_list, [(3, 4)])

    def testMoveHuman6(self):
        game = zombies.Apocalypse(4, 5)
        game.add_zombie(0, 0)
        game.add_human(3, 4)
        game.move_humans(game.compute_distance_field(7))
        game.move_humans(game.compute_distance_field(7))
        self.assertEqual(game._human_list, [(3, 4)])

    def testMoveHumanObstacle1(self):
        obstacle_list = [[2, 2]]
        game = zombies.Apocalypse(4, 5, obstacle_list)
        game.add_zombie(0, 0)
        game.add_human(1, 1)
        game.move_humans(game.compute_distance_field(7))
        self.assertEqual(game._human_list, [(2, 1)])

    def testMoveHumanObstacle2(self):
        obstacle_list = [[0, 1]]
        game = zombies.Apocalypse(1, 5, obstacle_list)
        game.add_zombie(0, 0)
        game.add_human(0, 2)
        game.move_humans(game.compute_distance_field(7))

    def testMoveHumanObstacle3(self):
        obstacle_list = [[2, 2], [2, 1], [1, 2]]
        game = zombies.Apocalypse(4, 4, obstacle_list)
        game.add_zombie(0, 0)
        game.add_human(1, 1)
        game.move_humans(game.compute_distance_field(7))
        self.assertEqual(game._human_list, [(1, 1)])

    def testMoveHumansTwice(self):
        game = zombies.Apocalypse(4, 5)
        game.add_zombie(3, 4)
        game.add_human(2, 2)
        game.move_humans(game.compute_distance_field(7))
        game.move_humans(game.compute_distance_field(7))
        self.assertEqual(game._human_list, [(0, 0)])

    def testMoveMultipleHumans(self):
        game = zombies.Apocalypse(4, 5)
        game.add_zombie(0, 0)
        game.add_human(0, 3)
        game.add_human(1, 2)
        game.move_humans(game.compute_distance_field(7))
        self.assertEqual(sorted(game._human_list), sorted([(2, 3), (1, 4)]))

    def testMoveZombie1(self):
        game = zombies.Apocalypse(4, 5)
        game.add_zombie(3, 4)
        game.add_human(1, 1)
        game.move_zombies(game.compute_distance_field(6))
        self.assertEqual(game._zombie_list, [(2, 4)])

    def testMoveZombie2(self):
        game = zombies.Apocalypse(4, 5)
        game.add_zombie(0, 0)
        game.add_human(1, 1)
        game.move_zombies(game.compute_distance_field(6))
        self.assertEqual(game._zombie_list, [(1, 0)])

    def testMoveZombieTwice(self):
        game = zombies.Apocalypse(4, 5)
        game.add_zombie(0, 0)
        game.add_human(1, 1)
        game.move_zombies(game.compute_distance_field(6))
        game.move_zombies(game.compute_distance_field(6))
        self.assertEqual(game._zombie_list, [(1, 1)])


def main():
    unittest.main()

if __name__ == '__main__':
    main()
