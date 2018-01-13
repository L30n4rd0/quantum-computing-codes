#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 10:28:46 2017

@author: um colega da cadeira de quantica
"""

from sympy.physics.quantum.qubit import Qubit
from sympy.physics.quantum.tensorproduct import TensorProduct
import numpy

def twoXor(qubit):
    
    qubitTemp = Qubit(qubit)
    
    for i in range(numeroBits):
        if( qubitTemp[indiceP + i] == 1 and qubitTemp[indiceU2] == 1 ):
            qubitTemp = qubitTemp.flip(indiceM + i)
    
    return qubitTemp

def notXor(qubit):
    
    qubitTemp = Qubit(qubit)
    
    for i in range(numeroBits):
        if( qubitTemp[indiceP + i] == 1 ):
            qubitTemp = qubitTemp.flip(indiceM + i)
        
        qubitTemp = qubitTemp.flip(indiceM + i)
        
    return qubitTemp

def nXor(qubit):
    
    qubitTemp = Qubit(qubit)
    
    for i in range(numeroBits):
        if( qubitTemp[indiceM + i] == 0):
            return qubitTemp
        
    qubitTemp = qubitTemp.flip(indiceU1)
    
    return qubitTemp

################# Execucao #############################

entrada = ['101', '001', '000']
    
numeroBits = len(entrada[0])
indiceU1 = numeroBits + 1
indiceU2 = numeroBits

indiceP = indiceU1 + 1
indiceM = 0

memoria = ''

for i in range(numeroBits):
    memoria += '0'

qubitInicial = Qubit(entrada[0] + '01' + memoria)

print (qubitInicial)

saida1 = twoXor(qubitInicial)

print (saida1)

saida2 = notXor(saida1)

print (saida2)

saida3 = nXor(saida2)

print (saida3)
