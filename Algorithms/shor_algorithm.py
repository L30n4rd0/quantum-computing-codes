# -*- coding: utf-8 -*-
"""
    Universidade Federal Rural de Pernambuco - UFRPE
    Disciplina de Introdução à Computação Quântica

    Algoritmo de Shor

    Por Israel Ferraz de Araújo.

    Input
    =====

    N : int
        Número inteiro que será fatorado.

    Output
    ======

    answer : tuple of int
        Fatores de N, primos entre si.

"""
import math
import random

from sympy import Mul, S
from sympy import log, sqrt
from sympy.core.numbers import igcd

from sympy.physics.quantum.gate import Gate, HadamardGate
from sympy.physics.quantum.qubit import Qubit, IntQubit, measure_partial_oneshot, measure_partial, measure_all_oneshot
from sympy.physics.quantum.qapply import qapply
from sympy.physics.quantum.qft import IQFT, QFT
from sympy.physics.quantum.qexpr import QuantumError


class Vx(Gate):
    """

    Porta Vx definida no artigo de Portugal.

    """

    @classmethod
    def _eval_args(cls, args):
        if len(args) != 4:
            raise QuantumError(
                'Insufficient/excessive arguments to Vx.'
            )
        return args

    @property
    def n(self):
        """"""
        return self.label[0]

    @property
    def t(self):
        """"""
        return self.label[1]

    @property
    def x(self):
        """"""
        return self.label[2]

    @property
    def N(self):
        """"""
        return self.label[3]

    def _apply_operator_Qubit(self, qubits, **options):
        """

        Calcula Vx da segunda metade do registrador e armazena na
        primeira metade

        """

        a = 1
        j = 0
        # Determina o valor de j no segundo registrador.
        for i in range(self.t):
            j = j + a * qubits[self.n + i]
            a = a * 2

        # Calcula o valor que será armazenado no primeiro registrador.
        value = int(self.x ** j % self.N)

        primeiro = Qubit(IntQubit(value, self.n))

        array = list(qubits[k] for k in reversed(range(self.n, self.n + self.t)))
        for i in reversed(range(self.n)):
            array.append(primeiro[i])

        #print Qubit(*array), self.x, j, value

        return Qubit(*array)

        #return Qubit(IntQubit(out, 2 * self.n))

def continued_fraction(x, y):
    """

    Retorna uma lista com os termos da fração continuada

    """
    #print ("x: ", x
    #print ("y: ", y
    x = int(x)
    y = int(y)
    temp = x//y
    if temp * y == x:
        return [temp,]

    list = continued_fraction(y, x - temp * y)
    list.insert(0, temp)
    return list

def find_r(x, N):
    """

    Encontra o período de x em aritimética módulo N.
    Essa é a parte realmente quântica da solução.

    Põe a primeira parte do registrador em um estado de superposição |j> |0>,
    com j = 0 to 2 ** n - 1, usando a porta Hadamard.
    Depois aplica a porta Vx e IQFT para determinar a ordem de x.

    """

    # Calcula o número de qubits necessários
    n = int(math.ceil(log(N, 2)))
    t = int(math.ceil(2 * log(N, 2)))

    print ("n: ", n)
    print ("t: ", t)

    # Cria o registrador
    register = Qubit(IntQubit(0, t + n))
    print ("register: ", register)

    # Põe a segunda metade do registrado em superposição |1>|0> + |2>|0> + ... |j>|0> + ... + |2 ** n - 1>|0>
    print ("Aplicando Hadamard...")
    circuit = 1
    for i in reversed(list(range(n, n + t))):
        circuit = HadamardGate(i) * circuit
    circuit = qapply(circuit * register)
    print ("Circuit Hadamard:\n", circuit.simplify())

    # Calcula os valores para a primeira metade do registrador |1>|x ** 1 % N> + |2>|x ** 2 % N> + ... + |k>|x ** k % N >+ ... + |2 ** n - 1 = j>|x ** j % N>
    print ("Aplicando Vx...")
    circuit = qapply(Vx(n, t, x, N) * circuit)
    print ("Circuit Vx:\n", circuit.simplify())

    # Faz a medição da primeira metade do registrador obtendo um dos [x ** j % N's]
    print ("Medindo 0->n ...")
    circuit = measure_partial_oneshot(circuit, range(n))
    print ("Circuit 0->n:\n", circuit.simplify())

    # Aplica a Transformada de Fourier Quântica Inversa na segunda metade do registrador
    print ("Aplicando a transformada inversa...")
    circuit = qapply(IQFT(n, n + t).decompose() * circuit)
    print ("Circuit IQFT:\n", circuit.simplify())

    # Faz a medição da segunda metade do registrador um dos valores da transformada

    while (True): # O correto seria repetir a rotina inteira, mas é suficiente repetir a medição.
                  # Num computador quântico real o estado colapsaria e não seria possível medi-lo novamente.
        print ("Medindo n->n+t ...")

        #measurement = measure_partial_oneshot(circuit, range(n, n + t))
        measurement = measure_all_oneshot(circuit)

        print (measurement.simplify())

        if isinstance(measurement, Qubit):
            register = measurement
        elif isinstance(measurement, Mul):
            register = measurement.args[-1]
        else:
            register = measurement.args[-1].args[-1]

        print ("Medicao: ", register)

        # Converte o qubit de binário para decimal
        k = 1
        answer = 0
        for i in range(t):
            answer += k * register[n + i]
            k = k << 1

        print ("Medicao: ", answer)

        if answer != 0:
            break

    print ("2^t: ", 2 ** t)
    # Lista os termos da fração continuada
    fraction = continued_fraction(answer, 2 ** t)

    # A soma dos termos da fração continuada é a razão entre dois
    # números primos entre si (p e q onde MDC(p, q) == 1) que
    # multiplicados resultam N (somar apenas os termos menores ou iguais a N)
    r = 0
    for x in fraction:
        if (x > N):
            break
        else:
            print ("fraction: ", x)
            r = r + x

    return r

def Shor(N):
    """

    Algoritmo de Shor.

    """
    print ("N= ", N)

    while (True):
        # Armazena um número aleatório menor que N
        x = random.randrange(N - 2) + 2
        # x = 2 # teste
        print ("x= ", x)

        # Se não é coprimo com N
        if igcd(N, x) != 1:
            print ("nao eh coprimo! MDC(N, x) != 1!")
            return igcd(N, x) # O resultado da fatoração é apenas o MDC de N e x

        # Encontra o período r
        print ("calculando o periodo...")
        r = find_r(x, N)

        print ("r= ", r)

        # Se r não é par
        if r % 2 == 1:
            print ("r nao eh par, reiniciando...")
        else:
            break

    # Como r é par, podemos calcular os fatores
    answer = (igcd(x ** (r/2) - 1, N), igcd(x ** (r/2) + 1, N))

    return answer

def main():
    N = 15
    while (N > 0):
        N = int(input("Informe o valor de N:"))
        print (Shor(N), "\n\n")

if __name__ == "__main__":
    main()
