print("--- Nhap Ma Tran A ---")
m = int(input("So dong cua A: "))
n = int(input("So cot cua A: "))
matrix_a = []
for i in range(m):
    s = input(f"A - Hang {i+1}: ")
    row = []
    tmp = ""
    for char in s + " ":
        if ('0' <= char <= '9') or (char == '-'): tmp += char
        elif tmp != "": row.append(int(tmp)); tmp = ""
    matrix_a.append(row)
print("--- Nhap Ma Tran B ---")
n_b = int(input("So dong cua B: "))
p = int(input("So cot cua B: "))
matrix_b = []
for i in range(n_b):
    s = input(f"B - Hang {i+1}: ")
    row = []
    tmp = ""
    for char in s + " ":
        if ('0' <= char <= '9') or (char == '-'): tmp += char
        elif tmp != "": row.append(int(tmp)); tmp = ""
    matrix_b.append(row)
if n != n_b:
    print("Khong the nhan ma tran (Cot cua A phai bang Dong cua B).")
else:
    matrix_c = []
    for i in range(m):
        dong_tam = []
        for j in range(p):
            dong_tam.append(0)
        matrix_c.append(dong_tam)
    for i in range(m):      
        for j in range(p):   
            tong_con = 0
            for k in range(n): 
                tong_con += matrix_a[i][k] * matrix_b[k][j]
            matrix_c[i][j] = tong_con
    print("Ma tran ket qua C:")
    for row in matrix_c:
        print(row)