N = input()
C = int(N)

def div_sum(num):
    new = num
    while num:
        new += num%10
        num //= 10
    if new == C:
        return True

start = 1 if C-(len(N)*9) < 0 else C-(len(N)*9)
while start < C:
    if div_sum(start):
        print(start)
        break
    start += 1
else:
    print(0)