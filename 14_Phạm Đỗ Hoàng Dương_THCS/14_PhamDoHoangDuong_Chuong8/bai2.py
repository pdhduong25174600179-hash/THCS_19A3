def ucln(a,b):
    r = b % a
    while r != 0:
        r=a % b
        a=b
        b=r
    return(a)
a=int(input("So thu 1:"))
b=int(input("So thu 2:"))
print(ucln(a,b))