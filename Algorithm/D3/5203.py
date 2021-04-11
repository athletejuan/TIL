T = int(input())

for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    p1, p2 = [0] * 10, [0] * 10
    for i in range(12):
        if i%2:
            p2[cards[i]] += 1
            if p2[cards[i]] > 2 or (p2[(cards[i]-2)%10] and p2[(cards[i]-1)%10]) or (p2[(cards[i]-1)%10] and p2[(cards[i]+1)%10]) or (p2[(cards[i]+1)%10] and p2[(cards[i]+2)%10]):
                print('#{} 2'.format(tc))
                break
        else:
            p1[cards[i]] += 1
            if p1[cards[i]] > 2 or (p1[(cards[i]-2)%10] and p1[(cards[i]-1)%10]) or (p1[(cards[i]-1)%10] and p1[(cards[i]+1)%10]) or (p1[(cards[i]+1)%10] and p1[(cards[i]+2)%10]):
                print('#{} 1'.format(tc))
                break
    else:
        print('#{} 0'.format(tc))