N = int(input())
books = {}
top = 0
best = []

for _ in range(N):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

for v in books.values():
    if v > top:
        top = v

for k, v in books.items():
    if v == top:
        best.append(k)

print(sorted(best)[0])