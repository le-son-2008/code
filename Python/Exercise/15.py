a=[]
for i in range(1000,3001):
    y=str(i)
    if  int(y[0]) % 2 == 0 and int(y[1]) % 2 == 0 and int(y[2]) % 2 == 0 and int(y[3]) % 2 == 0:
        a.append(str(i))   
print(",".join(a))