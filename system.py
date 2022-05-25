import itertools


class System():
    def __init__(self, particles, grav_const, time_step):
        # A list of Particle objects
        self.particles = particles
        self.pairs = self.get_pairs()
        self.grav_const = grav_const
        # Convert milliseconds to seconds
        self.time_step = time_step / 1e3

    def get_pairs(self):
        try:
            return self.pairs
        except:
            return list(itertools.combinations(self.particles, 2))

    def increment(self):
        for pair in self.pairs:
            pair[0].apply_forces(pair[1], self.grav_const)
        for particle in self.particles:
            particle.increment(self.time_step)
