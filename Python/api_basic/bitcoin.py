import requests
from pprint import pprint as pp

url = 'https://api.bithumb.com/public/ticker/all'
bithumb = requests.get(url).json()['data']

# for key,value in bithumb.items():
#     if type(value) == type(dict()):
#         now = float(value['closing_price'])
#         start = float(value['opening_price'])
#         if now - start > 0:
#             print(f'{key}: 상승장')
#         else:
#             print(f'{key}: 하락장')
#     else:
#         continue


# import copy

# a = [1, [2], 3, 4]
# b = copy.deepcopy(a)

# b[1].append(5)
# b[1][0] = 7
# print(a == b)

a = [ [] ] * 10
b = [ [] for _ in range(10) ]
# a[4].append(5)
# b[5].append(9)
print(a)
print(b)