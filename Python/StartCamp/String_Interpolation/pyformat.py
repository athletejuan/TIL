name = '홍길동'
english_name = 'hong'
print('안녕하세요, {}입니다. My name is {}'.format(name, english_name))
#=> '안녕하세요, 홍길동입니다. My name is hong'

print('안녕하세요, {1}입니다. My name is {0}'.format(name, english_name))
#=> '안녕하세요, hong입니다. My name is 홍길동'

print('안녕하세요, {1}입니다. My name is {1}'.format(name, english_name))
#=> '안녕하세요, hong입니다. My name is hong'