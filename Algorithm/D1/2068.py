T = int(input())

for test_case in range(1, T+1):
    number = input()
    print(max(map(int, number.split())))