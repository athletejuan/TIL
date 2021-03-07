T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())
    Cheese = list(map(int, input().split()))
    oven = [Cheese[i] for i in range(N)]
    bake = [1] * N + [0] * (M-N)
    pizza_num = [i for i in range(N)]
    waiting = True
    end = 0

    while end < N:
        end = 0
        for idx, cs in enumerate(oven):
            if cs:
                if oven[idx] == 1:
                    last = pizza_num[idx]+1
                oven[idx] = cs // 2
                if not oven[idx]:
                    if waiting:
                        for i, wait in enumerate(bake):
                            if not wait:
                                pizza_num[idx] = i
                                oven[idx] = Cheese[i]
                                bake[i] = 1
                                break
                        else:
                            waiting = False
            else:
                end += 1
    print('#{} {}'.format(tc, last))


# live code
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     pizza = list(map(int, input().split()))
#     firepot = [[i+1, pizza[i]] for i in range(N)]
#     next_pizza = N
#     # last_pizza = -1

#     while len(firepot) > 1:
#     # while firepot:
#         num, cheese = firepot.pop(0)

#         cheese //= 2
#         # last_pizza = num
#         if cheese:
#             firepot.append([num, cheese])
#         else:
#             if next_pizza < M:
#                 firepot.append([next_pizza+1, pizza[next_pizza]])
#                 next_pizza += 1
#     print('#{} {}'.format(tc, firepot[0][0]))