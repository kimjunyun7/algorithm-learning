'''
    CodeUp
    Pyhon 기초 100제 - 64번
'''

a, b, c = [int(i) for i in input().split()]
d = (a if(a < b) else b) if ((a if (a < b) else b) < c) else c
print(d)
