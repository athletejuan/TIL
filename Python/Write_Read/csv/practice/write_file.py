import csv

dust_list = [
    {'city': '서울', 'dust': 59},
    {'city': '대전', 'dust': 56},
    {'city': '광주', 'dust': 38},
    {'city': '구미', 'dust': 69},
]

# 1. string formatting
with open('dust.csv', 'w', encoding='utf-8', newline='') as f:
    for dust in dust_list:
        f.write('{},{}\n'.format(dust['city'], dust['dust']))

# 2. csv.writer
with open('dust2.csv', 'w', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)

    for dust in dust_list:
        print(dust)
        print(dust.values())
        csv_writer.writerow(dust.values())

# 3. csv.DictWriter
with open('dust3.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ('city', 'dust')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for dust in dust_list:
        writer.writerow(dust)

    # or
    # writer.writerows(dust_list)