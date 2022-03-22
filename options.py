filename = 'input/Cloud.txt'
debug = True

# Tasks
split = True
process = True

# Input settings
rgbmode = 0  # 0 -> [0-255]; # 1 -> [0.0-1.0]
data_format = 'X Y Z R G B Reflectance'  # default: 'X Y Z R G B Reflectance'

# Splitting options
center_cloud = True
grid_size = [4, 4, 1]

# Processing options
# single_filename = None  # if 'None', process all files in 'clouds' folder
single_filename = 'clouds\\Cloud_2_1_0.txt'
textdim = 4096
simplif_prcnt = 100
