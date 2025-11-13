ten_dang_nhap = input("Nhập tên đăng nhập: ")
mat_khau = input("Nhập mật khẩu: ")
if ten_dang_nhap == "admin" and mat_khau != "password123":
    print("Kiểm tra quyền truy cập: CÓ QUYỀN")
else:
    print("Kiểm tra quyền truy cập: KHÔNG CÓ QUYỀN")
