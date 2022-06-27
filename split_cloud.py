import os

import pandas as pd

import options
from utils import VoxelGrid


def write_files(grid_obj, filename):
    '''
    Write new files with splitten clouds
    '''
    print('Writing files')
    if not os.path.exists('clouds'):
        os.makedirs('clouds')
    name, ext = filename.rsplit('.', 1)
    _, name = name.rsplit('/', 1)
    grid = grid_obj.get_grid()
    for key in grid:
        if len(grid[key]) > 0:
            grid[key].to_csv('clouds/' + name + '_' + key + '.' + ext,
                             sep=' ', header=False, index=False)


def split_cloud(filename, grid_size=[1, 1, 1]):
    names = options.DATA_FORMAT.split(' ')
    for i in range(3):
        names[i] = names[i].lower()
    cloud = pd.read_csv(filename,
                        sep=options.COLUMN_SEPARATOR,
                        header=None,
                        names=names)

    grid_obj = VoxelGrid(cloud, grid_size,
                         center=options.CENTER_CLOUD, verbose=options.DEBUG)
    write_files(grid_obj, filename)
    print('Splitting finished')
