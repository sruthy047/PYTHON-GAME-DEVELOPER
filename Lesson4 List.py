matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)

print(len(matrix))
print(len(matrix[0]))
print(matrix[1][2])

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j],end=" ")
    print("\n")

rows=int(input("Enter the number of rows "))
cols=int(input("Enter the number of columns "))

'''mat=[]
for i in range(rows):
    temp=[]
    for j in range(cols):
        x=int(input("Enter your element - "))
        temp.append(x)
    mat.append(temp)

for i in range(rows):
    for j in range(cols):
        print(mat[i][j],end=" ")
    print("\n")'''

#square matrix

n = int(input("Enter the dimensions of the matrix - "))

for i in range(n):
    temp = []
    for j in range(n):
        x = int(input("Enter your element - "))
        temp.append(x)
    matrix.append(temp)


for i in range(n):
    for j in range(n):
        print(matrix[i][j],end=" ")
    print("\n")


matrixA = [[1,2], [3,4]]
matrixB = [[5,6], [7,8]]

add = [[0,0], [0,0]]
sub = [[0,0], [0,0]]

for i in range(0,2):
    for j in range(0,2):
        add[i][j] = matrixA[i][j] + matrixB[i][j] 
        sub[i][j] = matrixA[i][j] - matrixB[i][j]
      

for i in range(2):
    for j in range(2):
        print(add[i][j], end = " ")
    print("\n")

for i in range(2):
    for j in range(2):
        print(sub[i][j], end = " ")
    print("\n")


#Multiplication

matrixA = [[1,2], [3,4]]
matrixB = [[5,6], [7,8]]

result = [[0,0], [0,0]]

for i in range(0,2):
  for j in range(0,2):
    for k in range(0,2):
      result[i][j] = result[i][j] + (matrixA[i][k] * matrixB[k][j]) 
      
for i in range(2):
    for j in range(2):
        print(result[i][j], end = " ")
    print("\n")