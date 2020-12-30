word = input()

count = 0
for i in range(len(word)):
    if word[i] == '=' or word[i] == '-':
        if i > 1 and word[i-1] == 'z' and word[i-2] == 'd':
            count -= 1
        else:
            pass
    elif word[i] == 'j' and (word[i-1] == 'l' or word[i-1] == 'n'):
        pass
    else:
        count += 1
print(count)