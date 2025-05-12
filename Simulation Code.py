#Ising Mode Simulation

#Importing necessary packages
import numpy as np
import matplotlib.pyplot as plt
from numpy import random

#Setting up Parameters
#Size of Lattice (size x size)
size = 20
#Temperature (K)         
T = 100
#Energy of neighboring dipoles, energy = -e when parallel and +e when parallel
e = 1
#Boltzmann Constant
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
    probability = np.power(e, -delta_U(i, j)/T)
    return probability

#Metropolis Algorithm
def metropolis_algorithm(lattice):
    for n in range(100*size*size):
        i = random.randint(size)
        j = random.randint(size)
        e_diff = delta_U(i, j)
        if e_diff > 0:
            m = random.rand()
            if m < prob_of_flipping(i, j):
                lattice[i, j] = -1*lattice[i, j]
        else:
            lattice[i, j] = -1*lattice[i, j]

def show_lattice(lattice):
    plt.imshow(lattice, cmap = 'gray', vmin = -1, vmax = 1)
    plt.axis('off')
    plt.show()

show_lattice(lattice)
metropolis_algorithm(lattice)
show_lattice(lattice)