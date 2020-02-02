T = int(input())
data = input()

num_list = []
data2 = data.split()
for test_case in data2:
    num_list.append(int(test_case))
num_list = sorted(num_list)
print(num_list[T//2])