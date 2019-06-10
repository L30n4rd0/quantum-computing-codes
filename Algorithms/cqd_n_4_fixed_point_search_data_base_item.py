"""
Created on April 5, 2019

Simulation of the article An N/4 fixed-point duality quantum search algorithm - HAO Liang et al - 2010

@author: leonardo
"""


import numpy as np
from utils.gates import i, z, h, create_n_4_qwd_gate, create_controlled_u_gate
from utils.operations import apply_tensor, apply_n_tensor_to, apply_gate_to_psi, print_psi, apply_projective_operator, plot_psi
from utils.qbits import qubit_zero

############################################################
####### Circuit Properties #################################
############################################################
# Number of work qubits that algorithm will compute
n = 4

# Number of items marked on the data base
m = 2

dim_work = 2**n


############################################################
####### Circuit Gates ######################################
############################################################
# Creating projector operator to item to search
items_to_search_projector = np.zeros((dim_work, dim_work), dtype=complex)
for index in range(dim_work - 1, dim_work - 1 - m, -1):
    items_to_search_projector[index][index] = 1
print("\nitems_to_search_projector")
print(items_to_search_projector.real)


# Creating Identity's tensors to work qubits
tensor_i = np.identity(2**n, dtype=complex)


# Creating Hadamard's tensors to work qubits
# This gate is used to create a evenly distributed 
# state with work qubits, in equation 8
tensor_h = apply_n_tensor_to(n, h)
print("\ntensor_h")
print(tensor_h.real)
 
 
# Creating u_tau gate (the oracle)
# On the article, in equation 9, the u_tau is defined as:
# u_tau = identity - 2 * items_to_search_projector
u_tau = tensor_i - (2 * items_to_search_projector)
print("\nu_tau")
print(u_tau.real)
 
 
# Creating v gate (qwd)
# On the article it is defined in equation 11
v = create_n_4_qwd_gate(n, m)
print("\nv operator")
print(v)


# Creating controlled_0_Us (controlled_0_u_0)
# On the article, in equation 15, the u_s is defined as:
# u_s = 2 * |psi_0><psi_0| - identity
# On the article, in equation 8, the |psi_0> is defined as:
psi_0 = apply_n_tensor_to(n, qubit_zero)
print("psi_0")
print_psi(psi_0)
psi_0 = apply_gate_to_psi(tensor_h, psi_0)
print("psi_0")
print_psi(psi_0)

# |psi_0><psi_0|
psi_0_transposed_psi_0 = np.dot(psi_0, np.transpose(psi_0))
print("psi_0_transposed_psi_0")
print(psi_0_transposed_psi_0)

# 2 * |psi_0><psi_0| - identity
u_s = 2 * psi_0_transposed_psi_0 - tensor_i
print("u_s")
print(u_s)

# u_s = 2 * items_to_search_projector - tensor_i
controlled_0_Us = create_controlled_u_gate(u_s, 0)

print("\ncontrolled_0_Us")
print(controlled_0_Us.real)


# Creating controlled_1_negative_identity (controlled_1_u_1)
# On the article, in equation 15, this gate
# invert all coefficients of the down sub wave 
# controlled_1_negative_identity = apply_tensor(tensor_i, z)
controlled_1_negative_identity = create_controlled_u_gate(-1 * tensor_i, 1)
print("\ncontrolled_1_negative_identity")
print(controlled_1_negative_identity.real)


# Creating projection_operator
zero_projection_operator = np.dot(qubit_zero, np.transpose(qubit_zero))
projection_operator = apply_tensor( tensor_i, zero_projection_operator )
print("\nprojection_operator")
print(projection_operator.real)


############################################################
####### Circuit Execution ##################################
############################################################
# psi_0 - Creating tensor product between inputs: |000000>
psi = apply_n_tensor_to(n + 1, qubit_zero)
print("\npsi_0 - Creating tensor product between inputs: |000000>\n")
print_psi(psi)


# psi_1 - Applying tensor_h to psi_0 on work qubits
psi = apply_gate_to_psi( apply_tensor(tensor_h, i), psi )
print("\npsi_1 - Applying tensor_h to psi_0 on work qubits\n")
print_psi(psi)


# psi_2 - Applying u_tau to psi_1
psi = apply_gate_to_psi( apply_tensor(u_tau, i), psi )
print("\npsi_2 - Applying u_tau to psi\n")
print_psi(psi)


# psi_3 - Applying v (qwd) to psi_2
psi = apply_gate_to_psi( apply_tensor(tensor_i, v), psi )
print("\npsi_3 - Applying v (qwd) to psi_2\n")
print_psi(psi)


# psi_4 - Applying controlled_0_Us to psi_3
psi = apply_gate_to_psi(controlled_0_Us, psi)
print("\npsi_4 - Applying controlled_0_Us to psi_3\n")
print_psi(psi)


# psi_5 - Applying controlled_1_negative_identity to psi_4
psi = apply_gate_to_psi(controlled_1_negative_identity, psi)
print("\npsi_5 - Applying controlled_1_negative_identity to psi\n")
print_psi(psi)


# psi_6 - Applying conjugated transposed of v (qwc) to psi
v = np.conjugate(v)
v = np.transpose(v)
psi = apply_gate_to_psi( apply_tensor(tensor_i, v), psi )
print("\npsi_6 - Applying conjugated transposed of v (qwc) to psi\n")
print_psi(psi)
plot_psi(psi)


# psi_7 - Applying projection_operator to psi_6
psi = apply_gate_to_psi(projection_operator, psi)
print("\npsi_5 - Applying projection_operator to psi\n")
print_psi(psi)
plot_psi(psi)


