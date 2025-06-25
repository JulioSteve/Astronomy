import numpy as np
import matplotlib.pyplot as plt

def plot_energ(data):
    plt.figure(figsize=(7,4))
    plt.subplot(211)
    plt.plot(data[:, 0], marker='', ls='-', color='red', label = 'Ep')
    plt.plot(data[:, 1], marker='', ls='-', color='orange', label = 'Ec')
    plt.plot(data[:, 0] + data[:, 1], marker='', ls='-', color='pink', label = 'Etotal')
    plt.plot(data[:, 2], marker='', ls='-', color='green', label = 'Total Angular Momentum')
    plt.xlabel('Step')
    plt.ylabel('Energy')
    plt.legend()
    plt.subplot(212)
    plt.plot(data[:, 0] + data[:, 1], marker='', ls='-', color='pink', label = 'Etotal sequential')
    plt.xlabel('Step')
    plt.ylabel('Energy')
    plt.legend()
    plt.savefig('../output/energy_seq.png', bbox_inches='tight')
    plt.show()

# Load energy file
energ = np.loadtxt('../output/energy.dat')

# Plot energy
plot_energ(energ)