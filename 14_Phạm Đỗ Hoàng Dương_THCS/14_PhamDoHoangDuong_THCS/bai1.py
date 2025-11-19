def cp(n):
    k=(n**(1/2))**2
    if k==n:
        return True
    else:
        return False
n=int(input("Nhap n:"))
if cp(n):
    print(n,"la so chinh phuong")
else:
    print(n,"khong la so chinh phuong")
    