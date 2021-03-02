T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())
    queue = input().split()
    for _ in range(M):
        queue.append(queue.pop(0))
    print('#{} {}'.format(tc, queue[0]))


# 1st try
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = input().split()
#     print(f'#{test_case} {arr[M%N]}')