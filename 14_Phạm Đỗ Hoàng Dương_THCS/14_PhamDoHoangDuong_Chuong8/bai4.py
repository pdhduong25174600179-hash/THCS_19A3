def nt(n):
    if n < 2:
        return False
    exit
    for i in range(2,n // 2 + 1):
        if n % i == 0:
            return False
    return True
n=int(input("Nhap so:"))
i=0
while i < n-1:
    i+=1
    if nt(i):
        print(i,end=" ")