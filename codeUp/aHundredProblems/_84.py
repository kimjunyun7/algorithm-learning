'''
    CodeUp
    Pyhon 기초 100제 - 84번
'''

h, b, c, s = input().split()
h, b, c, s = int(h), int(b), int(c), int(s)
result = h * b * c * s / 8 / 1024 / 1024
print(f"{result:.1f} MB")
