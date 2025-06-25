import numpy as np
import matplotlib.pyplot as plt

# Load energy file
P,K,L = np.loadtxt('../output/energy.dat', unpack=True)

alpha = 2*K[-1]/abs(P[-1])

print(f"alpha = {alpha:4.3}")

