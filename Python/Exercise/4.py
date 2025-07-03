a=input("Nhập dãy số cách nhau bởi dấu phẩy:")
b=[]
for i in a.split(","):
	b.append(i)
print(b)
print(tuple(b))