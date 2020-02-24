L = int(input())

light = list(map(int, input().split()))
nums = int(input())
for i in range(nums):
    num = list(map(int, input().split()))
    if num[0]%2:
        for j in range(1, (L//num[1])+1):
            if light[(num[1]*j)-1]:
                light[(num[1]*j)-1] = 0
            else:
                light[(num[1]*j)-1] = 1
    else:
        k = 1
        if num[1] == 1 or num[1] == L:
            if light[num[1]-1]:
                light[num[1]-1] = 0
            else:
                light[num[1]-1] = 1
        else:
            if light[num[1]-1]:
                light[num[1]-1] = 0
            else:
                light[num[1]-1] = 1
            while (num[1]-k) > 0 and (num[1]+k-1) < L and light[num[1]-k-1] == light[num[1]+k-1]:
                if light[num[1]-k-1]:
                    light[num[1]-k-1] = light[num[1]+k-1] = 0
                else:
                    light[num[1]-k-1] = light[num[1]+k-1] = 1
                k += 1
s_li = list(map(str, light))
if len(s_li) > 20:
    for i in range(1, (len(s_li)//20)+1):
        print(' '.join(s_li[:20]))
        s_li = s_li[20:]
print(' '.join(s_li))



# while light[num[1]-k-1] == light[num[1]+k-1] and (num[1]-k) > 0 and (num[1]+k-1) < L:
#     if light[num[1]-k-1]:
#         light[num[1]-k-1] = light[num[1]+k-1] = 0
#     else:
#         light[num[1]-k-1] = light[num[1]+k-1] = 1
#     k += 1