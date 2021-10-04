T = int(input())

for tc in range(1, T+1):
    N,E = input().split()
    N,E,L = list(N), int(E), len(N)
    now, big = 0, '0'

    while E and big == '0':
        for i in range(now, L):
            if N[now] < N[i]:
                if big < N[i]:
                    big = N[i]
                    bigs = [i]
                elif big == N[i]:
                    bigs.append(i)
        if big != '0':
            if E < len(bigs):
                N[now], N[bigs[-E]] = N[bigs[-E]], N[now]
            else:
                N[now], N[bigs[0]] = N[bigs[0]], N[now]
            big = '0'
            E -= 1
        now += 1
        if now > L:
            break
    if len(N) == len(set(N)) and E%2:
        N[-1], N[-2] = N[-2], N[-1]
    print('#{} {}'.format(tc, ''.join(N)))



# 완전탐색
# def back_track(k):                      # k -> 교환 횟수
#     global ans
#     val = int(''.join(cards))           # 숫자 카드
#     if val in visited[k]:               # 이미 체크 했다면 종료
#         return
#     visited[k].add(val)                 # 아니라면 해당 카드 조합을 추가
#     print(visited)
#     if k == cnt:                        # 모든 카드를 교환 했다면(주어진 횟수만큼 교환)
#         ans = max(ans, val)             # 최대 금액을 갱신
#     else:
#         # 카드 조합 -> 최댓값 갱신
#         for i in range(num_of_cards-1):
#             for j in range(i+1, num_of_cards):
#                 cards[i], cards[j] = cards[j], cards[i]  # 변경하고
#                 back_track(k+1)                          # 다음 확인
#                 cards[i], cards[j] = cards[j], cards[i]  # 원복
#
# import sys
# sys.stdin = open('input.txt')
# T = int(input())
# for tc in range(1, T+1):
#     arr = list(input().split())
#     cards, cnt = list(arr[0]), int(arr[1])      # cards: 카드 목록, cnt: 최대 교환 횟수
#     num_of_cards = len(cards)                   # 카드 숫자(최대 자릿수 6)
#     visited = [set() for _ in range(cnt+1)]     # 최대 10회 교환 -> 체크한 숫자 조합 파악 -> set을 활용한 중복 제거
#     ans = 0
#     back_track(0)                               # 0번부터 시작
#     print('#{} {}'.format(tc, ans))