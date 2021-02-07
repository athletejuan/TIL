R,C,W = map(int, input().split())

pascal = [0, 1, 0]
# part_sum = 0
part = []
for i in range(R+W-2):
    next_list = [0]
    for j in range(len(pascal)-1):
        next_num = pascal[j] + pascal[j+1]
        next_list.append(next_num)
        if i >= R-2 and C-1 <= j <= i-R+C+1:
            part.append(next_num)
    # if i >= R-2:
    #     part_sum += sum(next_list[C:C+(i+3-R)])
    next_list += [0]
    pascal = next_list
if R == 1:
    # part_sum += 1
    part += [1]
# print(part)
print(sum(part))
# print(part_sum)