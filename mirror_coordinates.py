import numpy as np
import matplotlib.pyplot as plt
import utils
from run import transversal_plain_ideal
import pandas as pd
# from traces import geometry, geometry_heat

geometry = "geometry/glass-ideal-mirrorbox.yaml"
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
        f"translation: [&abs_x {x}, 1.5, &abs_y {y}] }}\n"
    utils.replace_line(geometry,newline=abs_transform)

def add_mirrorbox(geometry, box_space_x=0.01, box_h = 0.1, box_space_y = 0.01):
    box_z = centered_x[-1]+x/2 + box_space_x
    box_z_h = f"            - [ &box_z {box_z},        *box_h]\n"
    box_z_neg = f"            - [ &box_z_neg {-box_z},   &box_h_neg {-box_h}]\n"
    box_h_pos = f"            - [ *box_z_neg,         &box_h {box_h}]\n"
    utils.replace_line(geometry, occurrence="&box_z ", newline=box_z_h)
    utils.replace_line(geometry, occurrence="&box_z_neg", newline=box_z_neg)
    utils.replace_line(geometry, occurrence="&box_h ", newline=box_h_pos)
    
    box_x = centered_y[-1]+y/2 + box_space_y
    box_x_pos = f"            - [ &box_x {box_x},       *box_h]\n"
    box_x_neg = f"            - [ &box_x_neg {-box_x},  *box_h_neg]\n"
    utils.replace_line(geometry, occurrence="&box_x ", newline=box_x_pos)
    utils.replace_line(geometry, occurrence="&box_x_neg ", newline=box_x_neg)

centered_x = create_coords(x, space, num_x)
centered_y = create_coords(y, space, num_y)
    
# plot_coords()


append_reflectors_to_yaml(geometry)
# append_reflectors_to_yaml(geometry_heat)
move_absorber(geometry, 0, 0)

add_mirrorbox(geometry)