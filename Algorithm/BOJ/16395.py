n,k = map(int, input().split())
pascal = [0, 1, 0]

for i in range(n-1):
    triangle = [0]
    for i in range(len(pascal)-1):
        triangle.append(pascal[i] + pascal[i+1])
    pascal = triangle + [0]

print(pascal[k])


# 7% 시간 초과
# def pascal(n,k):
#     if n < 2 or k < 2 or k > n-1:
#         return 1
#     return pascal(n-1, k-1) + pascal(n-1, k)
#
# print(pascal(n,k))