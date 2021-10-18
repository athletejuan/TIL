N = int(input())
lectures = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
students = [list(map(int, input().split())) for _ in range(M)]


def possible(S,L):
    time = [0] * 51
    for i in range(len(S)):
        time[S[i]] = 1
    for j in range(len(L)):
        if not time[L[j]]:
            return 0
    return 1


for i in range(M):
    cnt = 0
    for j in range(N):
        if students[i][0] >= lectures[j][0]:
            cnt += possible(students[i][1:], lectures[j][1:])
    print(cnt)