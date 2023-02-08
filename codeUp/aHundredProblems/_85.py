'''
    CodeUp
    Pyhon 기초 100제 - 85번
'''

w, h, b = input().split()
w, h, b = int(w), int(h), int(b)
result = w * h * b / 8 / 1024 / 1024
print(f"{result:.2f} MB")