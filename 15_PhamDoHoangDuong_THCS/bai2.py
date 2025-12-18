s = input("Nhap chuoi: ")
n = int(input("Nhap so n: "))
tu_hien_tai = ""
danh_sach_tu = []
s_temp = s + " "
for char in s_temp:
    if char != " ":
        tu_hien_tai += char
    else:
        if len(tu_hien_tai) > n:
            print(tu_hien_tai)
        tu_hien_tai = ""