T = int(input())

ps = []
for _ in range(T):
    p = input()
    if p.count('(') == p.count(')') and p[-1] == ')':
        for i in p:
            if i == '(':
                ps.append(i)
            elif i == ')' and (not ps or ps[-1] == ')'):
                print('NO')
                break
            elif i == ')' and ps[-1] == '(':
                ps.pop()
        else:
            if not ps:
                print('YES')
    else:
        print('NO')