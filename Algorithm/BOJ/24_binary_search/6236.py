N,M = map(int, input().split())
costs, mini, total = [], 0, 0

def pocket(mid):
    cnt = 1
    temp = mid
    for cost in costs:
        if temp < cost:
            temp = mid
            cnt += 1
        temp -= cost
    return cnt

for _ in range(N):
    day = int(input())
    if not mini or day > mini:
        mini = day
    total += day
    costs.append(day)

while mini <= total:
    mid = (mini + total) // 2
    cnt = pocket(mid)
    if cnt < M:
        total = mid - 1
    elif cnt > M:
        mini = mid + 1
    else:
        while pocket(mid) == M and mid >= mini:
            mid -= 1
        print(mid+1)
        break
else:
    print(mid)