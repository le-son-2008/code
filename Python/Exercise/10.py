xy_input=input("X,Y=").split(',')
x=int(xy_input[0])
y=int(xy_input[1])
array=[[0 for _ in range(y)] for _ in range(x)]
for i in range(x):
    for j in range(y):
        array[i][j]=i*j
print(array)