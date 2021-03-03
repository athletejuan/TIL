def paren_match():
    for p in paren:
        if p in match:
            check.append(p)
        else:
            if match[check[-1]] == p:
                check.pop()
            else:
                return 0
    else:
        return 1 if not check else 0

for tc in range(1, 11):
    T = input()
    paren = input()
    check = []
    match = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    print('#{} {}'.format(tc, paren_match()))