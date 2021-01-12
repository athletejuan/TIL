import random

menu = ['새마을식당', '초원삼겹살', '홍콩반점']
print(menu)

lunch = random.choice(menu)
print(lunch)

phone_book = {'새마을식당': '1234-1234', '초원삼겹살': '2345-2345', '홍콩반점': '3456-3456'}

print(phone_book[lunch])