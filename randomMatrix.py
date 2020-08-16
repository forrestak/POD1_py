# Random matrix maker
# Making random data files for testing POD1.py

import numpy as np
import pandas as pd

for i in range(0,100,1):
    temp = np.random.randint(0,101, size=(25,1))
    #df = pd.DataFrame(temp)
    file_Name = 'tempData/data' + str(i) + '.csv'
    #df.to_csv(file_Name, float_format='%1.0f', header=False, index=False)
    np.savetxt(file_Name, temp, fmt='%1.0f')
