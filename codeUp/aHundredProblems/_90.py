'''
    CodeUp
    Pyhon 기초 100제 - 90번
'''

a, m, d, n = input().split()
a, m, d, n = int(a), int(m), int(d), int(n)
s = a
for i in range(n-1):
    s = s * m + d
print(s)