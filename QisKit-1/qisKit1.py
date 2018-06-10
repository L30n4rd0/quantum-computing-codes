'''
Created on 3 de jan de 2018
 
@author: leonardo
'''

# Checking the version of PYTHON; we only support > 3.5
import sys
if sys.version_info < (3,5):
    raise Exception('Please use Python version 3.5 or greater.')
       
from qiskit import QuantumProgram
import Qconfig

def printResult(dictionary):
    
    try:
        for item in dictionary.items():
            try:
                item[1].items()
                print('<<' , item[0] , '>>')
                
                printResult(item[1])
                
                print('<<' , item[0] , '>>')
            
            except:
                print(item[0] , ':' , item[1])
                pass
            
    except:
        pass

# Creating Programs create your first QuantumProgram object instance.
qp = QuantumProgram()
   
# Set your API Token
# You can get it from https://quantumexperience.ng.bluemix.net/qx/account,
# looking for "Personal Access Token" section.
QX_TOKEN = Qconfig.APItoken
QX_URL = Qconfig.config['url']
   
# Set up the API and execute the program.
# You need the API Token and the QX URL.
qp.set_api(QX_TOKEN, QX_URL)
   
# find real backends devices that your APIToken has access
# print(qp.online_devices())
   
# Creating Registers create your first Quantum Register called "qr" with 2 qubits
qr = qp.create_quantum_register("qr", 5)
   
# create your first Classical Register called "cr" with 2 bits
cr = qp.create_classical_register("cr", 5)
   
# Creating Circuits create your first Quantum Circuit called "qc" involving your Quantum Register "qr"
# and your Classical Register "cr"
qc = qp.create_circuit('test_circuit', [qr], [cr])
   
# add gates in the circuit
qc.x(qr[0])
# qc.cx(qr[0], qr[1])
# qc.cx(qr[1], qr[2])
# qc.cx(qr[2], qr[3])
# qc.cx(qr[3], qr[4])

# add measure to see the state
qc.measure(qr, cr)
   
QASM_source = qp.get_qasm('test_circuit')
    
print(QASM_source)
   
# Compiled and execute in the local_qasm_simulator
# result = qp.execute(['test_circuit'], backend='local_qasm_simulator', shots=1024)
# result = qp.execute(['test_circuit'], backend='ibmqx5', shots=1024, max_credits=3)
#    
# # Show the results
# print(result)
# printResult(result.get_data('test_circuit'))

dictionary = {'time': 22.825604915618896, 'counts': {'00000': 23, '00001': 11, '00010': 11, '00011': 43, '00100': 4, '00101': 77, '00110': 48, '00111': 807}, 'date': '2018-01-11T14:32:31.238Z'}
printResult(dictionary)
