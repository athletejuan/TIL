import os

# print(os.listdir())
# os.rename('night.py','hello.py')
# print(os.listdir())

# os.system('touch a.txt')
os.chdir('report')

# 100 revival
# for i in range(100):
#     os.system(f'touch report{i}.txt')

files = os.listdir()
for name in files:
    os.rename(name, name.replace('samsung_', 'ssafy_'))

print(files)
# a = 'hello ssafy'
# print(a.replace('hello','hell'))