import unittest
from part_01 import parse
from part_02 import run


class Part02Tests(unittest.TestCase):

    def test_example(self):
        asteroids = [
            '.#..##.###...#######',
            '##.############..##.',
            '.#.######.########.#',
            '.###.#######.####.#.',
            '#####.##.#.##.###.##',
            '..#####..#.#########',
            '####################',
            '#.####....###.#.#.##',
            '##.#################',
            '#####.##.###..####..',
            '..######..##.#######',
            '####.##.####...##..#',
            '.#####..#.######.###',
            '##...#.##########...',
            '#.##########.#######',
            '.####.#.###.###.#.##',
            '....##.##.###..#####',
            '.#.#.###########.###',
            '#.#.#.#####.####.###',
            '###.##.####.##.#..##'
        ]

        asteroids = parse(asteroids)
        x, y = 11, 13
        angles = run(asteroids, x, y)

        self.assertEqual(angles[0], '11,12')
        self.assertEqual(angles[1], '12,1')
        self.assertEqual(angles[2], '12,2')
        self.assertEqual(angles[9], '12,8')
        self.assertEqual(angles[19], '16,0')
        self.assertEqual(angles[49], '16,9')
        self.assertEqual(angles[99], '10,16')
        self.assertEqual(angles[198], '9,6')
        self.assertEqual(angles[199], '8,2')
        self.assertEqual(angles[200], '10,9')
        self.assertEqual(angles[298], '11,1')
