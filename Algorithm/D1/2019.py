T = int(input())

for test_case in range(1, T+1):
    number = int(input())
    nums = []
    for i in range(number+1):
        nums.append(2 ** i)
    print(' '.join(map(str, nums)))