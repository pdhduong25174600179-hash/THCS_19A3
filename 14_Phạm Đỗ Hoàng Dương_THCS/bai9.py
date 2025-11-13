n=int(input("nhap so dien: "))
if n <= 100:
    tien=n*1678
if (n >= 101) and (n <= 200):
    tien=100*1678+(n-100)*1734
if (n >= 201):
    tien=100*1678+100*1734+(n-200)*2014
print(tien)
