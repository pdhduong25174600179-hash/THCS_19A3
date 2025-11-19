def s1(n):
    s1=0
    for i in range(1,n+1):
        s1=s1+i
    return s1
def s2(n):
    s2=1
    for i in range(2,n):
        s2=s2*i
    return s2
def s3(n):
    s3=0
    for i in range(1,n+1):
        s3=s3+((-1)**n)/n
    k=round(s3,2)
    return k
def s4(n):
    s4=0
    for i in range(1,n+1):
        s4=s4+(i/i+2)
    return s4
n=int(input("nhap n:"))
print("S1=",s1(n))
print("S2=",s2(n))
print("S3=",s3(n))
print("S4=",s4(n))
