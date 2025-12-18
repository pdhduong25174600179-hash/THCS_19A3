n = int(input("Nhap kich thuoc ma tran vuong n: "))
matrix = []
print("Nhap tung hang (cac so cach nhau boi dau cach):")
for i in range(n):
    s = input(f"Hang {i+1}: ")
    row = []
    tmp = ""
    for char in s + " ":
        if ('0' <= char <= '9') or (char == '-'):
            tmp += char
        elif tmp != "":
            row.append(int(tmp))
            tmp = ""
    matrix.append(row)
la_doi_xung = True
for i in range(n):
    for j in range(i + 1, n): 
        if matrix[i][j] != matrix[j][i]:
            la_doi_xung = False
            break
    if la_doi_xung == False:
        break
if la_doi_xung:
    print("Day la ma tran doi xung.")
else:
    print("Day KHONG phai ma tran doi xung.")