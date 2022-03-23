# cloud2mesh
Converting point clouds to textured meshes.

## Use
Open [`options.py`](options.py) and assign to `FILENAME` the path to your point cloud.

Enabling `SPLIT` will produce as many clouds as specified in `GRID_SIZE`, with the option to set their pivot as the center of the original cloud if enabling `CENTER_CLOUD`.

Enabling `PROCESS` will produce the meshes of all the clouds in the "clouds/" directory. By setting a path to a cloud in `SINGLE_FILENAME` only that file will be processed.

After adjusting settings, run the [`main.py`](main.py) script. Outputs are stored in individual folders in the "clouds/" directory.