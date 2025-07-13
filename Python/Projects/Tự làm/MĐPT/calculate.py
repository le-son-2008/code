from math import e
from random import choice
import sqlite3

from numpy import add

conn = sqlite3.connect("C:\\Users\\Administrator\\OneDrive\\Desktop\\Code\\Python\\Projects\\Tự làm\\MĐPT\\phan_tan.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS phan_tan (
        value TEXT PRIMARY KEY,
        frequency INTEGER NOT NULL
    )
''')
conn.commit()

cursor.execute("SELECT * FROM phan_tan")

# Thêm dữ liệu
def add_value(n,value):
    lst=value.split(",")
    i=0
    for _ in range(n):
        value_fixed= str(float(lst[0])+i) + "," + str(float(lst[1])+ i)
        i += size(value)
        frequency = input("Nhập tần số của giá trị "+ value_fixed+" này: ")
        try:
            cursor.execute("INSERT INTO phan_tan (value, frequency) VALUES (?, ?)", (value_fixed, frequency))
            conn.commit()
            print("✅ Thêm thành công!")
        except sqlite3.IntegrityError:
            print("❌ Lỗi khi thêm dữ liệu!")

# Xem
def show_table():
    n = cursor.fetchall()
    if not n:
        print("\nBảng rỗng!")
        return
    else:
        print("\n--- Bảng số liệu ---")
        print("Giá trị\t\tTần số")
        cursor.execute("SELECT * FROM phan_tan")
        for row in n: # Lấy tất cả các giá trị
            value = row[0]
            frequency = row[1]
            print(f"{value}\t\t{frequency}")

# Xóa 
def delete_value():
    choice = input("Bạn có chắc chắn muốn xóa toàn bộ bảng số liệu không? (y/n): ")
    if choice.lower() != 'y':
        print("❌ Hủy xóa bảng số liệu!")
        return
    else:
        cursor.execute("Delete from phan_tan")
        conn.commit()
        print("✅ Xóa thành công!")

# Tính toán
def size(text):
    lst=text.split(",")
    s=float(lst[1])-float(lst[0])
    return s

def so_dai_dien(x,y):
    return (x+y)/2

def khoang_bien_thien(n,value):
    lst=value.split(",")
    i=0
    min_value = float(lst[0])
    max_value = 0
    for _ in range(n):
        max_value = float(lst[1]) + i
        i += size(value)
    return max_value - min_value

#def khoang_tu_phan_vi(n):

def menu():
    while True:
        print("\n--- Bảng số liệu ---")
        print("1. Thêm giá trị")
        print("2. Xem bảng số liệu")
        print("3. Xóa bảng số liệu")
        print("4. Tính toán mức độ phân tán")
        print("0. Thoát")
        choice = input("Chọn: ")

        if choice == '1':
            add_value(int(input("Nhập số lượng giá trị cần thêm: ")), input("Nhập giá trị (dạng 'a,b'): "))
        elif choice == '2':
            show_table()
        elif choice == '3':
            delete_value()
        elif choice == '4':
            print("\nTính toán mức độ phân tán:")
            cursor.execute("SELECT * FROM phan_tan")
            rows = cursor.fetchall()
            n = len(rows)
            if n > 0:
                value = rows[0][0]# Lấy giá trị đầu tiên
            else:
                print("Bảng rỗng!")
                continue
            print("Khoảng biến thiên: ", khoang_bien_thien(n, value))
        elif choice == '0':
            break
        else:
            print("❌ Lựa chọn không hợp lệ.")

menu()
conn.close()