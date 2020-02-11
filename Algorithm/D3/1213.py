for t in range(1, 11):
    test_case = input()
    search = input()
    text = input()
    count = 0
    for i in range(len(text)-len(search)+1):
        if text[i:i+len(search)] == search:
            count += 1
        print(text[i:i+len(search)])
    print(f'#{test_case} {count}')