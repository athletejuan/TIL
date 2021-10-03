import sys
string = sys.stdin.readline().rstrip()
stack = []

def check(string):
    result = 0
    for s in string:
        if s == '(' or s == '[':
            stack.append(s)
        elif stack:
            last = stack.pop()
            temp = 0 if type(last) == int else 1
            m = 2 if s == ')' else 3
            while stack and type(last) == int:
                temp += last
                last = stack.pop()
            if (m == 2 and last == '(') or (m == 3 and last == '['):
                stack.append(temp*m)
            else:
                return 0
        else:
            return 0
    while stack:
        num = stack.pop()
        if type(num) == int:
            result += num
        else:
            return 0
    return result

print(check(string))