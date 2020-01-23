import random
with open('4ban.txt', 'r') as f:
    ssafy_4ban = f.read().split()
    random.shuffle(ssafy_4ban)
    print(ssafy_4ban)
    print("문\t\tscreen\t\t강사\n")
    cnt = 0
    for i in range(len(ssafy_4ban)-2):
        if cnt == 2:
            print(" | ", end=" ")
        elif cnt == 5:
            print("\n")
            cnt = 0
        print(ssafy_4ban[i], end=" ")
        cnt += 1
    print(f'\n\n{ssafy_4ban[-2]} {ssafy_4ban[-1]}')
    print()