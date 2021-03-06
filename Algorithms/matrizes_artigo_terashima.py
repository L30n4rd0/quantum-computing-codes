'''
Created on Jun 7, 2018

@author: leonardo
'''

import numpy as np
from utils.gates import i, x, y, z, h, f
from utils.qbits import qubit_zero, qubit_one
from utils.operations import apply_tensor, apply_n_tensor_to, apply_gate_to_psi, print_psi
from numpy import float, sqrt

c = 0.85

# variáveis usadas no exemplo da porta NAND
a = np.sqrt(1 - c**2)
b = np.sqrt( 1 - ((c**2)/3) )
q = a - 0.1

# equação 22 no artigo
n = np.array(
        [[0, 0, 0, 1/sqrt(3)],
         [0, 0, 0, 0],
         [1/sqrt(3), 1/sqrt(3), 1/sqrt(3), 0],
         [0, 0, 0, 0]],
        dtype=complex
    )

# m_0 = c * n
m_0 = c * n

# equação 24 no artigo
m_1 = np.array(
        [[2 + a, -1 + a, -1 + a, 0],
         [-1 + a, 2 + a, -1 + a, 0],
         [-1 + a, -1 + a, 2 + a, 0],
         [0, 0, 0, 3 * b]],
        dtype=complex
    )

m_1 = (1/3) * m_1

# equação 27 no artigo
r_0 = np.array(
        [[1 + (2 * a), 1 - a, 1 - a, 0],
         [1 - a, 1 + (2 * a), 1 - a, 0],
         [1 - a, 1 - a, 1 + (2 * a), 0],
         [0, 0, 0, (3 * a) / b]],
        dtype=complex
    )

r_0 = (q / (3 * a)) * r_0

def aplicar_medicao(operador_n, psi):
    # Aplicação do operador de medição
    # M|psi> = (n * |psi>) / sqrt(<psi| * ((n_t * n) * |psi>))
    
    # (n * |psi>)
    resultado = apply_gate_to_psi(operador_n, psi)
    
    # (n_t * n)
    projetor_n = np.dot(np.transpose(operador_n), operador_n)

    # ((n_t * n) * |psi>)    
    normalizador = np.dot(projetor_n, psi)
    
    psi_t = np.transpose(psi)
    
    # <psi| * ((n_t * n) * |psi>)
    normalizador = np.dot(psi_t, normalizador)
    
    # sqrt(<psi| * ((n_t * n) * |psi>))
    normalizador = sqrt(normalizador)
    
    # (n * |psi>) / sqrt(<psi| * ((n_t * n) * |psi>))
    resultado = (1 / normalizador[0][0]) * resultado
    
    return resultado

if __name__ == '__main__':
    # verificando a propriedade (r_0 * m_1 = q * identidade) 
    # destacada no exemplo da porta NAND no artigo de Terashima 
    # no parágrafo logo após a equação 27
#     print('\nr_0 * m_1 = \n', np.dot(r_0, m_1))
#     print('\nq = ', q)

    # criando m_1 pela fórmula: m_1 = sqrt(i - (m_0_t * m_0))
     
    # (m_0_t * m_0)
    projetor_m_0 = np.dot(np.transpose(m_0), m_0)
     
    # tensor da identidade
    identity_tensor = i = np.identity(4, dtype=complex)
     
    # i - (m_0_t * m_0)
    temp = identity_tensor - projetor_m_0
     
    # sqrt(i - (m_0_t * m_0))
    m_1_gerado = sqrt(temp)
     
    print('\ntemp\n', temp)
    print('\nm_1_gerado\n', m_1_gerado)
    print('\nm_1\n', m_1)
    print('\nm_0\n', m_0)
    
    # calculando a probabilidade de sucesso para xx -> {|00>, |01>, |10>, |11>}
    # para porta NAND
    psi = np.array(
        [[1],
         [0],
         [0],
         [0]]
    )
    
    projetor_m_0 = np.dot(np.transpose(m_0), m_0)
      
    psi_t = np.transpose(psi)
      
    probabilidade = np.dot(projetor_m_0, psi)
      
    probabilidade = np.dot(psi_t, probabilidade)
      
    print('\nProbabilidade de sucesso de criação da porta não unitária:\n', probabilidade)
      
    # psi inicial
    print('\npsi inicial:\n', psi)
  
    # Aplicando medição m_0 em psi
    print('\nAplicando o operador de medição m_0 em: psi:\n', aplicar_medicao(m_0, psi))
      
    # Aplicando medição m_1 em psi
    psi = aplicar_medicao(m_1, psi)
    print('\nAplicando o operador de medição m_1 em: psi:\n', psi)
      
    # Aplicando medição r_0 em m_1|psi>
    psi = aplicar_medicao(r_0, psi)
    print('\nAplicando o operador de medição r_0 em: m_1|psi>:\n', psi)
      
    # Aplicando medição m_0 em r_0 m_1 |psi>
    psi = aplicar_medicao(m_0, psi)
    print('\nAplicando o operador de medição m_0 em: r_0 m_1|psi>:\n', psi)

    
    