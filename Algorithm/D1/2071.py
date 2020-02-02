T = int(input())

for test_case in range(1, T+1):
    number = input()
    print(round(sum(map(int, number.split())) / 10))