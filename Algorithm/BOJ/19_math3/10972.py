N = int(input())
nums = list(map(int, input().split()))

for i in range(N-1):
    if nums[N-i-1] > nums[N-i-2]:
        front,back = nums[:N-i-1], nums[N-i-1:]
        out = front.pop()
        back.sort()
        for b in range(len(back)):
            if out < back[b]:
                ins = back.pop(b)
                break
        front.append(ins)
        back.append(out)
        back.sort()
        print(' '.join(list(map(str, front+back))))
        break
else:
    print(-1)