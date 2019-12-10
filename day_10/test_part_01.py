import unittest
from part_01 import run, parse, get_count


class Part01Tests(unittest.TestCase):

    def test_simple_example(self):
        asteroids = [
            '..#',
            '...',
            '..#',
            '..#'
        ]

        asteroids = parse(asteroids)
        count = get_count(2, 0, asteroids)

        self.assertEqual(count, 1)

    def test_first_example(self):
        asteroids = [
            '.#..#',
            '.....',
            '#####',
            '....#',
            '...##'
        ]

        asteroids = parse(asteroids)
        coords, detect = run(asteroids)

        self.assertEqual(coords, '3,4')
        self.assertEqual(detect, 8)

    def test_second_example(self):
        asteroids = [
            '......#.#.',
            '#..#.#....',
            '..#######.',
            '.#.#.###..',
            '.#..#.....',
            '..#....#.#',
            '#..#....#.',
            '.##.#..###',
            '##...#..#.',
            '.#....####'
        ]

        asteroids = parse(asteroids)
        coords, detect = run(asteroids)

        self.assertEqual(coords, '5,8')
        self.assertEqual(detect, 33)

    def test_third_example(self):
        asteroids = [
            '#.#...#.#.',
            '.###....#.',
            '.#....#...',
            '##.#.#.#.#',
            '....#.#.#.',
            '.##..###.#',
            '..#...##..',
            '..##....##',
            '......#...',
            '.####.###.'
        ]

        asteroids = parse(asteroids)
        coords, detect = run(asteroids)

        self.assertEqual(coords, '1,2')
        self.assertEqual(detect, 35)
