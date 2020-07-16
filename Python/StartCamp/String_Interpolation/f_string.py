name = '홍길동'
print(f'안녕하세요, {name}입니다.')

import random
menu = ['김밥천국','스타벅스','부대찌개']
lunch = random.choice(menu)
print(f'오늘의 점심은 {lunch}입니다.')

numbers = range(1,46)
lotto = random.sample(numbers, 6)
print(f'오늘의 행운의 번호는 {sorted(lotto)} 입니다.')
