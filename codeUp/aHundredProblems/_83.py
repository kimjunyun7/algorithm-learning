'''
    CodeUp
    Pyhon 기초 100제 - 83번
'''

r, g, b = input().split()
r, g, b = int(r), int(g), int(b)
s = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print('%i %i %i' %(i, j, k))
            s += 1
print(s)
