T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    ans = -1
    for i in range(N):
        for j in range(i+1,N):
            if L[i]*L[j] > ans:
                x = L[i]*L[j]
                l = x % 10
                x //= 10
                while x > 0:
                    b = x % 10
                    if l < b:
                        break
                    else:
                        l = b
                        x //= 10
                else:
                    ans = L[i]*L[j]
    print(f'#{test_case} {ans}')