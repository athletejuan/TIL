N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
nums = list(map(int, input().split()))
match = []

for i in range(M):
    check = nums[i]
    left = 0
    right = N-1
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == check:
            match.append('1')
            break
        elif cards[mid] > check:
            right = mid-1
        else:
            left = mid+1
    else:
        match.append('0')

print(' '.join(match))