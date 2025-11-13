n=int(input("nhap so tien gui ban dau:"))
lai=float(input("nhap lai suat nam:"))
laithang=lai/12
motthang=laithang*n
haiquy=3*2*laithang*n
banam=3*lai*n
thang=round(motthang,-1)
quy=round(haiquy,-1)
nam=round(banam,-1)
print("so tien lai sau 1 thang: ",thang)
print("so tien lai sau 2 quy: ",quy)
print("so tien lai sau 3 nam: ",nam)
