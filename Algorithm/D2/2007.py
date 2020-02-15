T = int(input())

for test_case in range(1, T+1):
    text = input()
    temp = []
    for idx, value in enumerate(text):
        temp.append(value)
        if value in temp and text[:idx] == text[idx:idx+idx] and idx != 0:
            print(f'#{test_case} {idx}')
            break