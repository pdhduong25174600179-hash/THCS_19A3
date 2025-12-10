def kiem_tra_so_armstrong(n):
    s = sum(int(digit) ** 3 for digit in str(n))
    return s == n
print(kiem_tra_so_armstrong(153))