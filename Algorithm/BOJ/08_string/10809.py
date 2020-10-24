S = input()

chars = {}
for idx, char in enumerate(S):
    if not chars or ord(char) not in chars.keys():
        chars[ord(char)] = idx

result = []
for i in range(97,123):
    if i not in chars.keys():
        result.append('-1')
    else:
        result.append(str(chars[i]))
print(' '.join(result))