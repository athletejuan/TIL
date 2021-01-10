T = int(input())
ans = []
for tc in range(1, T+1):
    n = list(map(int, input()))
    while sum(n) > 9:
        n = list(map(int, list(str(sum(n)))))
    ans.append(sum(n))

for idx, a in enumerate(ans):
    print(f'#{idx+1} {a}')