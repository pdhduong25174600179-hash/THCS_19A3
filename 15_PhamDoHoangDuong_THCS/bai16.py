chuoi_nhap = input("Nhap chuoi bat ky: ")
tan_suat = {}
for char in chuoi_nhap:
    if char == " ":
        continue
    da_co = False
    for k in tan_suat:
        if k == char:
            da_co = True
            break            
    if da_co:
        tan_suat[char] += 1
    else:
        tan_suat[char] = 1
print("Tan suat xuat hien cua cac ky tu:")
print(tan_suat)