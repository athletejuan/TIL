T = int(input())

for test_case in range(1, T+1):
    number = int(input())
    nums = []
    for i in range(1, number+1):
        if number % i == 0:
            nums.append(i)
    print(' '.join(map(str, nums)))