days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
m,d = map(int, input().split())

print(days[(sum(month[:m])+d)%7])