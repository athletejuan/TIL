N = int(input())

cute = 0
for _ in range(N):
    ans = input()
    if ans == '1':
        cute += 1
if cute > N//2:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')