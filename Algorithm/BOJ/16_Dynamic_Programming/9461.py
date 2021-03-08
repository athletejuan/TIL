T = int(input())

for _ in range(T):
    tri = [0,1,1]
    N = int(input())
    for i in range(N-2):
        tri.append(tri[i] + tri[i+1])
    print(tri[N])

# 1st try
# for _ in range(T):
#     tri = [1,1,1,2,2]
#     N = int(input())
#     if N < 6:
#         print(tri[N-1])
#     else:
#         for i in range(N-5):
#             tri.append(tri[i] + tri[i+4])
#         print(tri[-1])