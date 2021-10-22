N = input()
M = int(input())
working = [1]*10
if M:
    dis = list(map(int, input().split()))
    for i in dis:
        working[i] = 0
move = abs(int(N)-100)


def check(x):
    for i in str(x):
        if not working[int(i)]:
            return False
    return True


click = 500000
for i in range(1000001):
    if check(i) and click > abs(i-int(N))+len(str(i)):
        click = abs(i-int(N))+len(str(i))
if click > move:
    click = move
print(click)