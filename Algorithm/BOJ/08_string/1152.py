text = input()

cnt = 0
for i in range(len(text)):
    if text[i].isalpha() and (i == len(text)-1 or text[i+1] == ' '):
        cnt += 1
print(cnt)