# 1. line 불러오기
with open('service.txt','r') as f:
    lines = f.readlines()

# 2. 뒤집기
lines.reverse()

# 3-1. line 작성하기 1
# with open('reverse_service.txt','w',encoding='utf-8', newline='') as f:
#     for line in lines:
#         f.write(line)

# 3-2. line 작성하기 2
# with open('reverse_service.txt','w',encoding='utf-8', newline='') as f:
#     f.writelines(lines)

# 4. line 작성하기
with open('reverse_service.txt','w',encoding='utf-8', newline='') as f:
    for line in lines:
        f.write(line.rstrip() + '\n')