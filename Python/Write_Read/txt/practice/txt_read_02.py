f = open('ssafy_02.txt', 'r')
all_text = f.read()  # all_text는 문자열(개행문자 포함)
print(all_text)
f.close()

with open('with_ssafy_02.txt', 'r') as f:
    all_text = f.read()  # all_text는 문자열(개행문자 포함)
    print(all_text)

f = open('ssafy_02_01.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line.rstrip())

with open('ssafy_02_01.txt', 'r') as f:
    lines = f.readlines()
with open('ssafy_02_01.txt', 'w') as r:
    for line in lines[::-1]:
        r.write(line)