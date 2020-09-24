import numpy as np
import matplotlib.pyplot as plt


x = 0.14  # mirror x dimension
y = 0.14
space = 0.002  # space between mirrors
num_x = 11  # number of mirrors in x direction
num_y = 7

len_x = num_x*x+(x-1)*space
len_y = num_y*y+(y-1)*space

# Substract - (len_x-x)/2-space to set array center at 0,0
xvalues = np.arange(0, len_x, step=space+x) - (len_x-x)/2-space
yvalues = np.arange(0, len_y, step=space+y) - (len_y-y)/2-space

xx, yy = np.meshgrid(xvalues, yvalues)

# plt.plot(xx, yy, marker=',', color='k', linestyle='none')
# plt.plot(0,0,'ro')


def get_coords_from_mesh():
    """ Meshgrid to list of [x,y,z]"""
    coords = []
    for lat in yy[:, 0]:
        for long in xx[0]:
            coords.append([round(long, 4), 0, round(lat, 4)])
    return coords


def coords_to_yamls(geometry='geometry/geometry.yaml'):
    """ Writes mirror coordinates to geometry.yaml and heatmap/geometry.yaml
    make sure that the number of reflector entities equals the number of coordinates"""
    coords = get_coords_from_mesh()
    with open(geometry, 'r') as f:
        lines = f.readlines()
    reflector = 0
    for count, line in enumerate(lines):
        if "reflector" in line:
            lines[count+1] = f'    transform: {{ rotation: [0 ,0, 0], translation: {coords[reflector]} }}\n'
            reflector += 1
    with open(geometry, 'w') as geom, open('heatmap/geometry.yaml', 'w') as geom_heat:
        geom.writelines(lines)
        geom_heat.writelines(lines)


coords_to_yamls()
