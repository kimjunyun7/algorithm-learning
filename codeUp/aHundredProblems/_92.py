'''
    CodeUp
    Pyhon 기초 100제 - 92번
'''

n = int(input())
a = [int(i) for i in input().split()]

d = []
for i in range(24) :
  d.append(0)

for i in range(n) :
  d[a[i]] += 1

for i in range(1, 24) :
  print(d[i], end=' ')