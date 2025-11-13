n=int(input("nhap nam:"))
k=0
if ((n % 4 == 0) or (n % 400 == 0)) and (n % 100 != 0):
    k=0
else:
    k=1 
if k==0:
    print("nam",n,"la nam nhuan")
else:
    print("nam",n,"khong la nam nhuan")
    