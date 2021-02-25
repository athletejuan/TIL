T = int(input())

for tc in range(1, T+1):
    l = 0
    arr = []
    col = ''
    for _ in range(5):
        row = list(input())
        # 행의 최대 길이를 저장
        if len(row) > l:
            l = len(row)
        arr.append(row)
    for i in range(l):
        for j in range(5):
            # 행의 첫번째 항목들을 꺼내면서 col 문자열에 추가, 더이상 꺼낼 글자가 없는 행은 조건문으로 skip
            if arr[j]:
                col += arr[j].pop(0)
    print('#{} {}'.format(tc, col))