#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 19:28:35 2019

@author: Nikita Letov (McGill University, Canada)
"""

# Importing libraries
import matplotlib.pyplot as plt # the library for plotting
import numpy as np # the library for working with matrices
from mpl_toolkits.mplot3d import Axes3D # the library for working with 3D
# objects

# The function for generating of a design space
def make_ax(grid = False):
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.grid(grid)
    return ax

# Main function
def main():
    ax = make_ax(True)
    
    filled = np.ones((3, 3, 3))
    x, y, z = np.indices(np.array(filled.shape) + 1)
    x[3, 2, 2] = 5
    
    colors = np.array([[['#7A88CCC0'] * 3] * 3] * 3)
    red = '#FF0000FF'
    colors[2, 1, 2] = red
    colors[2, 2, 2] = red
    colors[2, 1, 1] = red
    colors[2, 2, 1] = red
    
    ax.voxels(x, y, z, filled, facecolors = colors, edgecolor = 'black')
    ax.auto_scale_xyz([0, 5], [0, 5], [0, 5])
    plt.show()
    
# Entry point
if __name__ == '__main__':
    main()