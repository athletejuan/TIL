N,M = map(int, input().split())
queue = [x for x in range(1, N+1)]
nums = list(map(int, input().split()))
total = 0

while M:
    for num in nums:
        count = 0
        while True:
            if queue[0] == num:
                queue.pop(0)
                if count > N-count:
                    count = N-count
                total += count
                N -= 1
                M -= 1
                break
            else:
                queue.append(queue.pop(0))
                count += 1
print(total)