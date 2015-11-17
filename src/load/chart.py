#!/usr/bin/python3

"""
load.chart
~~~~~~~~~~

This module implements classes for transforming extracted datasets related to
airport data.
"""

from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt
import math


def dist(lat1, lon1, lat2, lon2):
    """Distance in nm between two points.
    Equirectangular formula works for small distances."""
    x = (lon2 - lon1) * math.cos(0.5*math.radians(lat2+lat1))
    y = lat2 - lat1
    retval = 3440 * math.sqrt(x*x + y*y)
    #raise ValueError
    print(retval)
    return retval


class Chart:

    PT_LAT = 0
    PT_LON = 1
    PT_ALT = 2

    def __init__(self, trail_list, verbose=False):
        self.verbose = verbose
        self.trail_list = trail_list
        self.cropped_trails = self.trail_list

    def crop_out_of_range(self, latitude, longitude, distance, elevation):
        """Remove points from trail which are located further than the
        distance to the reference or higher than the given elevation"""

        # self.cropped_trails = [
        #     [pt for pt in trail] for trail in self.trail_list]

        self.cropped_trails = [
            [pt for pt in trail if (dist(
                lat1=latitude, lon1=longitude,
                lat2=pt[self.PT_LAT], lon2=pt[self.PT_LON]) < distance)
                and (pt[self.PT_ALT] < elevation)]
            for trail in self.trail_list]

    def plot(self, longitude, latitude, distance):
        self.data_list = [list(zip(*trail[::-1]))
                          for trail in self.cropped_trails]
        fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
        for trail in self.data_list:
            i = self.data_list.index(trail)
            ax.plot(trail[self.PT_LON], trail[self.PT_LAT], trail[self.PT_ALT],
                    color=(i/10, 1-i/10, 0.5))

            # TODO: think of drawing three plots: dep, enroute and arr b/c
            # of the difference in scale, also why not use a log scale for Z
            # ax.plot(trail[1], trail[0], trail[2], color=color[(i % 5)])

        ax.set_xlabel('lon')
        ax.set_xlim(longitude-distance/2, longitude+distance/2)
        ax.set_ylabel('lat')
        ax.set_ylim(latitude-distance/2, latitude+distance/2)
        ax.set_zlabel('alt')
        ax.set_zlim(0, 3000)
        plt.show()

