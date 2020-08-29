N = int(input())

def fac(N):
    if not N or N == 1:
        return 1
    else:
        return N * fac(N-1)

print(fac(N))