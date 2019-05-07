'''
Created on Apr 15, 2019

@author: leonardo
'''
from qiskit.providers.ibmq import IBMQ
from Qconfig import APItoken
from utils import print_job_execution_information

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
Selecting backend of available devices.
"""
print("\nGetting backend ...")
backend_ibmq = IBMQ.get_backend('ibmqx2')


"""
Retrieving job by id
"""
job_ibmq = backend_ibmq.retrieve_job('5cd1ddff14ff4f0072e57815')


"""
Getting execution information
"""
print_job_execution_information(job_ibmq)

