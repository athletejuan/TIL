T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = input().split()
    front, back, link = [], [], []
    for idx, d in enumerate(nums):
        if idx%2:
            back.append(d)
        else:
            front.append(d)
    while front:
        for idx, f in enumerate(front):
            if not link:
                if f not in back:
                    link.append(front.pop(idx))
                    link.append(back.pop(idx))
            else:
                if f == link[-1]:
                    link.append(front.pop(idx))
                    link.append(back.pop(idx))
    print(f'#{tc} {" ".join(link)}')