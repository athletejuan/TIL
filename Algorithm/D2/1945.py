T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    prime = [2, 3, 5, 7, 11]
    count = [0] * 5
    for i in range(5):
        while not N % prime[i]:
            N /= prime[i]
            count[i] += 1
    print(f'#{test_case} {" ".join(map(str, count))}')