A,B = map(int, input().split())
N = int(input())
favor = [int(input()) for i in range(N)]

cnt = abs(B-A)
for F in favor:
    if cnt > abs(B-F):
        cnt = abs(B-F)+1
print(cnt)