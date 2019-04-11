'''
Created on Apr 11, 2019

@author: leonardo
'''

import numpy as np

def create_qwd(n_qbits, m_marked_itens):
    """
    Description:
        Make a quantum wave divider gate as specified on
        equation 22 in the article
    Required Params:
        n_qbits: Number of qbits that algorithm will computer
        m_marked_itens: Number of items marked on the data base
    Optional Params:
        None
    Return Value:
        A quantum wave divider gate
    Example:

    """
    
    n_data_base_size = 2 ** n_qbits
    
    a = np.sqrt( n_data_base_size / (2 * n_data_base_size - 4 * m_marked_itens) )
    b = None
    
    if m_marked_itens <= n_data_base_size / 4:
        b = np.sqrt( (n_data_base_size - 4 * m_marked_itens) / (2 * n_data_base_size - 4 * m_marked_itens) )
    
    else:
        b = np.sqrt( (4 * m_marked_itens - n_data_base_size) / (2 * n_data_base_size - 4 * m_marked_itens) )
        b = np.complex(0, b)
    
    
    gate_matrix = np.array(
        [[a, b],
         [b, -a]],
        dtype=complex
    )
    

    # Returning gate_matrix
    return gate_matrix



# a = 4 + 5j
# 
# b = 10
# 
# b = np.complex(0, b)
# 
# gate_matrix = np.array(
#             [[a, b],
#              [b, -a]],
#             dtype=complex
#         )
# 
# print(gate_matrix)
# 
# print("\n")

qwd = create_qwd(4, 5)

qwd_t = np.conjugate(qwd)
qwd_t = np.transpose(qwd_t)

print(qwd)
print("\n")
print(qwd_t)
print("\n")
print(np.dot(qwd, qwd_t))



