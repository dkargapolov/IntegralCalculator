from math import *

# Получение выражения для пользовательского интерфейса
def tkGetFformula(smth):
    global fformula
    fformula = smth

# Получение выражения для консольного меню
def getFformula():
    global fformula 
    fformula = input('\nВведите выражение: ')

# воспроизведение выражения
def ff(x, y):
    return eval(fformula)

# Метод левых прямоугольников
def mLeft(a, b, c, d, nx, ny):
    sumX = 0
    hx = (b - a) / nx
    hy = (d - c) / ny
    x = a

    while(x <= b - hx):
        sumY = 0
        y = c
        while(y <= d - hy):
            sumY += ff(x,y)
            y += hy
        iY = sumY * hy
        sumX += iY
        x += hx
    
    return hx * sumX

# Метод правых прямоугольников
def mRight(a, b, c, d, nx, ny):
    sumX = 0
    hx = (b - a) / nx
    hy = (d - c) / ny
    x = a + hx

    while(x <= b):
        sumY = 0
        y = c + hy
        while(y <= d):
            sumY += ff(x,y)
            y += hy
        iY = sumY * hy
        sumX += iY
        x += hx
    
    return hx * sumX

# Метод трапеций
def mTrap(a, b, c, d, nx, ny):
    sumX = 0
    hx = (b - a) / nx
    hy = (d - c) / ny
    x = a + hx

    while(x <= b - hx):
        sumY = 0
        y = c + hy
        while(y <= d - hy):
            sumY += ff(x,y)
            y += hy
        ffc = ff(x, c)
        ffd = ff(x, d)
        iY = hy * ((ffc + ffd) / 2 + sumY)
        sumX += iY
        x += hx
    
    ffa = ff(a, y)
    ffb = ff(b, y)

    return hx * ((ffa + ffb) / 2 + sumX)

# Метод парабол
def mSimp(a, b, c, d, nx, ny):
    sumX = 0
    sumX2 = 0
    hx = (b - a) / nx
    hy = (d - c) / ny
    x = a + hx

    while(x <= b - hx):
        sumY = 0
        sumY2 = 0
        y = c + hy
        while(y <= d - hy):
            sumY += ff(x,y)
            y += hy
            sumY2 += ff(x,y)
            y += hy
        ffc = ff(x, c)
        ffd = ff(x, d)
        iY = (hy/3) * (ffc + ffd + 4*sumY + 2*sumY2)
        sumX += iY
        x += hx
        sumX2 += iY
        x += hx
    
    ffa = ff(a, y)
    ffb = ff(b, y)

    return (hx / 3) * (ffa + ffb + 4*sumX + 2*sumX2)
