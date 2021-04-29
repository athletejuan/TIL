T = int(input())

for tc in range(1, T+1):
    once, dup = [], []
    for char in input():
        if char in once and char not in dup:
            dup.append(char)
        else:
            once.append(char)
    if len(dup) > 1:
        print('#{} Yes'.format(tc))
    else:
        print('#{} No'.format(tc))