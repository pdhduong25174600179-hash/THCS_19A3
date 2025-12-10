def tong_chu_so(n):
    if n < 10:
        return n
    return n % 10 + tong_chu_so(n // 10)
print(tong_chu_so(1234))

