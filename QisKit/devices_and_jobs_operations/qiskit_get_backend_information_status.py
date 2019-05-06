'''
Created on Oct 2, 2018

@author: leonardo
'''

# Import Qiskit Terra
from qiskit import IBMQ
from Qconfig import APItoken
from utils import list_backend_information_status



"""
Set your API Token.
You can get it from https://quantumexperience.ng.bluemix.net/qx/account,
looking for "Personal Access Token" section.
"""
QX_TOKEN = APItoken




"""
Authenticate with the IBM Q API in order to use online devices.
You need the API Token.
The account information is need to be stored locally on disk only once.
To store account information locally on disk, uncomment the next line.
"""
# print("Storing account information locally on disk ...")
# IBMQ.save_account(QX_TOKEN)

# The next line is mandatory to load the account infos stored
print("\nLoading account ...")
IBMQ.load_accounts()
# print_dict(IBMQ.stored_accounts()[0])




""" 
See a list of available devices.
"""
# print("\nIBMQ backends: ")
# print_list(IBMQ.backends())

# List of available devices beckend
# ibmqx4
# ibmqx2
# ibmq_16_melbourne
# ibmq_qasm_simulator


"""
Selecting backend of available devices.
"""
print("\nGetting backend ...")
backend_ibmq = IBMQ.get_backend('ibmqx2')



"""
Getting information of the selected backend
"""
list_backend_information_status(backend_ibmq)


