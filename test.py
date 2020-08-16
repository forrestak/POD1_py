# Test file for testing POD1.py

from POD1 import pod_svd
import os

dat_Dir = os.path.join(os.getcwd(),'tempData')
x = 25
y = 1
header = 0
basename = 'data'
type = '.csv'
pod_svd(dat_Dir,x,y,basename,type,header)
