n = int (input ("N sonni kiriting:"))
lt = []
while n > 0:
    k = n % 10
    n = n // 10
    lt.append(k)


j = 0
for i in lt:
    if i % 2 == 0:
        j += 1
print ("YES" if len(lt) % 2 != 0 and j == 0 else "NO")