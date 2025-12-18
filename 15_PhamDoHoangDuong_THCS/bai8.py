nhap = input("Nhap day so: ")
k = int(input("Nhap k: "))
lst = []
tmp = ""
for char in nhap + " ":
    if char != " ":
        tmp += char
    elif tmp != "":
        lst.append(int(tmp))
        tmp = ""
n = len(lst)
if n > 0:
    k = k % n 
    ket_qua = [0] * n    
    for i in range(n):
        vi_tri_moi = (i + k) % n
        ket_qua[vi_tri_moi] = lst[i]

    print("List sau khi dich chuyen:", ket_qua)
else:
    print("List rong")