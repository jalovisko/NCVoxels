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

# The surface class
class Surface:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def centroid(self):
        cm_x = np.average(self.x)
        cm_y = np.average(self.y)
        cm_z = np.average(self.z)
        
        return (cm_x, cm_y, cm_z)
        
        
# The torus class (inherites from the surface class).
# Note that the torus is made around the origin point (0, 0, 0).
class Torus(Surface):
    def __init__(self, radius, tube_radius, n = 100):

        self.n = n
        self.radius = radius
        self.tube_radius = tube_radius
        
        theta = np.linspace(0, 2.*np.pi, n)
        phi = np.linspace(0, 2.*np.pi, n)
        theta, phi = np.meshgrid(theta, phi)
        
        self.x = (radius + tube_radius*np.cos(theta)) * np.cos(phi)
        self.y = (radius + tube_radius*np.cos(theta)) * np.sin(phi)
        self.z = tube_radius * np.sin(theta)
        
    def centroid(self):
        
        cm_x = np.average(np.delete(self.x, self.n - 1, 0))
        cm_y = np.average(np.delete(self.y, self.n - 1, 0))
        cm_z = np.average(np.delete(self.z, self.n - 1, 0))
        
        return (cm_x, cm_y, cm_z)

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
def plot_torus(torus):
    (x, y, z) = (torus.x, torus.y, torus.z)
    
    ax = make_ax(True)
    ax.set_zlim(-3 * torus.tube_radius, 3 * torus.tube_radius)
    ax.plot_surface(x, y, z, rstride=5, cstride=5, color='k', edgecolors='w')
    ax.view_init(36, 26)
    
    plt.show()
    

# Function implementing the long-axis rule.
def LAR(surface, n = 1):
    pass

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