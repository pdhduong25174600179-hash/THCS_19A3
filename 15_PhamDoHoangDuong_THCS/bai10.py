def nhap_dong_ma_tran(thu_tu_dong):
    s = input(f"Nhap cac so hang {thu_tu_dong} (cach nhau boi khoang trang): ")
    lst = []
    tmp = ""
    for char in s + " ":
        if ('0' <= char <= '9') or (char == '-'):
            tmp += char
        elif tmp != "":
            lst.append(int(tmp))
            tmp = ""
    return lst
m = int(input("Nhap so dong m: "))
n = int(input("Nhap so cot n: "))
matrix = []
for i in range(m):
    row = nhap_dong_ma_tran(i + 1)
    while len(row) < n: row.append(0)
    if len(row) > n: row = row[:n] 
    matrix.append(row)
max_sum = -999999999 
hang_max_index = -1
for i in range(m):
    tong_hang = 0
    for x in matrix[i]:
        tong_hang += x
    if tong_hang > max_sum:
        max_sum = tong_hang
        hang_max_index = i

print(f"Hang co tong lon nhat la hang {hang_max_index + 1} voi tong la: {max_sum}")
print("Noi dung hang:", matrix[hang_max_index])