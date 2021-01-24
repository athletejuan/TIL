T = int(input())

for _ in range(T):
    A,B = map(int, input().split())
    C,D = A,B
    if D > C:
        C,D = D,C
    while D:
        C = C%D
        C,D = D,C
    print(C*(A//C)*(B//C))


# T = int(input())

# for _ in range(T):
#     A,B = map(int, input().split())
#     al = []
#     bl = []
#     cl = []
#     for i in range(2, max(A,B)+1):
#         while True:
#             if not A%i and not B%i:
#                 cl.append(i)
#                 A //= i
#                 B //= i
#             elif not A%i:
#                 al.append(i)
#                 A //= i
#             elif not B%i:
#                 bl.append(i)
#                 B //= i
#             else:
#                 break
#         if A == 1 and B == 1:
#             break
#     lcm = 1
#     if al:
#         for a in al:
#             lcm *= a
#     if bl:
#         for b in bl:
#             lcm *= b
#     if cl:
#         for c in cl:
#             lcm *= c
#     print(lcm)