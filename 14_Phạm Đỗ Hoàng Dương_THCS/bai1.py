giasp=float(input("Nhap gia san pham:"))
soluong=int(input("Nhap so luong:"))
thue=10/100
vat=giasp*soluong*thue
tongtien=giasp*soluong+vat
ttlt=round(tongtien,2)
print("tong tien phai tra la: ",ttlt)