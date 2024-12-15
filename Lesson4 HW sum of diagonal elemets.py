n = int(input("Enter the dimensions of the matrix - "))
matrix=[]
for i in range(n):
    temp = []
    for j in range(n):
        x = int(input("Enter your element - "))
        temp.append(x)
    matrix.append(temp)

sum=0   
for i in range(n):
    for j in range(n):
        if(i==j):
            sum+=matrix[i][j]
        print(matrix[i][j],end=" ")
    print("\n")
print("\n Sum of diagonal elements- ",sum)
print("\n\n")
l1=[]
l2=[]
l3=[]
for i in range(20):
    m=int(input("\nEnter the mark of student "))
    if m<=30:
        l1.append(m)
    elif m>30 and m<=69:
        l2.append(m)
    else:
        l3.append(m)
print("List of marks ")
print(l1)
print(l2)
print(l3)