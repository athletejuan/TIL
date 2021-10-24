text = input()
word = input()
tl, wl = len(text), len(word)
cnt = i = 0

while i <= tl-wl:
    if text[i] == word[0]:
        p = 1
        while p < wl:
            if text[i+p] == word[p]:
                p += 1
            else:
                break
        else:
            cnt += 1
            i += wl-1
    i += 1
print(cnt)