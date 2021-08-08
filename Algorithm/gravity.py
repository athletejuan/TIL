T = int(input())

for tc in range(1, T+1):
    width = int(input())
    heights = map(int, input().split())

    drop = {}
    for idx, height in enumerate(heights):
        for box in range(height):
            if box not in drop:
                drop[box] = width - idx - 1
            else:
                drop[box] -= 1

    max_drop = 0
    for dist in drop.values():
        if max_drop < dist:
            max_drop = dist
    print('#{} {}'.format(tc, max_drop))