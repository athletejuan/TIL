resists = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
resist = 0

resist += resists.index(input())*10
resist += resists.index(input())
resist *= 10**resists.index(input())
print(resist)