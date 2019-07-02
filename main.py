# Exercise 6
from pathlib import Path

input_dir  = Path("data")

# 1. Read the Scene that you downloaded from the data directory using SatPy. [2P]
files = find_files_and_readers(base_dir = input_dir, reader = "seviri_l1b_nc")
scn = Scene(filenames = files)

# 2. Load the composites "natural_color" and "convection" [2P]

# 3. Resample the fulldisk to the Dem. Rep. Kongo and its neighbours [4P] 
#    by defining your own area in Lambert Azimuthal Equal Area. 
#    Use the following settings:
#      - lat and lon of origin: -3/23
#      - width and height of the resulting domain: 500px
#      - projection x/y coordinates of lower left: -15E5
#      - projection x/y coordinates of upper right: 15E5 

# 4. Save both loaded composites of the resampled Scene as simple png images. [2P]
