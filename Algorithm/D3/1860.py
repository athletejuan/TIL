T = int(input())

for test_case in range(1, T+1):
    num = list(map(int, input().split()))
    cus = list(map(int, input().split()))
    wait = []
    fish = 0
    for i in range(num[0]):
        wait.append(cus[i] // num[1])
    pick = sorted(set(wait))
    for j in range(len(pick)):
        if not j:
            if num[2]*pick[j] - wait.count(pick[j]) < 0:
                print(f'#{test_case} Impossible')
                break
            else:
                fish += num[2]*pick[j] - wait.count(pick[j])
        else:
            fish += (num[2]*(pick[j] - pick[j-1])) - wait.count(pick[j])
            if fish < 0:
                print(f'#{test_case} Impossible')
                break
    else:
        print(f'#{test_case} Possible')