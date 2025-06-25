import numpy as np
import matplotlib.pyplot as plt

# Load energy file
P,K,L = np.loadtxt('../output/energy.dat', unpack=True)

timesteps = len(P)

A = np.zeros(timesteps)
for t in range(timesteps): 
    alpha = 2*K[t]/abs(P[t])
    A[t] = alpha

dt = 0.1
T = np.linspace(0, dt*timesteps, timesteps)

titlesize = 17
labelsize = 14
legendfontsize = 12

plt.plot(T,A, color="black", lw=3)
plt.xlabel("Simulation time (reduced units)", size=labelsize)
plt.ylabel(r"$\alpha$ value (unitless)", size=labelsize)
plt.title(rf"$\alpha_0 \approx {A[0]:4.2f}$ and $\alpha_f \approx {A[-1]:4.2f}$, $\overline{{\alpha}} = {np.mean(A):.2f}$:", fontsize=titlesize)
plt.xticks([0, T[-1]], [r"$t_0$", r"$t_f$"], size=labelsize)
yticks = np.sort(np.append(np.linspace(min(A), max(A), 5), 1.0))
ylabels = [f"{tick:.2f}" for tick in yticks]
plt.yticks(yticks, ylabels, size=labelsize)
plt.grid()
plt.tight_layout()

plt.savefig("../output/alpha.png", format='png', bbox_inches='tight')
plt.show()

