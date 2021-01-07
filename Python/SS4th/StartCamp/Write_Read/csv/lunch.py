import csv

lunch = {
    '양자강': '02-566-8116',
    '김밥카페': '02-553-3181',
    '순남시래기': '02-508-0887',
}

# csvfile = open('lunch.csv','w', encoding='utf-8', newline='')
# csv_writer = csv.writer(csvfile)
# for item, number in lunch.items():
#     csv_writer.writerow([item, number])
# csvfile.close()

with open('lunch.csv', 'w', encoding='utf-8', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    for item in lunch.items():
        csv_writer.writerow(item)