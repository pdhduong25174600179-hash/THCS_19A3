r = int(input("Nhap so dong: "))
c = int(input("Nhap so cot: "))
matrix = []
print("Nhap ma tran:")
for i in range(r):
    s = input(f"Hang {i+1}: ")
    row = []
    tmp = ""
    for char in s + " ":
        if ('0' <= char <= '9') or (char == '-'): tmp += char
        elif tmp != "": row.append(int(tmp)); tmp = ""
    matrix.append(row)
is_identity = True
if r != c:
    is_identity = False
else:
    for i in range(r):
        for j in range(c):
            if i == j:
                if matrix[i][j] != 1:
                    is_identity = False
                    break
            else:
                if matrix[i][j] != 0:
                    is_identity = False
                    break
        if is_identity == False:
            break
if is_identity:
    print("Day LA ma tran don vi.")
else:
    print("Day KHONG phai ma tran don vi.")