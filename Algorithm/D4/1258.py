T = int(input())

def box(x):
    r,c = x[0], x[1]
    h,w = 1,1
    while r < N-1 and depot[r+1][c]:
        r += 1
        h += 1
    while c < N-1 and depot[r][c+1]:
        c += 1
        w += 1
    for i in range(h):
        for j in range(w):
            depot[r-i][c-j] = 0
    return [h,w,h*w]

for tc in range(1, T+1):
    N = int(input())
    depot = [list(map(int, input().split())) for _ in range(N)]
    boxes = []
    count = 0

    for i in range(N):
        for j in range(N):
            if depot[i][j]:
                boxes.append(box([i,j]))
                count += 1
    print('#{} {}'.format(tc, count), end=' ')
    for b in sorted(boxes, key=lambda x: (x[2], x[0])):
        print(' '.join(map(str, b[:2])), end=' ')
    print()



# 1st try
# def width(i, j):
#     count = 1
#     dx = j
#     while True:
#         dx += 1
#         if dx == n:
#             break
#         if map_list[i][dx]:
#             count += 1
#         else:
#             break
#     return count
#
# def height(i, j):
#     count = 1
#     dy = i
#     while True:
#         dy += 1
#         if dy == n:
#             break
#         if map_list[dy][j]:
#             count += 1
#         else:
#             break
#     return count
#
# def reset(s_y, s_x, e_y, e_x):
#     for i in range(s_y, e_y):
#         for j in range(s_x, e_x):
#             map_list[i][j] = 0
#
# T = int(input())
#
# for test_case in range(1, T+1):
#     n = int(input())
#     map_list = [list(map(int, input().split())) for _ in range(n)]
#     answer = []
#     for i in range(n):
#         for j in range(n):
#             if map_list[i][j]:
#                 w = width(i, j)
#                 h = height(i, j)
#                 reset(i, j, i+h, j+w)
#                 answer.append([h, w, h*w])
#     answer = sorted(answer, key=lambda x: (x[2], x[0]))
#     print(f'#{test_case} {len(answer)}', end=' ')
#     for r, c, _ in answer:
#         print(f'{r} {c}', end=' ')
#     print()


# live code
# def search_size(r,c):
#     r_cnt = 0
#     c_cnt = 0
#
#     # 행의 길이 찾기
#     for i in range(r,N):
#         if arr[i][c] != 0:
#             r_cnt += 1
#         else:
#             break
#     # 열의 길이 찾기
#     for i in range(c,N):
#         if arr[r][i] != 0:
#             c_cnt += 1
#         else:
#             break
#     ans.append([r_cnt, c_cnt, r_cnt*c_cnt])
#     init(r, c, r_cnt, c_cnt)
#
# def init(r, c, r_cnt, c_cnt):
#     for i in range(r, r+r_cnt):
#         for j in range(c, c+c_cnt):
#             arr[i][j] = 0
#
# def counting_sort(idx):
#     cnt = [0] * 10001
#     sort_ans = [0] * len(ans)
#
#     #1. 카운팅
#     for i in range(len(ans)):
#         cnt[ans[i][idx]] += 1
#
#     #2. 누적
#     for i in range(1, len(cnt)):
#         cnt[i] += cnt[i-1]
#
#     #3. 정렬하여 입력
#     for i in range(len(ans)-1, -1, -1):
#         sort_ans[cnt[ans[i][idx]]-1] = ans[i]
#         cnt[ans[i][idx]] -= 1
#
#     return sort_ans
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     ans = []
#
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] != 0:
#                 search_size(i,j)
#
#     ans = counting_sort(0) # 행을 기준으로 정렬
#     ans = counting_sort(2) # 행렬의 크기로 다시 정렬
#
#     print('#{} {}'.format(tc, len(ans)), end=' ')
#     for i in range(len(ans)):
#         print('{} {}'.format(ans[i][0], ans[i][1]), end=' ')
#     print()

###################################################################

# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]

#     ans = []

#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] != 0:
#                 r, c = i, j
#                 # 범위를 먼저 제한
#                 while r<N and arr[r][j] != 0:
#                     r += 1
#                 while c<N and arr[i][c] != 0:
#                     c += 1
#                 ans.append([r-i, c-j])

#                 # 초기화
#                 for a in range(i, r):
#                     for b in range(j, c):
#                         arr[a][b] = 0
#     ans.sort(key=lambda x: (x[0]*x[1], x[0]))
#     print('#{} {}'.format(tc, len(ans)), end=' ')
#     for i in range(len(ans)):
#         print('{} {}'.format(ans[i][0], ans[i][1]), end=' ')
#     print()