T = int(input())

def perm(idx, temp):
    global result
    if temp > result:
        return
    if idx == N:
        if temp < result:
            result = temp
    for i in range(N):
        if not use[i]:
            use[i] = 1
            perm(idx+1, temp+arr[idx][i])
            use[i] = 0


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result, temp = 100, 0
    use = [0] * N

    perm(0, 0)
    print('#{} {}'.format(tc, result))


# 순서있는 비복원 추출로 순열 구한 후 풀이(시간초과)
# T = int(input())
#
# def perm(idx):
#     global part_sum
#     if idx == N:
#         total = 0
#         for idx, j in enumerate(sel):
#             total += arr[idx][j]
#             if total > part_sum:
#                 break
#         if total < part_sum:
#             part_sum = total
#     for i in range(N):
#         if not use[i]:
#             sel[idx] = per[i]
#             use[i] = 1
#             perm(idx + 1)
#             use[i] = 0
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     part_sum = 100
#     per = [x for x in range(N)]
#     sel = [0] * N
#     use = [0] * N
#
#     perm(0)
#     print('#{} {}'.format(tc, part_sum))