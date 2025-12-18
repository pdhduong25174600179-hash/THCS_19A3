s = input("Nhap tuple (cac so cach nhau boi khoang trang): ")
tuple_goc = () 
tmp = ""
for char in s + " ":
    if ('0' <= char <= '9') or (char == '-'):
        tmp += char
    else:
        if tmp != "":
            val = int(tmp)
            tuple_goc += (val,) 
            tmp = ""
tuple_chan = ()
tuple_le = ()
tong_chan = 0
tong_le = 0
for x in tuple_goc:
    if x % 2 == 0:
        tuple_chan += (x,) 
        tong_chan += x
    else:
        tuple_le += (x,)
        tong_le += x
print("Tuple goc:", tuple_goc)
print("Tuple chan:", tuple_chan, "| Tong:", tong_chan)
print("Tuple le:", tuple_le, "| Tong:", tong_le)