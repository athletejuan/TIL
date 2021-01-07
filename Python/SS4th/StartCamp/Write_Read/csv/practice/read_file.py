import csv

# 1. split
print('# split')
with open('dust.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print('1.', line)           # 개행문자 포함
        print('2.', line.strip())   # 개행문자 제거
        print('3.', line.strip().split(','))
        print('==============')
print()

# 2. csv.reader
print('# csv.reader')
with open('dust2.csv', 'r', encoding='utf-8') as f:
    items = csv.reader(f)
    for item in items:
        print(item)
print()

# 3. csv.DictReader
print('# csv.DictReader')
with open('dust3.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        print(row['city'], row['dust'])
