N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]


def half(r, c, matrix):
    second = []
    for i in range(2):
        for j in range(2):
            second.append(matrix[r*2+i][c*2+j])
    return sorted(second)[2]


def quarter(N, arr):
    if N == 1:
        print(arr[0][0])
        return
    new = [[0]*(N//2) for _ in range(N//2)]
    for i in range(N//2):
        for j in range(N//2):
            new[i][j] = half(i, j, arr)
    quarter(N//2, new)

quarter(N, matrix)