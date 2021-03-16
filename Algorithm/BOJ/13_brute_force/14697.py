A,B,C,N = map(int, input().split())

def arrange():
    for i in range(N//A+1):
        for j in range(N//B+1):
            for k in range(N//C+1):
                if A*i + B*j + C*k == N:
                    return 1
                elif A*i + B*j + C*k > N:
                    break
    return 0

print(arrange())