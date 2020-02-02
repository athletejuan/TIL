T = int(input())

for test_case in range(1, T+1):
    text = input()
    trans = []
    for i in text.split():
        trans.append(str(ord(i) - 64))
    print(' '.join(trans))