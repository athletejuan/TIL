N,M = map(int, input().split())
cards = list(map(int, input().split()))
win = 0
for i in range(N-2):
    a = cards[i]
    for j in range(i+1, N-1):
        b = cards[j]
        for k in range(j+1, N):
            c = cards[k]
            if M-(a+b+c)>=0 and M-win > M-(a+b+c):
                win = a+b+c
print(win)