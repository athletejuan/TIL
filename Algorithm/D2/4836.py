T = int(input())

for tc in range(1, T+1):
    arr = [[0]*10 for _ in range(10)]
    num = int(input())
    red, blue = [], []
    count = 0
    for i in range(num):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                arr[r][c] += color
                if arr[r][c] == 3:
                    count += 1
    #             if color%2:
    #                 red.append((x,y))
    #             else:
    #                 blue.append((x,y))
    # for j in red:
    #     if j in blue:
    #         count += 1
    print('#{} {}'.format(tc, count))


# Tony
# import sys
# sys.stdin = open('input.txt', 'r')


# def paint_box(r1, c1, r2, c2, color_number):
#     for row in range(r1, r2 + 1):
#         for col in range(c1, c2 + 1):
#             field[row][col] += color_number


# def calculated_result():
#     result = 0
#     for row_data in field:
#         for col_data in row_data:
#             if col_data == 3:
#                 result += 1
#     return result


# T = int(input())

# for t in range(1, T+1):
#     N = int(input())
#     field = [[0] * 10 for _ in range(10)]
#     # 1. 색칠하기
#     for _ in range(N):
#         r1, c1, r2, c2, color_number = map(int, input().split())
#         paint_box(r1, c1, r2, c2, color_number)

#     # 2. 색칠한 결과 계산하기
#     print('#{} {}'.format(t, calculated_result()))