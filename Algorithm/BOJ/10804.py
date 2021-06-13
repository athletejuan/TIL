cards = [str(i) for i in range(1, 21)]

for _ in range(10):
    a,b = map(int, input().split())
    for i in range(a-1, (b+a)//2):
        cards[i], cards[a+b-i-2] = cards[a+b-i-2], cards[i]
print(' '.join(cards))