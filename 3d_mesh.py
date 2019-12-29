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

# The function for plotting a torus with matplotlib
def make_torus():
    n = 100

    theta = np.linspace(0, 2.*np.pi, n)
    phi = np.linspace(0, 2.*np.pi, n)
    theta, phi = np.meshgrid(theta, phi)
    c, a = 2, 1
    x = (c + a*np.cos(theta)) * np.cos(phi)
    y = (c + a*np.cos(theta)) * np.sin(phi)
    z = a * np.sin(theta)
    
    fig = plt.figure()
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.set_zlim(-3,3)
    ax1.plot_surface(x, y, z, rstride=5, cstride=5, color='k', edgecolors='w')
    ax1.view_init(36, 26)
    ax2 = fig.add_subplot(122, projection='3d')
    ax2.set_zlim(-3,3)
    ax2.plot_surface(x, y, z, rstride=5, cstride=5, color='k', edgecolors='w')
    ax2.view_init(0, 0)
    ax2.set_xticks([])
    plt.show()

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