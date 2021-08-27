T = int(input())

def check(x, color):
    cnt = 0
    for i in flag[x]:
        if i != color:
            cnt += 1
    return cnt

for tc in range(1, T+1):
    N,M = map(int, input().split())
    flag = [input() for _ in range(N)]
    min_cnt = N*M

    white = 0
    for i in range(N-2):
        white += check(i, 'W')
        blue = 0
        for j in range(i+1, N-1):
            blue += check(j, 'B')
            red = 0
            while j < N-1:
                red += check(j+1, 'R')
                j += 1
            change = white + blue + red
            if min_cnt > change:
                min_cnt = change
    print('#{} {}'.format(tc, min_cnt))


# live code
# def perm(idx, sub_sum):
#     global ans
#     # 유망성 검사
#     # 아래 조건에 걸리게 되면 이후 작업은 무의미
#     if sub_sum > N:
#         return
#     if idx == 3:
#         if sub_sum == N:
#             cnt = 0
#             st0 = sel[0]
#             st1 = st0 + sel[1]
#
#             # 흰색 칠하기
#             for i in flag[:st0]:
#                 for j in i:
#                     if j != 'W':
#                         cnt += 1
#             # 파란색 칠하기
#             for i in flag[st0:st1]:
#                 for j in i:
#                     if j != 'B':
#                         cnt += 1
#             # 빨간색 칠하기
#             for i in flag[st1:]:
#                 for j in i:
#                     if j != 'R':
#                         cnt += 1
#             if ans > cnt:
#                 ans = cnt
#         return
#
#     # 중복순열 응용
#     for i in range(1, N-1):
#         sel[idx] = i
#         perm(idx+1, sub_sum+i)
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N,M = map(int, input().split())
#
#     flag = [list(input()) for _ in range(N)]
#     sel = [0] * 3
#     ans = 987654321
#
#     perm(0, 0)
#     print('#{} {}'.format(tc, ans))

########################################################

# T = int(input())
#
# for tc in range(1, T+1):
#     N,M = map(int, input().split())
#
#     flag = [input() for _ in range(N)]
#     W = [0] * N
#     B = [0] * N
#     R = [0] * N
#
#     # 행을 보면서 나와 다른 색깔의 개수를 카운팅
#     for i in range(N):
#         for j in range(M):
#             if flag[i][j] != 'W':
#                 W[i] += 1
#             if flag[i][j] != 'B':
#                 B[i] += 1
#             if flag[i][j] != 'R':
#                 R[i] += 1
#
#     # 누적
#     for i in range(1, N):
#         W[i] += W[i-1]
#         B[i] += B[i-1]
#         R[i] += R[i-1]
#     ans = 987654321
#     # 각 색별로 한줄 이상은 확보해야하기 때문에
#     for i in range(N-2):
#         for j in range(i+1, N-1):
#             w_cnt = W[i]
#             b_cnt = B[j] - B[i]
#             r_cnt = R[N-1] - R[j]
#
#             if ans > w_cnt + b_cnt + r_cnt:
#                 ans = w_cnt + b_cnt + r_cnt
#     print('#{} {}'.format(tc, ans))
