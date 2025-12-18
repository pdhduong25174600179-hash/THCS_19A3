s = input("Nhap Sanpham:Gia (vd: Ao:40 Quan:60 Mu:55): ")

kho_hang = {}
tmp_key = ""
tmp_val = ""
dang_doc_key = True

for char in s + " ":
    if char == ":":
        dang_doc_key = False
    elif char == " ":
        if tmp_key != "" and tmp_val != "":
            kho_hang[tmp_key] = int(tmp_val)
        tmp_key = ""; tmp_val = ""; dang_doc_key = True
    else:
        if dang_doc_key: tmp_key += char
        else: 
            if ('0' <= char <= '9'): tmp_val += char

print("Du lieu goc:", kho_hang)

ket_qua_loc = {}
nguong_loc = 50

for san_pham in kho_hang:
    gia = kho_hang[san_pham]
    
    if gia > nguong_loc:
        ket_qua_loc[san_pham] = gia

print(f"Cac san pham co gia > {nguong_loc}:", ket_qua_loc)