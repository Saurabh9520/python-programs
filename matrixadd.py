print("Addition of matrix======================")
x=[[12,7,3],[4,5,6],[7,8,9]]
y=[[12,7,3],[4,5,6],[7,8,9]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j]=x[i][j]+y[i][j]
for r in result:
    print(r)
print("=================================================multiplication of matrix")

x=[[12,7,3],[4,5,6],[7,8,9]]
y=[[5,8,1,2],[6,7,3,0],[4,5,9,1]]
result=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j]+=x[i][k]*y[k][j]
            
        
for r in result:
    print(r)
print()
print("transpose of matrix=========row to col==============")
print()
#Original Matrix
import numpy
#Original Matrix
x = [[1,2],[3,4],[5,6]]
print(numpy.transpose(x))


