'''
    CodeUp
    Pyhon 기초 100제 - 70번
'''

a = int(input())
if(a%11==1 or a%11==2):
    print('winter')
if(a//3==1):
    print('spring')
if(a in [6, 7, 8]):
    print('summer')
if(a in [9, 10, 11]):
    print('fall')