a=[]
for i in range(2000,3201):
	if i%7==0 and i%5!=0:
		a.append(i)
for i in a:print(i,end=",")