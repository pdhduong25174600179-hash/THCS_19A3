s = input("Nhap cac cap key:value (vd: a:1 b:2 c:3): ")
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
        tmp_key = ""; tmp_val = ""; dang_doc_key = True
    else:
        if dang_doc_key: tmp_key += char
        else: 
            if ('0' <= char <= '9'): tmp_val += char
print("Dict goc:", my_dict)
reversed_dict = {}
for key in my_dict:
    val = my_dict[key]
    reversed_dict[val] = key
print("Dict sau khi dao nguoc:", reversed_dict)