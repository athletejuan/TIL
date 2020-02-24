time = list(map(int, input().split()))
if not time[0] and time[1] < 45:
    time[0] = 23
    time[1] += 15
else:    
    if time[1] > 44:
        time[1] -= 45
    else:
        time[0] -= 1
        time[1] += 15    
print(' '.join(list(map(str, time))))