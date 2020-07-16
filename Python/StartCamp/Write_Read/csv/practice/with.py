# 만약 파일을 열고 닫히기 전에 예외가 발생한다면
# 파일이 정상적으로 
csvfile = open(..)
...
...
csvfile.close()

# 해결방법1
csvfile = open(..)
...
...
finally:
    csvfile.close()

# with 문을 이용하면 더 간단하게 구현할 수 있다.
# with 문의 범위를 벗어날 때(with 문이 끝났을 때),
# 혹은 with 안에서 예외가 발생하더라도 파일종료를 보장한다.
with open('test.csv','w') as csvfile:
    ...
    ...