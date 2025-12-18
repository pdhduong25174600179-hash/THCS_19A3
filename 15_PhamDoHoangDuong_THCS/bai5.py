nhap = input("Nhap cac so (cach nhau boi khoang trang): ")
lst = []
tmp = ""
for char in nhap + " ":
    if ('0' <= char <= '9') or (char == '-'):
        tmp += char
    else:
        if tmp != "":
            lst.append(int(tmp)) 
            tmp = ""
ket_qua = []
for x in lst:
    da_ton_tai = False
    for item in ket_qua:
        if item == x:
            da_ton_tai = True
            break
    if da_ton_tai == False:
        ket_qua.append(x)
print("List sau khi xoa trung:", ket_qua)