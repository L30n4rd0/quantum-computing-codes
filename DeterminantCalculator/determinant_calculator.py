'''
Created on 4 de out de 2017

@author: leonardo
'''
from click._compat import raw_input

class DeterminantCalculator(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
    
    def printMatrix(self, currentMatrix):
        '''
        Show the matrix on the console.
        
        Inputs:
        any matrix
        
        Return: void
        '''
        
        for index in range(len(currentMatrix)):
            print (currentMatrix[index])
    
    def calculate(self, matrix):
        '''
        Calculate the determinant value of square matrix received as a parameter.
        
        Inputs:
        any square matrix
        
        Return: matrix's determinant value
        '''
        
        # Matrix dimension = 1
        if (len(matrix) == 1):
            return matrix[0][0]
        
        # Matrix dimension = 2
        elif (len(matrix) == 2):
            self.printMatrix(matrix)
            determinant = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

            return determinant
        
        # Matrix dimension > 2
        else:
            determinant = 0
            
            # Increments first row matrix
            for current_column in range(len(matrix)):
                # Matrix temp: remaining values
                matrix_temp = []
                
                # Filling the matrix temp
                for row in range(1, len(matrix)):
                    row_temp = []
                    
                    for column in range(len(matrix)):
                        if (column != current_column):
                            row_temp.append(matrix[row][column])
                        
                    matrix_temp.append(row_temp)
                
                # Calculate the determinant by La Place theorem
                determinant += ((-1) ** (1 + current_column + 1)) * matrix[0][current_column] * self.calculate(matrix_temp)
                        
            return determinant
            
        
    def init_matrix(self):
        '''
        Get user input data and fill the matrix. 
        
        Inputs:
        
        Return: matrix filled
        '''
        
        matrix_dimension = int( raw_input("Digite a dimensao da matrix: ") )
        
        matrix = [[0 for x in range(matrix_dimension)] for y in range(matrix_dimension)]
        
        for index in range(matrix_dimension):
            matrix_row = raw_input("Digite os valores da linha %d da matriz separados por espaco:\nExemplo: 7 2 3\n" % (index +1))
            matrix[index] = map(int, matrix_row.split(' '))
            
        return matrix;
    
calculator = DeterminantCalculator()

matrix = calculator.init_matrix()
determinant = calculator.calculate(matrix)

print ("Matriz inserida")
calculator.printMatrix(matrix)

print ("\nDeterminante: ", determinant)
