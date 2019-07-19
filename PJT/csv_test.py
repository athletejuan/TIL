lunch = {
    '진가와':'01012345678',
    '대우식당':'01011111111',
    '바스버거':'0221334442',
    '고갯마루':'03212332422'    
}

# lunch.csv 데이터를 저장
# with open('lunch.csv','w',encoding='utf-8') as f:
#     for k,v in lunch.items():
#         f.write(f'{k},{v} \n')

# # ',' join을 통해 string 만들기
# with open('lunch.csv','w',encoding='utf-8') as f:
#     for item in lunch.items():
#         f.write(','.join(item)+'\n')

# csv writer
import csv

with open('lunch.csv','w',encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)
    for item in lunch.items():
        csv_writer.writerow(item)

# 4. DictWriter
with open('student.csv','w',encoding='utf-8', newline='') as f:
    fieldnames = ['name','major']

    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name':'juan', 'major':'engineering'})
    writer.writerow({'name':'jason','major':'math'})


    with open('boxoffice.csv','w',encoding='utf-8') as f:
    for k,v in res.items():
        f.write(f'{k},{v} \n')