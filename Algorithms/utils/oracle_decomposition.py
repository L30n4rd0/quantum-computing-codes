'''
Created on Feb 14, 2019

@author: leonardo
'''

import numpy as np
from utils.gates_z import cz_q_2_q_0, cz_q_1_q_0, z_q_0, z_q_1, z_q_2,\
    cz_q_2_q_1, fredkin, create_controlled_n_not

class Gate(object):
    '''
    Unitary gate.
    '''
 
    def __init__(self, name, matrix):
        '''
        Create a new gate.
 
        name = instruction name string
        matrix = matrix of the gate
        
        return: none
        '''
        self.name = name
        self.matrix = matrix

    def equals(self, gateB):
        '''
        Compare two gates by their parameters
        
        gateB = gate to compare with self
        
        return:
        True = the gates are the same
        False = the gates are different
        
        '''
        
        if self.name != gateB.name:
            return False
        
        else:
            return equalsMatrix(self.matrix, gateB.matrix)
            
def equalsMatrix(matrixA, matrixB):
    if (len(matrixA) != len(matrixB)) or (len(matrixA[0]) != len(matrixB[0])):
        return False
    
    else:
        for i in range(len(matrixA)):
            for j in range(len(matrixA[0])):
                if matrixA[i][j] != matrixB[i][j]:
                    return False
                
    return True
                

    
def oracle_decomposition(gate_list, oracle_matrix):
    counter = 0
 
    for gate_1 in gate_list:
        solution_string = gate_1.name
        solution_matrix = gate_1.matrix
#         print(solution_string)
#         print(solution_matrix)
        
#         if counter > 0:
#             return "parou no primeiro ciclo"
            
        counter += 1
        print("counter: " + str(counter))
        
        if equalsMatrix(solution_matrix, oracle_matrix):
            return solution_string
         
        for gate_2 in gate_list:
            solution_string = solution_string + ' * ' + gate_2.name
            solution_matrix = np.dot(solution_matrix, gate_2.matrix)
#             print(solution_string)
#             print(solution_matrix)
            
            counter += 1
            print("counter: " + str(counter))
            
            if equalsMatrix(solution_matrix, oracle_matrix):
                return solution_string
            
            for gate_3 in gate_list:
                solution_string = solution_string + ' * ' + gate_3.name
                solution_matrix = np.dot(solution_matrix, gate_3.matrix)
#                 print(solution_string)
#                 print(solution_matrix)

                counter += 1
                print("counter: " + str(counter))
                
                if equalsMatrix(solution_matrix, oracle_matrix):
                    return solution_string
                
                for gate_4 in gate_list:
                    solution_string = solution_string + ' * ' + gate_4.name
                    solution_matrix = np.dot(solution_matrix, gate_4.matrix)
#                     print(solution_string)
#                     print(solution_matrix)

                    counter += 1
                    print("counter: " + str(counter))
                    
                    if equalsMatrix(solution_matrix, oracle_matrix):
                        return solution_string
                    
                    for gate_5 in gate_list:
                        solution_string = solution_string + ' * ' + gate_5.name
                        solution_matrix = np.dot(solution_matrix, gate_5.matrix)
#                         print(solution_string)
#                         print(solution_matrix)

                        counter += 1
                        print("counter: " + str(counter))
                        
                        if equalsMatrix(solution_matrix, oracle_matrix):
                            return solution_string
                        
                        for gate_6 in gate_list:
                            solution_string = solution_string + ' * ' + gate_6.name
                            solution_matrix = np.dot(solution_matrix, gate_6.matrix)
#                             print(solution_string)
#                             print(solution_matrix)

                            counter += 1
                            print("counter: " + str(counter))
                            
                            if equalsMatrix(solution_matrix, oracle_matrix):
                                return solution_string
                            
#                             for gate_7 in gate_list:
#                                 solution_string = solution_string + ' * ' + gate_7.name
#                                 solution_matrix = np.dot(solution_matrix, gate_7.matrix)
#     #                             print(solution_string)
# #                                 print(solution_matrix)
#     
#                                 counter += 1
#                                 print("counter: " + str(counter))
#                                 
#                                 if equalsMatrix(solution_matrix, oracle_matrix):
#                                     return solution_string
#                                 
#                                 for gate_8 in gate_list:
#                                     solution_string = solution_string + ' * ' + gate_8.name
#                                     solution_matrix = np.dot(solution_matrix, gate_8.matrix)
#         #                             print(solution_string)
# #                                     print(solution_matrix)
#         
#                                     counter += 1
#                                     print("counter: " + str(counter))
#                                     
#                                     if equalsMatrix(solution_matrix, oracle_matrix):
#                                         return solution_string
                            
                            
    return "It was not possible to decompose!!"

oracle_matrix = np.array(
    [[1, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, -1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 1]]
)

gate_list = []
gate_list.append(Gate('z_q_0', z_q_0))
gate_list.append(Gate('z_q_1', z_q_1))
gate_list.append(Gate('z_q_2', z_q_2))
gate_list.append(Gate('cz_q_1_q_0', cz_q_1_q_0))
gate_list.append(Gate('cz_q_2_q_0', cz_q_2_q_0))
gate_list.append(Gate('cz_q_2_q_1', cz_q_2_q_1))
# gate_list.append(Gate('fredkin', fredkin))
# gate_list.append(Gate('controlled_n_not', create_controlled_n_not(2)))


# for gate in gate_list:
#     print(gate.name)
#     print(gate.matrix)

print(oracle_decomposition(gate_list, oracle_matrix))

