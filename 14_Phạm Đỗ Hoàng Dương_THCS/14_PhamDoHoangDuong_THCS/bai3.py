def ucln(a,b):
    r = b % a
    while r != 0:
        r=a % b
        a=b
        b=r
    return(a)
a=int(input("Nhap tu so:"))
b=int(input("Nhap mau so:"))
r=ucln(a,b)
a1=a // r
b1=b // r
print("phan so da toi gian:",a1,"/",b1)