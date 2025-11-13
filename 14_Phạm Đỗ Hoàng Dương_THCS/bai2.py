keo=int(input("Nhap so keo:"))
hs=int(input("Nhap so hoc sinh:"))
i=0
min=keo
sokeo=0
while i<=(keo//hs):
    i+=1
    cl=keo-hs*i
    if (cl<min) and (cl>0):
        min=cl
        sokeo=i
print("so keo moi hoc sinh nhan duoc la: ",sokeo)
print("so keo thua la: ",min)
