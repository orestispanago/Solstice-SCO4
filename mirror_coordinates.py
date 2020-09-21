import numpy as np
import matplotlib.pyplot as plt

x = 0.07
y = 0.07
space = 0.002
num_x = 11
num_y = 7

len_x = num_x*x+(x-1)*space
len_y = num_y*y+(y-1)*space

xvalues = np.arange(0, len_x, step=space+x)#-(len_x-x)/2-space
yvalues = np.arange(0,len_y, step=space+y) #-(len_y-y)/2-space

xx, yy = np.meshgrid(xvalues, yvalues)

plt.plot(xx, yy, marker=',', color='k', linestyle='none')
plt.plot(0,0,'ro')


with open('coords.txt', 'w') as outf:
    for lat in yy[:,0]:
        for long in xx[0]:
            outf.write(f"{long:.4f}, {lat:.4f}, 0\n")