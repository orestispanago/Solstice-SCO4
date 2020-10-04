import numpy as np
import matplotlib.pyplot as plt
import utils
from run import transversal_plain_ideal
import pandas as pd
# from traces import geometry, geometry_heat

geometry = "geometry/glass-ideal.yaml"
geometry_heat= "geometry/heatmap/glass-ideal.yaml"

x = 0.14  # mirror x dimension
y = 0.14
space = 0.002  # space between mirrors
num_x = 11  # number of mirrors in x direction
num_y = 7


def create_coords(dim,space,num_elements):
    step = dim + space
    coords = np.arange(0,num_elements)*step
    return coords - coords[-1]/2 # center coords at rectangle center

def plot_coords():
    xx, yy = np.meshgrid(centered_x, centered_y)
    plt.plot(xx, yy, marker=',', color='k', linestyle='none')
    plt.plot(0,0,'ro')

def append_reflectors_to_yaml(fpath):
    """ Appends reflectors to yaml as entities """
    utils.keep_until(fpath, occurrence='reflector', lines_before=1)
    count=1
    with open(fpath, 'a') as f:
        for x in centered_x:
            for y in centered_y:
                reflector = f"- entity:\n    name: reflector{count}\n"\
                    f"    transform: {{ rotation: [0 ,0, 0], "\
                        f"translation: [ {x:.3f}, 0, {y:.3f} ] }}\n"\
                        "    children: [ *self_oriented_facet ]\n\n"
                f.writelines(reflector)
                count+=1

def move_absorber(geometry, x,y):
    abs_transform=f"    transform: {{ rotation: [90, 0, 0], "\
        f"translation: &absorber_translation [{x}, 1.5, {y}] }}\n"
    utils.replace_line(geometry,newline=abs_transform)

centered_x = create_coords(x, space, num_x)
centered_y = create_coords(y, space, num_y)
    
# plot_coords()


# append_reflectors_to_yaml(geometry)
# move_absorber(geometry, 0,0)
# append_reflectors_to_yaml(geometry_heat)

