# f = open('ssafy.txt', 'r')
# all_text = f.read()    # all_text는 문자열(개행문자 포함!)
# print(all_text)
# f.close()

# with open('with_ssafy.txt', 'r') as f:
#     all_text = f.read()    # all_text는 문자열(개행문자 포함!)
#     print(all_text)

# f = open('ssafy.txt','r')
# lines = f.readlines() # lines는 리스트 형태
# for line in lines:
#     print(line)
# f.close()

# with open('with_ssafy.txt','r') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line.strip()) # 개행 문자 제거! (print 함수 자체에 개행 문자 있음.)

# reverse save
# f = open('ssafy.txt','r')
# lines = f.readlines()
# re_lines = []
# for i in range(len(lines)):
#     re_lines.append(lines.pop())
#1
# w = open('reverse_ssafy2.txt','w', encoding='utf-8')
# for j in re_lines:
#     w.write(j)
# w.close()
#2
# with open('reverse_ssafy.txt', 'w', encoding='utf-8') as f:
#     f.writelines(re_lines)