import csv

lunch = {
    '양자강': '02-566-8116',
    '김밥카페': '02-553-3181',
    '순남시래기': '02-508-0887',
}

# 먼저 파일을 열어야 함
# open() 내장함수로 해당 파일을 열고 파일 객체를 만든다
# csvfile = open('lunch_ex.csv', 'w', newline='', encoding='utf-8')
# csv_writer = csv.writer(csvfile)
# for item, number in lunch.items():
#     csv_writer.writerow([item, number])
# # csv_writer.writerow(['스팸','햄'])
# # csv_writer.writerow(['밥','계란'])
# # csv_writer.writerow(['밥','계란'])
# # 파일 조작이 끝나면 반드시 닫아야 한다.
# csvfile.close()

# with문 사용
with open('lunch_ex.csv', 'w', encoding='utf-8', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    for item, number in lunch.items():
        csv_writer.writerow([item, number])


# csvfile = open('lunch_01.csv', 'w', encoding='utf-8', newline='')
# csv_writer = csv.writer(csvfile)
# for item, number in lunch.items():
#     csv_writer.writerow([item, number])
# csvfile.close()

# with open('lunch_01.csv', 'w', encoding='utf-8', newline='') as csvfile:
#     csv_writer = csv.writer(csvfile)
#     for item in lunch.items():
#         csv_writer.writerow(item)