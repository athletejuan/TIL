A,B = input().split()
A = int(A[::-1])
B = int(B[::-1])

if A > B:
    print(A)
else:
    print(B)

# A,B = map(int, input().split())
# a = str(A)[::-1]
# b = str(B)[::-1]

# for _ in range(3):
#     if A%10 > B%10:
#         print(a)
#         break
#     elif A%10 < B%10:
#         print(b)
#         break
#     else:
#         if (A//10)%10 > (B//10)%10:
#             print(a)
#             break
#         elif (A//10)%10 < (B//10)%10:
#             print(b)
#             break
#         else:
#             if int(a) > int(b):
#                 print(a)
#             else:
#                 print(b)