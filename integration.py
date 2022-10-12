from math import *


a = 1
b = 2
n = 1000


def f(x):
    return sin(x)

def Left_Rect(a, b, n):
    h = (b - a) / n
    sum = 0
    for i in range(n - 1):
        sum += h * f(a + i * h)

    return sum

def Right_Rect(a, b, n):
    h = (b - a) / n
    sum = 0
    for i in range(1, n):
        sum += h * f(a + i * h)

    return sum

def Trapeze(a, b, n):
    h = (b - a) / n
    sum = f(a) + f(b)
    for i in range(1, n - 1):
        sum += 2 * f(a + i * h)
    
    sum *= h / 2
    return sum

def Parabol(a, b, n):
    h = (b - a) / n
    sum = f(a) + f(b)
    for i in range(1, n - 1):
        k = 2 + 2 * (i % 2)
        sum += k * f(a + i * h)
    
    sum *= h / 3
    return sum

print(Left_Rect(a, b, n))
print(Right_Rect(a, b, n))
print(Trapeze(a, b, n))
print(Parabol(a, b, n))

# 300 icq updates (do not use!)

eps = 0.001
k = 10
i = 0
while True:
    i += 1
    diff = abs(Left_Rect(a, b, k * i) - Left_Rect(a, b, k * (i + 1)))
    if diff < eps:
        break

print(' /// ')
print(k * (i + 1))
print(Left_Rect(a, b, k * (i + 1)))
