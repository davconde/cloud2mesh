import os

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def find_files(dirpath):
    """
    Recursively detect files contained in a folder
    """
    files = [os.path.join(root, filename)
             for root, dirs, files in os.walk(dirpath)
             for filename in files]
    return files


def plot_histogram(array, bins=50, title=''):
    hist, edges = np.histogram(array, bins=bins)
    bar_width = 0.7 * (edges[1] - edges[0])
    hist_c = (edges[:-1] + edges[1:]) / 2
    plt.bar(hist_c, hist, align='center', width=bar_width)
    plt.title(title)
    plt.show()


class VoxelGrid():
    '''
    Class to compute and hold a point cloud voxelization
    '''
    def __init__(self, cloud, grid_size=[1, 1, 1],
                 center=False, verbose=False):
        self.cloud = cloud
        self.grid_size = grid_size
        self.grid_center = None
        self.segs = None
        self.grid = None
        self.center = center
        self.verbose = verbose
        self.compute()

    def find_limits(self):
        '''
        Find min and max coordinates in the cloud
        as well as voxel segments limits
        '''
        min_coords = [self.cloud[axis].min() for axis in ['x', 'y', 'z']]
        max_coords = [self.cloud[axis].max() for axis in ['x', 'y', 'z']]
        self.grid_center = [(max_coords[axis] + min_coords[axis]) / 2
                            for axis in range(3)]
        self.segs = [np.linspace(min_coords[axis], max_coords[axis],
                                 num=self.grid_size[axis] + 1)
                     for axis in range(3)]

    def center_cloud(self):
        '''
        Sets the origin at the bounding box center
        '''
        for axis, idx in zip(['x', 'y', 'z'], range(3)):
            self.cloud[axis] -= self.grid_center[idx]
            self.segs[idx] -= self.grid_center[idx]

    def build_voxel(self, x, y, z):
        '''
        Builds the voxel DataFrame into a dictionary
        '''
        key = str(x) + '_' + str(y) + '_' + str(z)
        if self.verbose:
            print('Generating voxel ' + key)
        self.grid[key] = self.cloud[(self.cloud['x'] >= self.segs[0][x]) &
                                    (self.cloud['x'] < self.segs[0][x + 1]) &
                                    (self.cloud['y'] >= self.segs[1][y]) &
                                    (self.cloud['y'] < self.segs[1][y + 1]) &
                                    (self.cloud['z'] >= self.segs[2][z]) &
                                    (self.cloud['z'] < self.segs[2][z + 1])]

    def build_grid(self):
        '''
        Fills a dictionary with DataFrame objects
        containing the points of each voxel
        '''
        if self.verbose:
            print('Building grid')
        self.grid = {}
        for i in range(len(self.segs[0]) - 1):
            for j in range(len(self.segs[1]) - 1):
                for k in range(len(self.segs[2]) - 1):
                    self.build_voxel(i, j, k)

    def get_grid(self):
        return self.grid

    def set_grid(self, grid):
        self.grid = grid

    def save_to_file(self, filename, voxel_key=None):
        '''
        Export a unique file after working
        with a VoxelGrid is done
        '''
        if voxel_key is None:
            full_cloud = pd.concat(self.grid)
            full_cloud.to_csv(filename, sep=' ',
                              header=False, index=False)
        else:
            self.grid[voxel_key].to_csv(filename, sep=' ',
                                        header=False, index=False)

    def compute(self):
        '''
        Execution sequence
        '''
        self.find_limits()
        if self.center:
            self.center_cloud()
        self.build_grid()
