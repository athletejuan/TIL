T = int(input())

for test_case in range(1, T+1):
    number = input()
    my_sum = 0
    for i in number:
        my_sum += int(i)
    print(my_sum)