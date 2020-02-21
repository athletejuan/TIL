T = int(input())

for test_case in range(1, T+1):
    numbers = list(map(int, input().split()))
    i = 1
    while i**2 <= numbers[0]:
        i += 1
    if numbers[0] == (i**2):
        print(f'#{test_case} 0')
    else:
        i -= 1
        gap_list = []
        gap_list.append(numbers[2] * (numbers[0] - (i**2)))
        for j in range(1, i+1):
            a = numbers[0] // j
            b = numbers[0] % j
            r = (numbers[1] * abs(a - j)) + (numbers[2] * b)
            gap_list.append(r)
        print(f'#{test_case} {min(gap_list)}')