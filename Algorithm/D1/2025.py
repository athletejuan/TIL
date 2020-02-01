T = int(input())

for test_case in range(1, T+1):
    number = int(input())
    num_sum = 0
    for i in range(1, number+1):
        num_sum += i
    print(num_sum)