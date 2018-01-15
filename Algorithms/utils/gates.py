'''
Created on 14 de jan de 2018

@author: leonardo
'''

import numpy as np

'''Pauli-identity gate'''
i = np.identity(2, dtype=complex)

'''Pauli-X gate (= NOT gate)'''
x = np.array(
        [[0, 1],
         [1, 0]],
        dtype=complex
    )

'''Pauli-Y gate'''
y = np.array(
        [[0, 0. - 1.j],
         [0. + 1.j, 0]],
        dtype=complex
    )

'''Pauli-Z gate (fase gate)'''
z = np.array(
        [[1, 0],
         [0, -1]],
        dtype=complex
    )

'''Hadamard (H) gate'''
h = np.array(
        [[1/np.sqrt(2), 1/np.sqrt(2)],
         [1/np.sqrt(2), -1/np.sqrt(2)]],
        dtype=complex
    )

'''Controlled NOT gate'''
c_not = np.array(
        [[1, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 0, 1],
         [0, 0, 1, 0]],
        dtype=complex
    )

