winner = 0
for i in range(5):
    total = sum(map(int, input().split()))
    if winner < total:
        winner = total
        num = i+1
print(f'{num} {winner}')