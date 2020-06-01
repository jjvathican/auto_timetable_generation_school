
import numpy as np
from io import StringIO

d = StringIO("M 21 72\nF 35 58")
y=np.loadtxt(d, dtype={'names': ('gender', 'age', 'weight'),
                     'formats': ('S1', 'i4', 'f4')})



print(y)