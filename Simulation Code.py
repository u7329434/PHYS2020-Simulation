#Ising Mode Simulation

import numpy as np
import matplotlib.pyplot as plt
#Setting up Parameters
# Size of Lattice (size x size)
size = 10         
#Temperature (Given in units of e/K)          
T = 2.5         
#energy of neighboring dipoles, energy = -e when parallel and +e when parallel
e = 1

#Initial lattice with each dipole randomly either having spin up or down
lattice = np.random.choice([1, -1], size = (size, size))

def delta_U(i, j):
    center = lattice[i, j]
    center_changed = -lattice[i, j]
    below = lattice[i, j - 1]
    above = lattice[i, j + 1]
    left = lattice[i - 1, j]
    right = lattice[i + 1, j]
    initial_U = -e*(center*below + center*above + center*left + center*right)
    final_U = -e*(center_changed*below + center_changed*above + center_changed*left + center_changed*right)
    return final_U - initial_U



