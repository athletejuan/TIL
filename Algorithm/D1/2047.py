T = int(input())

for test_case in range(1, T+1):
    text = input()
    title = ''
    for i in text:
        if i.islower():
            i = i.upper()
        title += i
    print(title)