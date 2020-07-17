# Workshop

# 1. 세로로 출력하기
N = int(input())

for i in range(1, N+1):
    print(i)

# 2. 가로로 출력하기
N = int(input())

for i in range(N+1):
    print(i, end=' ')

# 3. 거꾸로 출력하기
N = int(input())

for i in range(N, 0, -1):
    print(i)

# 4. 거꾸로 출력하기(SWEA #1545)
N = int(input())

for i in range(N, -1, -1):
    print(i, end=' ')

# 5. N줄 덧셈(SWEA #2025)
N = int(input())

total = 0
for i in range(1, N+1):
    total += i

print(total)