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
    fig = plt.figure(figsize=(8.53, 4.8))
    ax = fig.add_subplot(projection='3d')
    ax.view_init(elev=30, azim=45, roll=0)
    ax.set_xticks([-1,0,1],["-R", "0", "R"])
    ax.set_yticks([-1,0,1],["-R", "0", "R"])
    ax.set_zticks([-1,0,1],["-R", "0", "R"])
    ax.set_xlim(-1.1,1.1)
    ax.set_ylim(-1.1,1.1)
    ax.set_xlabel(r"$X$")
    ax.set_ylabel(r"$Y$")
    ax.set_zlabel(r"$Z$")
    titlesize = 15
    labelsize = 14
    legendfontsize = 12

    color_choice = ["red", "green", "blue"]
    for i_part in range(100):
        if i_part <=2:
            X,Y,Z = data[:,i_part]
            ax.scatter(X,Y,Z, color=color_choice[i_part], edgecolors='none', s=10)
    
    plt.savefig('../output/traj.png', dpi=dpi,bbox_inches='tight')
    plt.show()




def load_file(filename, in_line):
    data = np.fromfile(filename, dtype = np.float64)
    data = data.reshape(data.shape[0]//(in_line*3), in_line, 3).T
    return data

####################################
#            Parameters            #
####################################

# Number of particles
nb_part = 100
# Path to the file
filepath = '../output/position.bin'
# Size of the output GIF (in pixels)
figs = (10, 10)

####################################
#               Main               #
####################################


data = load_file(filepath, nb_part)
make_plot(data)

