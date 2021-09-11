T = int(input())

for tc in range(1, T + 1):
    s, p, q, m = map(int, input().split())
    A = []
    visited = [0] * m

    while not visited[s]:
        A.append(s)
        visited[s] = 1
        s = ((s * p) + q) % m

    for idx, num in enumerate(A):
        if num == s:
            print('#{} {}'.format(tc, len(A[idx:])))
            break