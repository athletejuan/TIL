n = int(input())
k = int(input())
nums = set()

def pick(cards, picked, toPick):
    if not toPick:
        num = ''
        for j in picked:
            num += cards[j]
        nums.add(num)

    for i in range(n):
        if i not in picked:
            picked.append(i)
            pick(cards, picked, toPick - 1)
            picked.pop()

cards = [input() for _ in range(n)]

pick(cards, [], k)
print(len(nums))