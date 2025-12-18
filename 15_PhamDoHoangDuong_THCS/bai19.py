s = input("Nhap Ten:Diem (vd: An:8 Binh:9 Chi:8): ")
bang_diem = {}
tmp_key = ""
tmp_val = ""
dang_doc_key = True
for char in s + " ":
    if char == ":":
        dang_doc_key = False
    elif char == " ":
        if tmp_key != "" and tmp_val != "":
            bang_diem[tmp_key] = int(tmp_val)
        tmp_key = ""; tmp_val = ""; dang_doc_key = True
    else:
        if dang_doc_key: tmp_key += char
        else: 
            if ('0' <= char <= '9'): tmp_val += char
print("Bang diem goc:", bang_diem)
grouped_dict = {}
for ten in bang_diem:
    diem = bang_diem[ten]
    da_co_diem = False
    for k in grouped_dict:
        if k == diem:
            da_co_diem = True
            break   
    if da_co_diem:
        grouped_dict[diem].append(ten)
    else:
        grouped_dict[diem] = [ten]
print("Nhom theo diem:", grouped_dict)