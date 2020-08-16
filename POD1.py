# Proper Orthogonal Decomposition Code through Singular Value Decomposition
# Forrest Mobley - 8/2020

import pandas as pd
import os
# import plotly.graph_objs as go
import plotly
import numpy as np
import pathlib

# POD def for use elsewhere
# 4 Inputs: input_directory grid_x, grid_y, header_value
# input_directory is a string, giving the full directory
# grid_x and grid_y are the sizes of the rows and columns of dataset of each
# timestep
# header_value is an int, saying how many header lines are in each data file [0]
def pod_svd(input_directory, grid_x, grid_y, file_basename, file_type, header_value):
    count = 0
    for path in pathlib.Path(input_directory).iterdir():
        if path.is_file():
            count += 1
    #data = pd.DataFrame()
    DAT = np.zeros((grid_x, count-1))
    DAT_mean = np.zeros(count-1)
    i = 0
    for i in range(0,count-1,1):
        filename = os.path.join(input_directory,file_basename + str(i) + file_type)
        #data = pd.read_csv(filename, header=header_value, error_bad_lines=False, index_col=False)
        DAT[:,i] = np.loadtxt(filename, skiprows=header_value)
        DAT_mean[i] = np.mean(DAT[:,i], axis=0)
        #s[:,:,i] = data.to_numpy()
    #s_mean = np.reshape(count-1,1)
    DAT_mean = np.multiply(np.ones(grid_x).reshape(1,grid_x),DAT_mean.reshape(count-1,1)).reshape(grid_x,count-1)
    DAT_pert = DAT - DAT_mean
    u, s, vh = np.linalg.svd(DAT_pert, full_matrices=True)
    print(u.shape)
# 2: Set input as working directory
# 3: Look for csv files, which should be ordered by timestep. Use this for finding number of timesteps
# 4: Read in data in matrices (columns: x,y,u,v)
# 5: Compute spatial correlation matrix
# 6: SVD
# 7: Basis Functions
# 8: Calculate Coefficient
# 9: Visualize
