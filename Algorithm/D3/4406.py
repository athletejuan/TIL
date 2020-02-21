T = int(input())

for test_case in range(1, T+1):
    text = input()
    vowels = 'aeiou'
    new = []
    for i in text:
        if i not in vowels:
            new.append(i)
    print(f'#{test_case} {"".join(new)}')