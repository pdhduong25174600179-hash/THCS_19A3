s = input("Nhap cac cap key:value (vd: a:10 b:20 c:5): ")
my_dict = {}
tmp_key = ""
tmp_val = ""
dang_doc_key = True 
for char in s + " ":
    if char == ":":
        dang_doc_key = False 
    elif char == " ":
        if tmp_key != "" and tmp_val != "":
            val_so = int(tmp_val) 
            my_dict[tmp_key] = val_so
        tmp_key = ""
        tmp_val = ""
        dang_doc_key = True
    else:
        if dang_doc_key:
            tmp_key += char
        else:
            if ('0' <= char <= '9') or (char == '-'):
                tmp_val += char
print("Dictionary da nhap:", my_dict)
if len(my_dict) == 0:
    print("Dictionary rong.")
else:
    max_val = -999999999
    max_key = ""
    for key in my_dict:
        val = my_dict[key]
        if val > max_val:
            max_val = val
            max_key = key
    print(f"Key co gia tri lon nhat la '{max_key}' voi gia tri {max_val}")