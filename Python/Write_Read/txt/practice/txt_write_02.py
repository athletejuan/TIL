f = open('ssafy_02.txt', 'w')
for i in range(10):
    f.write(f"This is line {i}\r\n")
f.close()

with open('with_ssafy_02.txt', 'w') as f:
    for i in range(10):
        f.write(f"This is line {i}, too\r\n")

with open('ssafy_02_01.txt', 'w') as f:
    f.writelines(['0\n','1\n','2\n','3\n'])