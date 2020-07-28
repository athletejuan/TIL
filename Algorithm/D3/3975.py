T = int(input())

# for test_case in range(1, T+1):
#     A,L,B,O = map(int, input().split())
#     if A*O > L*B:
#         print(f'#{test_case} ALICE')
#     elif A*O < L*B:
#         print(f'#{test_case} BOB')
#     else:
#         print(f'#{test_case} DRAW')

# answer???
result = []
for test_case in range(1, T+1):
    A,L,B,O = map(int, input().split())
    if A*O > L*B:
        result.append('ALICE')
    elif A*O < L*B:
        result.append('BOB')
    else:
        result.append('DRAW')
for idx, who in enumerate(result, start=1):
    print(f'#{idx} {who}')