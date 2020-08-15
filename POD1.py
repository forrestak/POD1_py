# Proper Orthogonal Decomposition Code through Singular Value Decomposition
# Forrest Mobley - 8/2020

import pandas as pd
import os
import plotly.graph_objs as go
import plotly
import numpy as np


def pod_svd(input_directory, header_value):
    # 1: Take input for data directory
    data = pd.DataFrame()
    for filename in sorted(os.listdir(input_directory)):
        data = pd.read_csv(filename, delim_whitespace=True, header=header_value)

    

# 2: Set input as working directory
# 3: Look for csv files, which should be ordered by timestep. Use this for finding number of timesteps
# 4: Read in data in matrices (columns: x,y,u,v)
# 5: Compute spatial correlation matrix
# 6: SVD
# 7: Basis Functions
# 8: Calculate Coefficient
# 9: Visualize
