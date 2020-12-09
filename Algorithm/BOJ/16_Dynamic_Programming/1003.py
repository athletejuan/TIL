T = int(input())

for _ in range(T):
    N = int(input())
    z, o = 1, 0
    for i in range(N):
        z, o = o, z+o
    print(z, o)

# T = int(input())

# def fib(N):
#     v = [0, 1]
#     if N < 2:
#         return v[N]
#     for i in range(2, N+1):
#         v.append(fib(i-1) + fib(i-2))
#     return v[N]

# for _ in range(T):
#     N = int(input())
#     if not N:
#         print('1 0')
#     else:
#         print(f'{fib(N-1)} {fib(N)}')


# T = int(input())

# def fib(N):
#     v = [0, 1]
#     if N < 2:
#         return (0, N)
#     for i in range(2, N+1):
#         v.append(sum(fib(i-1)))
#     return (v[N-1], v[N])

# for _ in range(T):
#     N = int(input())
#     if not N:
#         print('1 0')
#     else:
#         print(f"{' '.join(map(str, fib(N)))}")