#1. Pass function to argument
def my_func(func):
    return func

def my_argument_func():
    return 'Hello My Func!'

result = my_func(my_argument_func)
print(result) # <function my_argument_func at 0x1103d9560>
print(result()) # Hello My Func!


#2. map
numbers = [0, 9, 99]

def plus_one(num):
    return num + 1

print(list(map(plus_one, numbers))) # [1, 10, 100]