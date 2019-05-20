'''
Created on Apr 11, 2019

@author: leonardo
'''

import numpy as np
from utils.gates import create_n_4_qwd_gate


qwd = create_n_4_qwd_gate(4, 5)

qwd_t = np.conjugate(qwd)
qwd_t = np.transpose(qwd_t)

print(qwd)
print("\n")
print(qwd_t)
print("\n")
print(np.dot(qwd, qwd_t))



