digit=0
alpha=0
string=input().strip()
for i in range(len(string)):
    if string[i].isdigit():
        digit+=1
    if string[i].isalpha():
        alpha+=1
print("Số chữ cái:", alpha,"Số chữ số:", digit)