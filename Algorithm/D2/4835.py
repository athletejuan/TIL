T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(N-M+1):
        part = 0
        for j in range(i, i+M):
            part += arr[j]
        if not i:
            top, bottom = part, part
        else:
            if part > top:
                top = part
            if part < bottom:
                bottom = part
    print('#{} {}'.format(tc, top - bottom))


# 1st try
# T = int(input())

# for tc in range(1, T+1):
#     N,M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     parts = []
#     for i in range(N-M+1):
#         part = 0
#         for j in range(i, i+M):
#             part += arr[j]
#         parts.append(part)
#     parts.sort()
#     print('#{} {}'.format(tc, parts[-1] - parts[0]))