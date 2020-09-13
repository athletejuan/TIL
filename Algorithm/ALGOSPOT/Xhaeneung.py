T = int(input())

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

for _ in range(T):
    new_eq = []
    equation = input().split()

    for idx,v in enumerate(numbers):
        if equation[0] == v:
            new_eq.append(idx)
    for idx,v in enumerate(numbers):
        if equation[2] == v:
            new_eq.append(idx)

    if equation[1] == '+':
        number = sum(new_eq)
    elif equation[1] == '-':
        number = new_eq[0]-new_eq[1]
    elif equation[1] == '*':
        number = new_eq[0]*new_eq[1]
        
    num_cnt = {}
    num_check = {}
    if 0 <= number <= 10:
        for char in equation[4]:
            num_cnt[char] = equation[4].count(char)
        for char in numbers[number]:
            num_check[char] = numbers[number].count(char)
        if num_cnt == num_check:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

