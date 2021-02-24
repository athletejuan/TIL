dy = [1, -1]

for _ in range(10):
    tc = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 도착지점 기준으로 위로 올라가도록 정의, 이동거리를 담아둘 리스트 생성
    start, short = [], []
    # 도착지점들을 start list에 추가
    for i in range(100):
        if ladder[99][i] == 1:
            start.append([99,i])
    for s in start:
        # 여러 도착지점에서 출발지점까지의 이동거리를 체크해야 하기때문에 ladder 안에서 숫자를 변경할 수 없음.
        # 이동 중 지나간 곳을 체크하기 위해 0으로 초기화된 visited list 생성
        visited = [[0] * 100 for j in range(100)]
        # 이동 거리 초기화
        dis = 0
        way = [s]

        while True:
            x,y = way.pop()
            # 이동시 거리 1씩 추가
            dis += 1
            if not x:
                short.append([dis, y])
                break
            # visited 의 현재위치를 1로 수정하여 다시 지나가지 않도록
            visited[x][y] = 1
            for j in range(2):
                if 0 <= y+dy[j] < 100 and ladder[x][y+dy[j]] and not visited[x][y+dy[j]]:
                    way.append([x,y+dy[j]])
                    break
            else:
                way.append([x-1,y])
    # 이동거리가 동일한 경로가 있는 경우에는 x좌표가 큰 값을 출력하기위해 lambda 함수로 이동거리 기준 오름차순, x좌표 기준 내림차순으로 정렬 후 결과 출력
    print('#{} {}'.format(tc, sorted(short, key=lambda x:(x[0], -x[1]))[0][1]))
    # 이렇게 해도 답은 동일(이동거리가 동일한 케이스 없음)
    # print('#{} {}'.format(tc, min(short)[1]))


# 1st try
# for _ in range(1, 11):
#     T = input()
#     dx = [1, -1]
#     ladder = []
#     visited = [[0]*100 for _ in range(100)]
#     checked = [[0]*100 for _ in range(100)]
#     q = []
#     for _ in range(100):
#         ladder.append(list(map(int, input().split())))
#     for i in range(100):
#         if ladder[0][i]:
#             q.append((0,i))
#     dis = {}
#     while q:
#         y,x = q.pop()
#         if not y:
#             s = x
#         elif y == 99:
#             dis[visited[99][x]] = s
#             checked = [[0]*100 for _ in range(100)]
#             continue
#         for j in range(2):
#             nx = x+dx[j]
#             if 0 <= nx < 100:
#                 if ladder[y][nx] and not checked[y][nx]:
#                     q.append((y, nx))
#                     checked[y][x] = 1
#                     visited[y][nx] = visited[y][x] + 1
#                     print('side', visited[y][nx])
#                     break
#         else:
#             q.append((y+1, x))
#             visited[y+1][x] = visited[y][x] + 1
#             print('down', y+1, visited[y+1][x])

#     print(f'#{T} {dis[min(dis.keys())]}')