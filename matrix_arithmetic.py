# Jackson Goenawan, 8/23/21

import copy

def scale(scalar, matrix):
  
  scaled = copy.deepcopy(matrix)

  for r in range(len(matrix)): 
    #r starts at 0 and goes until end of matrix (exclusive of last index)
    for c in range(len(matrix[0])):
      scaled[r][c] = scalar * matrix[r][c]
  return(scaled)
    
def add(m1, m2):
  
  r = len(m1)
  c = len(m1[0])
  
  if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
    return("Matrix dimensions do not agree")
    
  else:
    M3 = copy.deepcopy(m1) # alr checked that this has same dimensions as m2
    for i in range(r):
      for j in range(c):
        M3[i][j] = m1[i][j] + m2[i][j]
    return(M3)    

def mult(m1, m2):

  if len(m1[0]) != len(m2):
    return("Matrix dimensions do not agree")

  else:

    r = len(m1)
    c = len(m2[0])
    m = [([0] * len(m2[0])) for i in range(len(m1))]
    
    for i in range(len(m)):
      for j in range(len(m[0])):
        
        numTerms = len(m1[0]) # how many products we need to sum
        for k in range(numTerms):
          m[i][j] += m1[i][k] * m2[k][j] # moving horizontally through m1, moving vertically through m2

    return(m)

def main():

  m1 = [[1, 2, 3], [4, 5, 6]]
  m2 = [[4, 6, 7], [9, 11, 2]]
  m3 = [[4, 7], [10, 3], [8, 2]] # can multiply m1m3 or m2m3
  # m4 = input("enter matrix for determinant calculation"), tough to do matrix input, since we'd have to split by element and then cast each element to int

  print('Matrix 1: ' + str(m1))
  print('Matrix 2: ' + str(m2))
  print('Matrix 3: ' + str(m3))

  print('Scaled matrix 1 by 6: ' + str(scale(6, m1)))

  print('Adding matrices 1 and 2: ' + str(add(m1, m2)))
  print('Adding matrices 1 and 3: ' + str(add(m1, m3))) # should return error

  print('Multiplying matrices 2 and 3: ' + str(mult(m2, m3)))
  print('Multiplying matrices 1 and 2: ' + str(mult(m1, m2))) # should return error

if __name__ == '__main__':
  main()
