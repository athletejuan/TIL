b = []
d = []
for _ in range(3):
    bp = int(input())
    b.append(bp)
for i in range(2):
    dp = int(input())
    d.append(dp)
print(min(b)+min(d)-50)