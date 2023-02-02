'''
    CodeUp
    Pyhon 기초 100제 - 74번
'''

a = ord(input())
for n in range(a+1-ord('a')):
    print(chr(n+ord('a')), end=' ')
