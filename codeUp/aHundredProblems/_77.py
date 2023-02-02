'''
    CodeUp
    Pyhon 기초 100제 - 77번
'''

a = int(input())
sum = 0
for i in range(a+1):
    if i % 2 == 0:
        sum += i
print(sum)
