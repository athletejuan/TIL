n = int(input())

a,b = 0,1
for i in range(n-1):
    a,b = b,a+b
print(b)


# n = int(input())

# def fib(n):
#     v = [0, 1]
#     if n < 2:
#         return v[n]
#     for i in range(2, n+1):
#         v.append(fib(i-1) + fib(i-2))
#     return v[n]

# print(fib(n))