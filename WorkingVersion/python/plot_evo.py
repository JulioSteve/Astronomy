import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
import os

####################################
#             Functions            #
####################################

def make_images(in_i, figsize):
    fig = plt.figure(figsize = figsize, facecolor = 'k', num = 1)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_box_aspect([1, 1, 1])
    ax.scatter(data[in_i, :, 0], data[in_i, :, 1], data[in_i, :, 2], s=10, marker="*",color='w', linewidths=0, edgecolors="none")
    ax.axes.set_xlim3d(left=-1.2, right=1.2) 
    ax.axes.set_ylim3d(bottom=-1.2, top=1.2) 
    ax.axes.set_zlim3d(bottom=-1.2, top=1.2)
    ax.set_axis_off()
    ax.set_facecolor("k")
    plt.savefig('../gif_data/pos_{}.png'.format(in_i), bbox_inches='tight',pad_inches = 0)
    plt.clf()

def make_gif(in_nb):
    im = [Image.open("../gif_data/pos_{}.png".format(i)) for i in range(in_nb)]
    im[0].save('../output/pos.gif', save_all=True, append_images=im[1:], duration=10, loop=0)
    files = os.listdir("../gif_data")


def load_file(filename, in_line):
    data = np.fromfile(filename, dtype = np.float64)
    data = data.reshape(data.shape[0]//(in_line*3), in_line, 3)
    return data

####################################
#            Parameters            #
####################################

# Number of particles
nb_part = 5000
# Path to the file
filepath = '../output/position.bin'
# Size of the output GIF (in pixels)
figs = (10, 10)

####################################
#               Main               #
####################################


data = load_file(filepath, nb_part)

nb_time = np.shape(data)[0]
for i in range(nb_time):
    make_images(i, figs)
    print('Image {}/{} done'.format(i, nb_time-1), end = "\r")
print("\n")

print('Making GIF...')
make_gif(nb_time)
print('GIF done')
