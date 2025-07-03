print(abs.__doc__) 
print(int.__doc__) 
print(input.__doc__)
def nlt(x):
    '''Trả về giá trị bình phương của giá trị x
    x phải là số nguyên'''
    return x**2
x=int(input("Nhập x:"))
print(nlt(x).__doc__)