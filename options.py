FILENAME = 'input/Cloud.txt'
DEBUG = True

# Tasks
SPLIT = True
PROCESS = True

# Input settings
RGB_MODE = 0  # 0 -> [0-255]; # 1 -> [0.0-1.0]
DATA_FORMAT = 'X Y Z R G B Reflectance'  # default: 'X Y Z R G B Reflectance'

# Splitting options
CENTER_CLOUD = True
GRID_SIZE = [4, 4, 1]

# Processing options
SINGLE_FILENAME = None  # if 'None', process all files in 'clouds' folder
TEXTDIM = 4096
SIMPLIF_PRCNT = 100
