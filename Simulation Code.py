#Ising Mode Simulation

#Importing necessary packages
import numpy as np
import matplotlib.pyplot as plt

#Setting up Parameters
#Size of Lattice (size x size)
size = 10         
#Temperature (K)         
T = 2.5         
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
    below = lattice[i, j - 1]
    above = lattice[i, j + 1]
    left = lattice[i - 1, j]
    right = lattice[i + 1, j]
    not_changed_U = -e*(center*below + center*above + center*left + center*right)
    changed_U = -e*(center_changed*below + center_changed*above + center_changed*left + center_changed*right)
    return changed_U - not_changed_U

#If delta U > 0 we flip the dipole with the following probability
def prob_of_flipping(i, j):
    prob = e^(-delta_U(i, j)/(kT))
    return prob

