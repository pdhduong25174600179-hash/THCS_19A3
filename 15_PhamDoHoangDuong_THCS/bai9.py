n = int(input("Nhap kich thuoc ma tran vuong n: "))
matrix = []
print(f"Nhap {n} dong, moi dong {n} so cach nhau boi khoang trang:")
for i in range(n):
    row_str = input(f"Dong {i+1}: ")
    # Xu ly tach so thu cong
    row = []
    tmp = ""
    for char in row_str + " ":
        if char != " ":
            tmp += char
        elif tmp != "":
            row.append(int(tmp))
            tmp = ""
    matrix.append(row)
tong_cheo_phu = 0
for i in range(n):
    tong_cheo_phu += matrix[i][n - 1 - i]
print("Tong duong cheo phu la:", tong_cheo_phu)