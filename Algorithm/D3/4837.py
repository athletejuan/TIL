T = int(input())

arr = [i for i in range(1, 13)]
for tc in range(1, T+1):
    N,K = map(int, input().split())
    cnt = 0
    for i in range(1 << 12):
        sub = []
        for j in range(12):
            if i & (1 << j):
                sub.append(arr[j])
        if len(sub) == N and sum(sub) == K:
            cnt += 1
    print(f'#{tc} {cnt}')


# Tony
# import sys
# sys.stdin = open('input.txt', 'r')


# def find_subset(count, s, N, K, selected):
#     if count == N:
#         target_value = 0
#         for idx, val in enumerate(selected, start=1):
#             if val:
#                 target_value += idx
#         if target_value == K:
#             return 1
#         else:
#             return 0

#     result = 0
#     for i in range(s, 12):
#         selected[i] = 1
#         result += find_subset(count+1, i+1, N, K, selected)
#         selected[i] = 0
#     return result


# T = int(input())

# for t in range(1, T+1):
#     N, K = map(int, input().split())
#     selected = [0] * 12
#     print('#{} {}'.format(t, find_subset(0, 0, N, K, selected)))