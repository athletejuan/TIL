T = int(input())

for test_case in range(1, T+1):
    number = input()
    odd_sum = 0
    for i in map(int, number.split()):
        if i%2:
            odd_sum += i
    print(odd_sum)