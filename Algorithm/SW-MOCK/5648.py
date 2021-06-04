T = int(input())

for tc in range(1, T+1):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]
    energy = 0

    for i in atoms:
        i[0] *= 2
        i[1] *= 2
    for _ in range(4000):
        for a in atoms:
            if a[2] == 0:
                a[1] += 1
            elif a[2] == 1:
                a[1] -= 1
            elif a[2] == 2:
                a[0] -= 1
            else:
                a[0] += 1
        if a[0] > 2000 or a[0] < -2000 or a[1] > 2000 or a[1] < -2000:
            atoms.remove(a)
        if len(atoms) < 2:
            break
        for i in atoms:
            poss = 0
            crush = 0
            temp = [i]
            for j in atoms:
                if i[2] != j[2]:
                    poss = 1
                if i[0] == j[0] and i[1] == j[1] and i[2] != j[2]:
                    energy += j[3]
                    temp.append(j)
                    crush = 1
            if crush:
                energy += i[3]
                for k in temp:
                    atoms.remove(k)
            if not poss:
                atoms.remove(i)
        # for k in atoms:
        #     for l in atoms:
        #         if l != k:
        #             if l[0] == k[0] or l[1] == k[1]:
        #                 poss = 1
        #     if not poss:
        #         atoms.remove(k)
    print('#{} {}'.format(tc, energy))