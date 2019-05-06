'''
Created on May 2, 2019

@author: leonardo
'''
from numpy import pi
from qutip import tensor
from qutip.operators import sigmax, identity
from qutip.qip.circuit import QubitCircuit
from qutip.qip.gates import hadamard_transform, cnot, snot, swap, \
    gate_sequence_product
from qutip.qip.qubits import qubit_states
from qutip.states import basis, fock



print(basis(N=4, n=0))
print("\n")

print(fock(N=4, n=0))
print("\n")

print(qubit_states(N=2, states=[0, 0]))
print("\n")

x = sigmax()
print(x)
print("\n")

ket_zero = qubit_states(N=1, states=[0])

print(ket_zero)
print("\n")

print(x * ket_zero)
print("\n")

print(tensor([identity(N=2), hadamard_transform(N=1)]))
print("\n")

print(snot(N=2, target=1))
print("\n")

print(swap(N=2, targets=[0, 1]))
print("\n")

print(cnot(N=2, control=0, target=1))
print("\n")

print(cnot(N=4, control=0, target=3))
print("\n")

print(hadamard_transform(N=2) * qubit_states(N=2, states=[0, 0]))
print("\n")






qc3 = QubitCircuit(N=3)
qc3.add_gate("CNOT", 1, 0)
qc3.add_gate("RX", 0, None, pi/2, r"\pi/2")
qc3.add_gate("RY", 1, None, pi/2, r"\pi/2")
qc3.add_gate("RZ", 2, None, pi/2, r"\pi/2")
qc3.add_gate("ISWAP", [1, 2])
# qc3.png

print("Gates on qc3")
print(qc3.gates)
print("\n")


unitaries_gates_list = qc3.propagators()
# print("Detailed gates on qc3")
# print(unitaries_gates_list)
# print("\n")

circuit_unitary_gate = gate_sequence_product(U_list=unitaries_gates_list)

print("Gate that represents the circuit qc3")
print(circuit_unitary_gate)
print("\n")

# Resolve (decompose) the circuit gate to another circuit gate
qc4 = qc3.resolve_gates(["CNOT", "RX", "RY", "RZ"])
# qc4.png

# print("propagators")
# print("\n")
# print(qc4.propagators())
# print("\n")


circuit_unitary_gate_qc4 = gate_sequence_product(U_list=qc4.propagators())

print("Gate that represents the circuit qc4")
print(circuit_unitary_gate_qc4)
print("\n")

print("The two circuit gates represent the same quantum operator")
print(circuit_unitary_gate == circuit_unitary_gate_qc4)
print("\n")

print("Type of the circuit gate")
print(type(circuit_unitary_gate))
print("\n")


qc5 = QubitCircuit(N=2,)

qc5.add_state(state=0, targets=[0], state_type='input')
qc5.add_state(state=1, targets=[1], state_type='input')
qc5.add_gate(gate="SWAP", targets=[0, 1], controls=None, arg_value=None, arg_label="SWAP")

print(qc5.input_states)
print("\n")

print(qc5.propagators())
print("\n")

print(gate_sequence_product(U_list=qc5.propagators()))
print("\n")


