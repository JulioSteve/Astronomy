import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
import os

####################################
#             Functions            #
####################################

def make_plot(data):
    dpi = 300
    fig, ax = plt.subplots(ncols=2, figsize=(8.53, 4.8),layout="constrained")
    titlesize = 15
    labelsize = 14
    legendfontsize = 12

    ax[0].set_aspect("equal")
    ax[0].set_xlim(-1.1,1.1)
    ax[0].set_ylim(-1.1,1.1)
    ticks = [-1, 0, 1]
    ticklabels = ["-R", "0", "R"]
    ax[0].set_xticks(ticks, ticklabels)
    ax[0].set_yticks(ticks, ticklabels)
    ax[0].tick_params(axis="both", labelsize=labelsize)
    ax[0].set_title("One of the 2-bodies trajectory in the plane", size=titlesize)

    X1,Y1,Z = data[:,0]
    ax[0].scatter(X1,Y1, marker="o", s=15, color="black", label = "Body N°1", alpha=1)
    ax[0].legend(loc="upper left", fontsize=legendfontsize, markerscale=2)

    dt = 0.1
    T = np.linspace(0, dt*len(X1), len(X1))
    v = 0.35355339059327379 #obtained from Fortran
    ax[1].plot(T, X1, lw=3, color="black")
    ax[1].set_title("Evolution of one of the 2-bodies x-coordinate w/r to time", size=titlesize)
    ax[1].set_yticks([-1,0,1], ["-R", "0", "R"])
    ax[1].tick_params(axis="both", labelsize=labelsize)

    v_th = 2*np.pi/v
    v_m = 89.06/5
    print(f"T_th = {v_th:.2f}")
    print(f"T_meas = {v_m:.2f}")
    print(f"relative deviation: {abs(v_th-v_m)/v_th*100:.2f}%")

    # plt.savefig("../output/traj.png", format='png', dpi=dpi, bbox_inches="tight")
    # plt.show()


def load_file(filename, in_line):
    data = np.fromfile(filename, dtype = np.float64)
    data = data.reshape(data.shape[0]//(in_line*3), in_line, 3).T
    return data

####################################
#            Parameters            #
####################################

# Number of particles
nb_part = 2
# Path to the file
filepath = '../output/position.bin'
# Size of the output GIF (in pixels)
figs = (10, 10)

####################################
#               Main               #
####################################


data = load_file(filepath, nb_part)
make_plot(data)

