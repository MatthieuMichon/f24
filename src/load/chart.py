#!/usr/bin/python3

"""
load.chart
~~~~~~~~~~

This module implements classes for transforming extracted datasets related to
airport data.
"""

from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt


class Chart:

    def __init__(self, trail_list, verbose=False):
        self.data_list = [list(zip(*trail[::-1])) for trail in trail_list]

    def plot(self, longitude, latitude, distance):
        fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
        color = ['r', 'b', 'g', 'k', 'm']
        for trail in self.data_list:
            i = self.data_list.index(trail)
            ax.plot(trail[1], trail[0], color=color[(i % 5)])

            # TODO: think of drawing three plots: dep, enroute and arr b/c
            # of the difference in scale, also why not use a log scale for Z
            # ax.plot(trail[1], trail[0], trail[2], color=color[(i % 5)])

        ax.set_xlabel('X')
        ax.set_xlim(longitude-distance/2, longitude+distance/2)
        ax.set_ylabel('Y')
        ax.set_ylim(latitude-distance/2, latitude+distance/2)
        ax.set_zlabel('Z')
        ax.set_zlim(-1, 1)
        plt.show()
