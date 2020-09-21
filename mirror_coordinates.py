import numpy as np
import matplotlib.pyplot as plt

x = 0.14
y = 0.14
space = 0.002
num_x = 11
num_y = 7

len_x = num_x*x+(x-1)*space
len_y = num_y*y+(y-1)*space

xvalues = np.arange(0, len_x, step=space+x) -(len_x-x)/2-space
yvalues = np.arange(0,len_y, step=space+y) -(len_y-y)/2-space

xx, yy = np.meshgrid(xvalues, yvalues)

# plt.plot(xx, yy, marker=',', color='k', linestyle='none')
# plt.plot(0,0,'ro')

coords_list = []
for lat in yy[:,0]:
    for long in xx[0]:
        coords_list.append([round(long,4),0, round(lat,4)])

with open('geometry/geometry1.yaml','r') as f:
    lines = f.readlines()
    
reflector=0
for count,line in enumerate(lines):
    if "reflector" in line:
        lines[count+1] = f'    transform: {{ rotation: [0 ,0, 0], translation: {coords_list[reflector]} }}\n'
        reflector += 1
with open('geometry/geometry2.yaml', 'w') as file:
    file.writelines(lines)