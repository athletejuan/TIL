T = int(input())

if T%10:
    print(-1)
else:
    print(f'{T//300} {T%300//60} {T%300%60//10}')