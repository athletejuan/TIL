T = int(input())

for test_case in range(1, T+1):
    nums = input()
    numbers = input().split()
    planet = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
    num_list = []
    str_list = []
    for i in numbers:
        num_list.append(planet[i])
    for j in sorted(num_list):
        for key, value in planet.items():
            if j == value:
                str_list.append(key)
    print(f'#{test_case}')
    print(f'{" ".join(str_list)}')