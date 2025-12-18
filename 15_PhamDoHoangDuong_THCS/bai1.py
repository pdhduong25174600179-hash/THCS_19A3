s=input("Nhap vao chuoi:")
dem_chu = 0
dem_so = 0
dem_dac_biet = 0
for char in s :
    if ('a'<= char <= char <= 'z') or ('A'<= char <= 'Z'):
        dem_chu += 1
    elif '0' <= char <= '9':
        dem_so += 1
    else:
        dem_dac_biet +=1
print ("So ki tu chu :", dem_chu)
print ("So ky tu so :", dem_so)
print ("So ki tu dac biet :", dem_dac_biet)
