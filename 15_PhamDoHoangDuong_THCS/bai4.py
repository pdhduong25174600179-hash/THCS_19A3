s = input("Nhap cac so nguyen (cach nhau boi khoang trang): ")
lst = []
tmp = ""
for char in s + " ":
    if char != " ":
        tmp += char
    else:
        if tmp != "": 
            lst.append(int(tmp))
            tmp = ""
if len(lst) < 2:
    print("Danh sach can it nhat 2 so de tim so lon thu hai.")
else:
    so_lon_nhat = -999999999 
    so_lon_thu_hai = -999999999    
    for x in lst:
        if x > so_lon_nhat:
            so_lon_thu_hai = so_lon_nhat
            so_lon_nhat = x           
        elif x > so_lon_thu_hai and x != so_lon_nhat:
            so_lon_thu_hai = x
    if so_lon_thu_hai == -999999999:
        print("Khong co so lon thu hai (cac so bang nhau het).")
    else:
        print("So lon thu hai la:", so_lon_thu_hai)