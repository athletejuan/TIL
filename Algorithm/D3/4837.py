T = int(input())

arr = [1,2,3,4,5,6,7,8,9,10,11,12]
for test_case in range(1, T+1):
    N,K = map(int, input().split())
    div = []
    cnt = 0
    for i in range(1 << 12):
        sub_div = []
        for j in range(12):
            if i & (1 << j):
                sub_div.append(arr[j])
        div.append(sub_div)
    
    for k in div:
        if len(k) == N and sum(k) == K:
            cnt += 1
    print(f'#{test_case} {cnt}')