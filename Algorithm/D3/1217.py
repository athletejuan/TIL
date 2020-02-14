for t in range(1, 11):
    test_case = input()
    numbers = list(map(int, input().split()))
    num = numbers[0]
    count = numbers[1]-1
    def repeat(num, count):
        if count:
            return repeat(num, count-1) * num
        else:
            return num
    print(f'#{test_case} {repeat(num, count)}')