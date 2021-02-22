T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    for i in range(len(str2)-len(str1)+1):
        if str2[i:i+len(str1)] == str1:
            print('#{} 1'.format(tc))
            break
    else:
        print('#{} 0'.format(tc))


# Boyer-Moore Algorithm
# for tc in range(1, T+1):
#     str1 = input()
#     str2 = input()

#     s = str1[::-1]
#     i = len(str1)-1
#     result = 0

#     while i < len(str2):
#         j = 0
#         if s[j] == str2[i]:
#             while j < len(s):
#                 if s[j] != str2[i-j]:
#                     i += 1
#                     break
#                 j += 1
#             else:
#                 result = 1
#         else:
#             while j < len(str1):
#                 if s[j] == str2[i]:
#                     i += j
#                     break
#                 j += 1
#             else:
#                 i += j
#                 while i < len(str2) and s[0] != str2[i]:
#                     i += 1
#         if result:
#             break
#     print('#{} {}'.format(tc, result))