nhap = input("Nhap day so: ")
target = int(input("Nhap gia tri tong can tim: "))
lst = []
tmp = ""
for char in nhap + " ":
    if char != " ":
        tmp += char
    elif tmp != "":
        lst.append(int(tmp))
        tmp = ""
print(f"Cac cap so co tong bang {target}:")
n = len(lst)
for i in range(n):
    for j in range(i + 1, n): 
        if lst[i] + lst[j] == target:
            print(f"({lst[i]}, {lst[j]})")