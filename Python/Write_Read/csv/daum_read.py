import csv

with open('daum_rank.csv', 'r', encoding='utf-8', newline='') as csvfile:
    # print(csvfile)
    reader = csv.DictReader(csvfile)
    # print(reader)
    for row in reader:
        # print(row)
        print(row['rank'], row['ranker'])