from system import System
from vector import Vector, Particle
from trajectory_data import *
import unittest


class KnownOutput(unittest.TestCase):
    particles = [
        Particle(
            config3['particles'][key]['p_0'],
            config3['particles'][key]['v_0'],
            config3['particles'][key]['m'],
            config3['particles'][key]['color']
        )
        for key in config3['particles']
    ]
    system = System(particles, config3['gravity'], config3['time_step'])
    known_positions_after_increment = [
        [-0.0015, 0.0],
        [0.8993234673545738, 199.98309786422152],
        [199.9831906165297, -0.9001291296683563],
        [-0.9003841275263537, -199.98309786422152],
        [-199.9835656165297, 0.9001291296683563],
        [-399.39859591833886, 499.39815738505627],
        [399.6985971950403, -499.84828651472463]
    ]
    known_positions_after_increment = [
        Vector(coords) for coords in known_positions_after_increment]
    known_pairs = [
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (0, 5),
        (0, 6),
        (1, 2),
        (1, 3),
        (1, 4),
        (1, 5),
        (1, 6),
        (2, 3),
        (2, 4),
        (2, 5),
        (2, 6),
        (3, 4),
        (3, 5),
        (3, 6),
        (4, 5),
        (4, 6),
        (5, 6),
    ]

    def test_get_pairs(self):
        pairs = self.system.get_pairs()
        pairs = [(self.system.particles.index(part1), self.system.particles.index(part2))
                 for (part1, part2) in pairs]
        self.assertEqual(pairs, self.known_pairs)

    def test_positions_after_increment(self):
        self.system.increment()
        self.assertEqual(self.system.particles,
                         self.known_positions_after_increment)


if __name__ == '__main__':
    unittest.main(verbosity=2)
