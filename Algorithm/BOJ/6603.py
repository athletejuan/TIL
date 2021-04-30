lotto = list(map(int, input().split()))
k = lotto[0]
S = lotto[1:]
picked = []
cnt = 0

def select(S):
    if len(picked) == 6:
        return print(' '.join(picked))
    for i in range(k):
        if not picked or (str(S[i]) not in picked and S[i] > int(picked[-1])):
            picked.append(str(S[i]))
            select(S)
            picked.pop()

while k:
    if not cnt:
        select(S)
        cnt += 1
        lotto = list(map(int, input().split()))
        k = lotto[0]
        S = lotto[1:]
        picked = []
    else:
        print()
        select(S)
        lotto = list(map(int, input().split()))
        k = lotto[0]
        S = lotto[1:]
        picked = []