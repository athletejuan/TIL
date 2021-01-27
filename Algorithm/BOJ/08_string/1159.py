N = int(input())
player = {}
starting = ''

for _ in range(N):
    name = input()
    if name[0] not in player:
        player[f'{name[0]}'] = 1
    else:
        player[f'{name[0]}'] += 1

for key, count in player.items():
    if count > 4:
        starting += key
if starting:
    print(''.join(sorted(starting)))
else:
    print('PREDAJA')