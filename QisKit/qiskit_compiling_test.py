'''
Created on Apr 12, 2019

@author: leonardo
'''
import numpy as np
from qiskit.mapper._compiling import two_qubit_kak, euler_angles_1q
from utils import print_list

def generate_circuit_two_qubits(unitary_matrix_4x4):
    
    gate_list = two_qubit_kak(unitary_matrix_4x4)
    # print("gate_list")
    # print_list(gate_list)
    
    for gate_dict in gate_list:
        
        if gate_dict['name'] == 'cx':
            # qc.cx(q[0], q[1])
            print("qc." + gate_dict['name'] + 
                  "(" + 
                  "q[" + str( gate_dict['args'][0] ) + "], " + 
                  "q[" + str( gate_dict['args'][1] ) + "]" + 
                  ")"
            )
            
        else:
            # qc.u3(1.5707963267948966, 3.141592653589793, -3.141592653589793, q[0])
            print("qc.u3" + # gate_dict['name'] + 
                  "(" + 
                  str( gate_dict['params'][0] ) + ", " + 
                  str( gate_dict['params'][1] ) + ", " + 
                  str( gate_dict['params'][2] ) + ", " + 
                  "q[" + str( gate_dict['args'][0] ) + "]" + 
                  ")"
            )
        


def generate_circuit_one_qubit(unitary_matrix_2x2):
    
    tuple_data = euler_angles_1q(unitary_matrix_2x2)
    
    list_data = list(tuple_data)
    
    print("qc.u3" + 
          "(" + 
          str( list_data[0] ) + ", " + 
          str( list_data[1] ) + ", " + 
          str( list_data[2] ) + ", " + 
          "q[0]" + 
          ")"
    )



# matrix = np.array(
#     [[1, 0, 0, 0],
#      [0, -1, 0, 0],
#      [0, 0, -1, 0],
#      [0, 0, 0, 1]]
# )
# generate_circuit_two_qubits(matrix)


# Divider to 3 qubit of works on algorithm n 4 fixed point search
matrix = np.array(
    [[0.81649658+0.j,  0.57735027+0.j],
     [0.57735027+0.j, -0.81649658+0.j]],
    dtype=complex
)
 
generate_circuit_one_qubit(matrix)

