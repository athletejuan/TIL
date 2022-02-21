days = ['SAT', 'FRI', 'THU', 'WED', 'TUE', 'MON', 'SUN']
T = int(input())
 
for tc in range(1, T+1):
    S = input()
    for idx,day in enumerate(days, start=1):
        if day == S:
            print('#{} {}'.format(tc, idx))
            break