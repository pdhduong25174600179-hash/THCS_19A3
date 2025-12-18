s1 = input("Nhap cac phan tu Set A (cach nhau boi khoang trang): ")
list_a = []
tmp = ""
for char in s1 + " ":
    if ('0' <= char <= '9') or (char == '-'): tmp += char
    elif tmp != "": 
        val = int(tmp)
        da_co = False
        for x in list_a: 
            if x == val: da_co = True
        if not da_co: list_a.append(val)
        tmp = ""
s2 = input("Nhap cac phan tu Set B: ")
list_b = []
tmp = ""
for char in s2 + " ":
    if ('0' <= char <= '9') or (char == '-'): tmp += char
    elif tmp != "": 
        val = int(tmp)
        da_co = False
        for x in list_b: 
            if x == val: da_co = True
        if not da_co: list_b.append(val)
        tmp = ""
a_tru_b = [] 
b_tru_a = [] 
giao = []    
for x in list_a:
    nam_trong_b = False
    for y in list_b:
        if x == y:
            nam_trong_b = True
            break   
    if nam_trong_b:
        giao.append(x)
    else:
        a_tru_b.append(x)
for x in list_b:
    nam_trong_a = False
    for y in list_a:
        if x == y:
            nam_trong_a = True
            break
    if not nam_trong_a:
        b_tru_a.append(x)
print("A nhung khong thuoc B:", a_tru_b)
print("B nhung khong thuoc A:", b_tru_a)
print("Giao cua hai set:", giao)