T = int(input())
 
for tc in range(1, T+1):
    results = input()
    lose = 0
    for result in results:
        if result == 'x':
            lose += 1
            if lose > 7:
                print('#{} NO'.format(tc))
                break
    else:
        print('#{} YES'.format(tc))