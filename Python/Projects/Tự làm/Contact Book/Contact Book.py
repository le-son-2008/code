from calendar import c
import re
import sqlite3

# 1. Kết nối và tạo bảng nếu chưa có
conn = sqlite3.connect("C:\\Users\\Administrator\\OneDrive\\Desktop\\Code\\Python\\Projects\\Tự làm\\Contact Book\\contacts.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        address TEXT,
        phone TEXT NOT NULL UNIQUE,
        email TEXT
    )
''')
conn.commit()

# 2. Thêm liên hệ
def add_contact(name, address, phone, email):
    try:
        cursor.execute("INSERT INTO contacts (name, address, phone, email) VALUES (?, ?, ?, ?)", (name, address, phone, email))
        conn.commit()
        print("✅ Thêm liên hệ thành công!")
    except sqlite3.IntegrityError:
        print("❌ Số điện thoại đã tồn tại!")

# 3. Hiển thị danh bạ
def show_contacts():
    cursor.execute("SELECT * FROM contacts")
    for row in cursor.fetchall(): # Lấy tất cả các liên hệ
        print(row)

# 4. Chỉnh sửa liên hệ
def edit_contact(name=None, phone=None, email=None, address=None):
    print("\n⚙️Tìm kiếm liên hệ để chỉnh sửa.")
    print("Có thể bỏ qua các trường không muốn tìm kiếm.")
    name = input("Tên cần tìm: ")
    phone = input("Số điện thoại cần tìm: ")
    email = input("Email cần tìm: ")
    address = input("Địa chỉ cần tìm: ")
    if name:
        cursor.execute("SELECT * FROM contacts WHERE name LIKE ?", ('%' + name + '%',))
        results = cursor.fetchall()
    if phone:
        cursor.execute("SELECT * FROM contacts WHERE phone = ?", (phone,))
        results = cursor.fetchall()
    if email:
        cursor.execute("SELECT * FROM contacts WHERE email LIKE ?", ('%' + email + '%',))
        results = cursor.fetchall()
    if address:
        cursor.execute("SELECT * FROM contacts WHERE address LIKE ?", ('%' + address + '%',))
        results = cursor.fetchall()
    if not name and not phone and not email and not address:
        print("❌ Vui lòng cung cấp ít nhất một tiêu chí tìm kiếm.")
        return
    if results:
        print("\n🔎 Có kết quả tìm kiếm!")
        for row in results:
            print(row)
        print("\nBạn muốn chỉnh sửa gì?" )
        choice = input("1: Xóa, 2: Cập nhật, 0: Quay lại: ")
        if choice == 1: delete_contact(results)
        if choice == 2: update_contact(input("Nhập SĐT cần cập nhật: "), input("Tên mới (bỏ qua nếu không muốn thay đổi): "), input("Địa chỉ mới (bỏ qua nếu không muốn thay đổi): "), input("Email mới (bỏ qua nếu không muốn thay đổi): "))
        if choice == 0: return
    else:
        print("❌ Không tìm thấy liên hệ.")
    
# 5. Xoá liên hệ
def delete_contact(results):
    n=len(results)
    print(n)
    if n == 1:
        print("⚠️ Bạn có chắc muốn xoá liên hệ này không? (Y)")
        confirm = input().strip().upper()
        if confirm == 'Y':
            cursor.execute("DELETE FROM contacts WHERE id = ?", (results[0][0],))
            if cursor.rowcount > 0:
                print("✅ Xoá liên hệ thành công!")
                conn.commit()
        if confirm != 'Y':
            print("❌ Hủy xoá liên hệ.")
            return
    if n > 1:
        print("Bạn muốn xoá liên hệ nào trong số này?")
        temp = input("Xóa theo (cần nhập chính xác) cái gì? (1: Tên, 2: SĐT, 3: Email, 4: Địa chỉ): ")
        if temp == '1':
            name = input("Nhập tên cần xoá: ")
            cursor.execute("DELETE FROM contacts WHERE name = ?", (name,))
        if temp == '2':
            phone = input("Nhập SĐT cần xoá: ")
            cursor.execute("DELETE FROM contacts WHERE phone = ?", (phone,))
        if temp == '3':
            email = input("Nhập email cần xoá: ")
            cursor.execute("DELETE FROM contacts WHERE email = ?", (email,))
        if temp == '4':
            address = input("Nhập địa chỉ cần xoá: ")
            cursor.execute("DELETE FROM contacts WHERE address = ?", (address,))
        if cursor.rowcount > 0: # Kiểm tra xem có liên hệ nào bị xoá không
            conn.commit()
            print("✅ Xoá liên hệ thành công!")
        else:
            print("❌ Không tìm thấy liên hệ để xoá.")

# 6. Cập nhật liên hệ
def update_contact(phone, name=None, address=None, email=None):

    updates = []
    params = []

    if name:
        updates.append("name = ?")
        params.append(name)
    if address:
        updates.append("address = ?")
        params.append(address)
    if email:
        updates.append("email = ?")
        params.append(email)

    if not updates:
        print("❌ Không có thông tin nào để cập nhật.")
        return

    params.append(phone)
    cursor.execute(f"UPDATE contacts SET {', '.join(updates)} WHERE phone = ?", params)
    
    if cursor.rowcount > 0:
        conn.commit()
        print("✅ Cập nhật liên hệ thành công!")
    else:
        print("❌ Không tìm thấy liên hệ để cập nhật.")

# 7. Menu đơn giản
def menu():
    while True:
        print("\n--- DANH BẠ ---")
        print("1. Thêm liên hệ")
        print("2. Xem danh bạ")
        print("3. Chỉnh sửa liên hệ")
        print("0. Thoát")
        choice = input("Chọn: ")

        if choice == '1':
            add_contact(input("Tên: "),input("Địa chỉ:"), input("SĐT: "), input("Email: "))
        elif choice == '2':
            show_contacts()
        elif choice == '3':
            edit_contact()
        elif choice == '0':
            break
        else:
            print("❌ Lựa chọn không hợp lệ.")

menu()
conn.close()