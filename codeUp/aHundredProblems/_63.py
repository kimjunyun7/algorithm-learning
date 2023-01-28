'''
    CodeUp
    Pyhon 기초 100제 - 63번
'''

a, b = [int(i) for i in input().split()]
c = (a if(a >= b) else b)
print(c)
