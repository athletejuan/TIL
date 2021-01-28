T = int(input())

for tc in range(T):
    text = input().split()
    re_word = []
    for word in text:
        re_char = ''
        for char in word:
            re_char = char + re_char
        re_word.append(re_char)
    print(' '.join(re_word))