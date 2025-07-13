upper=0
lower=0
sring=input()
for i in range(len(sring)):
    if sring[i].isupper():
        upper+=1
    if sring[i].islower():
        lower+=1
print("Chữ hoa:", upper, "\nChữ thường:", lower)