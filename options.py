FILENAME = 'input/Cloud.txt'
DEBUG = False

# Tasks
SPLIT = True
PROCESS = True

# Input settings
RGB_MODE = 0  # range of color: 0 -> [0-255]; # 1 -> [0.0-1.0]
DATA_FORMAT = 'X Y Z R G B Reflectance'  # default: 'X Y Z R G B Reflectance'
COLUMN_SEPARATOR = ' '  # character to separate columns in the TXT cloud

# Splitting options
CENTER_CLOUD = True  # set local origin at the center of the cloud
GRID_SIZE = [4, 4, 1]  # number of splits per axis

# Processing options
SINGLE_FILENAME = None  # if 'None', process all files in 'clouds' folder
TEXTDIM = 4096  # resolution of the texture
SIMPLIF_PRCNT = 100  # simplification percentage of each cloud split
LARGEST_FACE_THRES = 0.9  # a lower value prevents removing long planes
