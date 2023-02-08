'''
    CodeUp
    Pyhon 기초 100제 - 87번
'''

value = int(input())
for i in range(1, value+1):
    if i%3 == 0:
        continue
    print(i, end=' ')