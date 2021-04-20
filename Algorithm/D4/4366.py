T = int(input())

for tc in range(1, T+1):
    bi = list(map(int, input()))
    tri = list(map(int, input()))
    cand = []
    for i in range(1, len(bi)):
        temp = 2**(len(bi)-1)
        for j in range(1, len(bi)):
            if i == j:
                temp += ((bi[j]+1)%2)*2**(len(bi)-j-1)
            else:
                temp += (bi[j])*2**(len(bi)-j-1)
        cand.append(temp)

    for k in cand:
        check, cnt, p = k, 0, 1
        while check:
            if check%3 == tri[len(tri)-p]:
                cnt += 1
            p += 1
            check //= 3
        if cnt == len(tri)-1:
            print('#{} {}'.format(tc, k))
            break


# aclass
# TC = int(input())
# for tc in range(1, TC + 1):
#     bi_num = input()
#     tri_num = input()
#
#     bi_num_lst = []
#     tri_num_lst = []
#     for i in range(len(bi_num)):
#         bi_num2 = list(bi_num)
#         if bi_num2[i] == '0':
#             bi_num2[i] = '1'
#             bi_num_lst.append(int(''.join(bi_num2), 2))
#
#         else:
#             bi_num2[i] = '0'
#             bi_num_lst.append(int(''.join(bi_num2), 2))
#
#     for i in range(len(tri_num)):
#         tri_num2 = list(tri_num)
#         if tri_num2[i] == '0':
#             tri_num2[i] = '1'
#             tri_num_lst.append(int(''.join(tri_num2), 3))
#             tri_num2[i] = '0'
#             tri_num2[i] = '2'
#             tri_num_lst.append(int(''.join(tri_num2), 3))
#
#         elif tri_num2[i] == '1':
#             tri_num2[i] = '2'
#             tri_num_lst.append(int(''.join(tri_num2), 3))
#             tri_num2[i] = '1'
#             tri_num2[i] = '0'
#             tri_num_lst.append(int(''.join(tri_num2), 3))
#
#         else:
#             tri_num2[i] = '0'
#             tri_num_lst.append(int(''.join(tri_num2), 3))
#             tri_num2[i] = '2'
#             tri_num2[i] = '1'
#             tri_num_lst.append(int(''.join(tri_num2), 3))
#
#     result = 0
#     for i in bi_num_lst:
#         if i in tri_num_lst:
#             result = i
#             break
#
#     print('#%d %d' % (tc, result))