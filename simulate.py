from vector import Particle
from system import System
from system_data import *
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')

# The configuration data, stored as dict in another file.
config = config3
time_step, gravity, extent, particles = config['time_step'], config[
    'gravity'], config['extent'], config['particles']
speed_mult = 2
window = ((-1 * extent, extent), (-1 * extent, extent))

system = System(
    [
        Particle(particles[key]['p_0'], particles[key]['v_0'], particles[key]['m'], particles[key]['color']) for key in config['particles']
    ],
    gravity,
    time_step
)

# A quick way to speed things up if a *boring* initial state was chosen.
for particle in system.particles:
    particle.velocity = particle.velocity.mult(speed_mult)

fig = plt.figure()
ax = plt.axes(xlim=window[0], ylim=window[1])
dots = [ax.plot(
    [],
    [],
    marker='o',
    markersize=particle.display_size,
    color=particle.color)[0] for particle in system.particles]
lines = [ax.plot(
    [],
    [],
    lw=0.5,
    color=particle.color)[0] for particle in system.particles]
# Beware the syntax coord_lists = [[[], []]] * len(system.particles) !  Modifying one of its subarrays modifies the others.
coord_lists = [[[] for i in range(2)] for i in range(len(system.particles))]


def animate(i=0):
    system.increment()
    for dot, particle in zip(dots, system.particles):
        dot.set_data(particle.position[0], particle.position[1])

    for index, line in enumerate(lines):
        coord_lists[index][0].append(
            system.particles[index].position[0])
        coord_lists[index][1].append(
            system.particles[index].position[1])
        line.set_data(coord_lists[index][0], coord_lists[index][1])

    return lines + dots


anim = FuncAnimation(fig, animate,
                     frames=200, interval=time_step, blit=True)

plt.show()
