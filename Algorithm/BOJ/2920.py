scale = list(map(int, input().split()))

for i in range(len(scale)-1):
    if scale[i] - scale[i+1] == 1:
        sequence = 'descending'
    elif scale[i] - scale[i+1] == -1:
        sequence = 'ascending'
    else:
        sequence = 'mixed'
        break
        
print(sequence)