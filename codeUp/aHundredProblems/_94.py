'''
    CodeUp
    Pyhon 기초 100제 - 94번
'''

n = int(input())
a = [int(i) for i in input().split()]
smallest = a[0]

for i in a :
  if i < smallest:
    smallest = i
print(smallest)