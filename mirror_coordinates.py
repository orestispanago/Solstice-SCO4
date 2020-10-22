import numpy as np
import matplotlib.pyplot as plt
from config import geom


mir_len_x = geom.mirror_array.mirror_dimensions.x
mir_len_y = geom.mirror_array.mirror_dimensions.y
space = geom.mirror_array.space
num_x = geom.mirror_array.number_of_mirrors.x
num_y = geom.mirror_array.number_of_mirrors.y



def create_coords(dim,space,num_elements):
    step = dim + space
    coords = np.arange(0,num_elements)*step
    return coords - coords[-1]/2 # center coords at rectangle center

def plot_coords():
    xx, yy = np.meshgrid(centered_x, centered_y)
    plt.plot(xx, yy, marker=',', color='k', linestyle='none')
    plt.plot(0,0,'ro')


centered_x = create_coords(mir_len_x, space, num_x)
centered_y = create_coords(mir_len_y, space, num_y)
    
# plot_coords()



