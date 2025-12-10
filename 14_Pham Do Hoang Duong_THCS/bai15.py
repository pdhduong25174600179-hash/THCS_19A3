def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Nhập n: "))
print("Nguyên tố?" , kiem_tra_so_nguyen_to(n))

print("Các số nguyên tố từ 100 đến 500:")
for i in range(100, 501):
    if kiem_tra_so_nguyen_to(i):
        print(i, end=" ")