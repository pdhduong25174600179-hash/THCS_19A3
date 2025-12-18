nhap = input("Nhap cac so (cach nhau boi khoang trang): ")
lst = []
tmp = ""
for char in nhap + " ":
    if char != " ":
        tmp += char
    elif tmp != "":
        lst.append(int(tmp))
        tmp = ""
tong_chan = 0
tong_le = 0
for x in lst:
    if x % 2 == 0:
        tong_chan += x
    else:
        tong_le += x
print("Tong so chan:", tong_chan)
print("Tong so le:", tong_le)