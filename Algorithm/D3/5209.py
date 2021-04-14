T = int(input())

def min_cost(cost, product):
    global minimum
    if minimum and cost > minimum:
        return
    for i in range(product, N):
        for j in range(N):
            if not visited[j]:
                cost += factory[i][j]
                product += 1
                visited[j] = 1
                min_cost(cost, product)
                if product == N and (not minimum or minimum > cost):
                    minimum = cost
                cost -= factory[i][j]
                product -= 1
                visited[j] = 0
        else:
            break

for tc in range(1, T+1):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    minimum = 0
    min_cost(0, 0)
    print('#{} {}'.format(tc, minimum))