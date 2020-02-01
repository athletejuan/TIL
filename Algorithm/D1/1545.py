T = int(input())

for test_case in range(1, T+1):
    number = int(input())
    rev_num = []
    for i in range(number+1):
        rev_num.append(i)
    print(' '.join(map(str, rev_num[::-1])))