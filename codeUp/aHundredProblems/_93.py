'''
    CodeUp
    Pyhon 기초 100제 - 93번
'''

n = int(input())
a = [int(i) for i in input().split()]


for i in range(len(a)-1, -1, -1) :
  print(a[i], end=' ')