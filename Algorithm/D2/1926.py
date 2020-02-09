number = int(input())

tri = []
no = '369'
for i in range(1, number+1):
    clap = ''
    for j in str(i):
        if j in no:
            clap += '-'
    if clap:
        tri.append(clap)
    else:
        tri.append(str(i))
print(' '.join(tri))