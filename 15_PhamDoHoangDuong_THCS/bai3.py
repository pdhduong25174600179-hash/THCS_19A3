s = input("Nhap chuoi can chuan hoa: ")
ket_qua = ""
co_khoang_trang_truoc = False 
bat_dau = 0
while bat_dau < len(s) and s[bat_dau] == " ":
    bat_dau += 1
ket_thuc = len(s) - 1
while ket_thuc >= 0 and s[ket_thuc] == " ":
    ket_thuc -= 1
for i in range(bat_dau, ket_thuc + 1):
    if s[i] != " ":
        ket_qua += s[i]
        co_khoang_trang_truoc = False
    else:
        if co_khoang_trang_truoc == False: 
            ket_qua += " "
            co_khoang_trang_truoc = True
print("Chuoi da chuan hoa:", ket_qua)