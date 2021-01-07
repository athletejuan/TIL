lunch = {
    '양자강': '02-566-8116',
    '김밥카페': '02-553-3181',
    '순남시래기': '02-508-0887',
}

# 1. string formatting
with open('csv_conversion.csv', 'w', encoding='utf-8', newline='') as f:
    for key, value in lunch.items():
        # \n 없이 진행하는 거 보여주고 변환
        f.write(f'{key}, {value}\n')

# 2. join method
with open('csv_conversion.csv', 'w', encoding='utf-8', newline='') as f:
    for item in lunch.items():
        # print(item) -> ('양자강': '02-566-8116') -> tuple
        f.write(', '.join(item)+'\n')

# 3. csv.writer -> 각 행별로 알아서 한줄씩 쓰여짐
import csv

with open('csv_conversion.csv', 'w', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)
    for item in lunch.items():
        csv_writer.writerow(item)