for test_case in range(1, 11):
    le = int(input())
    if le == 1:
        print(f'#{test_case} 64')
    count = 0
    para = []
    for i in range(8):
        row = input()
        para.extend(row.split())
        for j in range(9-le):
            if row[j:j+le] == row[j:j+le][::-1]:
                count += 1
    for l in range(8):
        for m in range(9-le):
            col = []
            for n in range(m, m+le):
                col.append(para[n][l])
            print(col)
            if col == col[::-1]:
                count += 1
    print(f'#{test_case} {count}')