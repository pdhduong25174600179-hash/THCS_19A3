n=int(input("nhap luong co ban: "))
c=int(input("nhap so ngay cong: "))
luongngay=n//22
if c>=22:
    tienthuong=(10/100)*n
    tiennhan=n*c+tienthuong
if c<22:
    tienphat=(5/100)*n
    tiennhan=n*c-tienphat
print(tiennhan)

