import numpy as np
import matplotlib.pyplot as plt
import utils
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

def get_coords_from_mesh():
    """ Meshgrid to list of [x,y,z]"""
    coords = []
    for lat in yy[:, 0]:
        for long in xx[0]:
            coords.append([round(long, 4), 0, round(lat, 4)])
    return coords

def append_reflectors_to_yaml(fpath):
    """ Appends reflectors to yaml as entities """
    coords = get_coords_from_mesh()
    with open(fpath, 'a') as f:
        for count,i in enumerate(coords):
            reflector = f"- entity:\n    name: reflector{count+1}\n"\
                f"    transform: {{ rotation: [0 ,0, 0], translation: {i} }}\n"\
                    "    children: [ *self_oriented_facet ]\n\n"
            f.writelines(reflector)

centered_x = create_coords(x, space, num_x)
centered_y = create_coords(y, space, num_y)

xx, yy = np.meshgrid(centered_x, centered_y)

plt.plot(xx, yy, marker=',', color='k', linestyle='none')
plt.plot(0,0,'ro')

utils.keep_until(geometry, occurence='reflector', lines_before=1)
utils.keep_until(geometry_heat, occurence='reflector', lines_before=1)

append_reflectors_to_yaml(geometry)
append_reflectors_to_yaml(geometry_heat)
