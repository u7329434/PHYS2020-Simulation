#Ising Mode Simulation Animation

#Importing necessary packages
import numpy as np
import matplotlib.pyplot as plt
from numpy import random
from matplotlib.animation import FuncAnimation

#Setting up Parameters
#Size of Lattice (size x size)
size = 100
#Temperature (epsilon/k)
T = 2.25
#Energy of neighboring dipoles, energy = -e when parallel and +e when anti-parallel
e = 1
#Boltzmann Constant (Don't actually use but is there in case I do use it)
k = 1.38*10**(-23)

#Initial lattice with each dipole randomly either having spin up or down
lattice = np.random.choice([1, -1], size = (size, size))

#Defining Delta U, returns U when the dipole is flipped - U when the dipole is not flipped
def delta_U(i, j):
    center = lattice[i, j]
    center_changed = -lattice[i, j]
    below = lattice[i, (j - 1) % size]
    above = lattice[i, (j + 1) % size]
    left = lattice[(i - 1) % size, j]
    right = lattice[(i + 1) % size, j]
    #not_changed_U = -e*(center*below + center*above + center*left + center*right)
    #changed_U = -e*(center_changed*below + center_changed*above + center_changed*left + center_changed*right)
    e_diff = 2*center*(above + below + left + right)
    return e_diff

#If delta U > 0 we flip the dipole with the following probability
def prob_of_flipping(i, j):
    probability = np.exp(-delta_U(i, j)/T)
    return probability

#Metropolis Algorithm
def metropolis_algorithm(lattice, steps, interval):
    for n1 in range(steps):
        for n2 in range(interval):
            i = random.randint(size)
            j = random.randint(size)
            e_diff = delta_U(i, j)
            if e_diff > 0:
                m = random.rand()
                if m < prob_of_flipping(i, j):
                    lattice[i, j] = -1*lattice[i, j]
            else:
                lattice[i, j] = -1*lattice[i, j]
        yield lattice.copy()

def show_lattice(lattice):
    plt.imshow(lattice, cmap = 'gray', vmin = -1, vmax = 1)
    plt.axis('off')
    plt.show()

# Animation
fig, ax = plt.subplots()
img = ax.imshow(lattice, cmap='gray', vmin=-1, vmax=1)
ax.axis('off')

def update(frame):
    img.set_data(frame)
    return [img]

frames = list(metropolis_algorithm(lattice, steps=200, interval=1000))
ani = FuncAnimation(fig, update, frames=frames, blit=True, repeat=False)
ani.save("ising_animation.mp4", fps=30, dpi=200)
plt.show()
