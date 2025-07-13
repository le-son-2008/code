def binary_to_decimal(binary_str):
    return int(binary_str, 2) #2 là cơ số của hệ nhị phân
out=[]
inp=input("Chuỗi nhị phân:").split(",")
for binary in inp:
    decimal = binary_to_decimal(binary.strip()) #.strip() để loại bỏ khoảng trắng
    if decimal % 5 == 0:
        out.append(binary.strip())
print(",".join(out))