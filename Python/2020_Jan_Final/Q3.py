def q2(num):
    if (num % 10) % 2 == 0:
        if (num % 100) % 3 == 0:
            if num % 4 == 0:
                return True
    return False
        
print(q2(512))
print(q2(384))
print(q2(321))  # 3의 배수기만 함
print(q2(100))
print(q2(311))
print(q2(520))  # 3의 배수가 아님
print(q2(102))  # 2의 배수 + 전체가 3의 배수 + 4의 배수가 아님
print(q2(120))  # 2의 배수 + 전체가 3의 배수 + 4의 배수
print(q2(354))  # 2의 배수 + 3의 배수 + 4의 배수가 아님
print(q2(460))  # 다맞는데 마지막 0
print(q2(400))  # 다맞는데 0, 00