bros = []
total = 0
for _ in range(9):
    bro = int(input())
    total += bro
    bros.append(bro)
for i in bros:
    if total-100-i != i and total-100-i in bros:
        bros.remove(i)
        bros.remove(total-100-i)
        break
for j in sorted(bros):
    print(j)