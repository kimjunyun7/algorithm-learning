'''
    CodeUp
    Pyhon 기초 100제 - 81번
'''

n = int(input(), 16)

for i in range (1, 16):
    print("%X*%X=%X" %(n, i, (n*i)))
