T = int(input())

data = input()
num_list = sorted([int(num) for num in data.split()])
print(num_list[(T//2)])