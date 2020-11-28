T = int(input())

for test_case in range(1, T+1):
    s,f = map(int, input().split())
    cnt = 0
    if len(str(s**.5)) < 5 and str(int(s**.5)) == str(int(s**.5))[::-1]:
        cnt = 1
    a = int(s**.5)+1
    b = int(f**.5)+1
    for i in range(a, b):
        if str(i) == str(i)[::-1] and str(int(i**2)) == str(int(i**2))[::-1]:
            cnt += 1
    print(f'#{test_case} {cnt}')