T = int(input())

for test_case in range(1, T+1):
    tri = list(map(int, input().split()))
    print(f'#{test_case} {(tri[0]//tri[1])**2}')