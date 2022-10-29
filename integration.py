from math import *

def getFormula():
    global formula 
    formula = input('\nВведите выражение: ')

def f(x):
    return eval(formula)

def left(a,b,n):
    s = 0
    h = (b - a) / n
    x = a

    while (x <= (b - h)):
        s += f(x)
        x += h

    result = h * s
    return result

def right(a,b,n):
    s = 0
    h = (b - a) / n
    x = a + h

    while (x <= b):
        s += f(x)
        x += h

    result = h * s
    return result

def trap(a,b,n):
    s = 0
    h = (b - a) / n
    x = a + h

    while (x <= b):
        s += f(x)
        x += h

    result = h * ((f(a) + f(b)) / 2 + s)
    return result

def simp(a,b,n):
    s1 = 0
    s2 = 0
    h = (b - a) / n / 2

    x = a + h
    while (x <= b):
        s1 += f(x)
        x += 2 * h

    x = a + 2 * h
    while (x <= (b - h)):
        s2 += f(x)
        x += 2 * h

    result = h / 3 * (f(a) + f(2 * b) + 4 * s1 + 2 * s2)
    return result

def doubleRecLeft(a,b,n):
    In = 0
    I2n = 0
    R = 1

    E = 0.0001

    while (R > E):
        S2 = 0
        h = (b - a) / n
        x = a
        while (x <= (b - h)):
            S2 += f(x)
            x += h
        I2n = h * S2
        R = abs(I2n - In)
        In = I2n
        h = h / 2

    return I2n

def doubleRecRight(a,b,n):
    In = 0
    I2n = 0
    R = 1

    E = 0.0001

    while (R > E):
        S2 = 0
        h = (b - a) / n
        x = a + h
        while (x <= b):
            S2 += f(x)
            x += h
        I2n = h * S2
        R = abs(I2n - In)
        In = I2n
        h = h / 2

    return I2n

def doubleRecTrap(a,b,n):
    In = 0
    I2n = 0
    R = 1

    E = 0.0001

    while (R > E):
        S2 = 0
        h = (b - a) / n
        x = a + h
        while (x <= b):
            S2 += f(x)
            x += h
        I2n = h * ((f(a) + f(b)) / 2 + S2)
        R = abs(I2n - In)
        In = I2n
        h = h / 2

    return I2n

def doubleRecSimp(a,b,n):
    In = 0
    I2n = 0
    R = 1

    E = 0.0001

    while (R > E):
        S2_1 = 0
        S2_2 = 0
        h = (b - a) / n / 2

        x = a + h

        while (x <= b):
            S2_1 += f(x)
            x += 2 * h

        x = a + 2 * h

        while(x <= (b - h)):
            S2_2 += f(x)
            x += 2 * h

        I2n = h / 3 * (f(a) + f(2 * b) + 4 * S2_1 + 2 * S2_2)
        R = abs(I2n - In)
        In = I2n
        h = h / 2

    return I2n

def doubleRec2Left(a,b,n):
    E = 0.0001
    hv = (b - a) / n #h
    hs = a #x
    hd = hv
    I1 = 0
    R = 1
    x = a

    while R > E:
        x = hs
        s = 0
        while x <= (b - hv):
            s += f(x)
            x += hd #h
        I2 = hd * s #result
        R = abs(I1 - I2)
        I1 = I2
        if hd == hv:
            hd = hv / 2
            hv /= 4
        else:
            hd = hv
            hs = hd / 2
            hv /= 2

    return I2

def doubleRec2Right(a,b,n):
    E = 0.0001
    hv = (b - a) / n #h
    hs = a #x
    hd = hv
    I1 = 0
    R = 1
    x = a + hv

    while R > E:
        x = hs + hv
        s = 0
        while x <= b:
            s += f(x)
            x += hd #h
        I2 = hd * s #result
        R = abs(I1 - I2)
        I1 = I2
        if hd == hv:
            hd = hv / 2
            hv /= 4
        else:
            hd = hv
            hs = hd / 2
            hv /= 2

    return I2

def doubleRec2Trap(a,b,n):
    E = 0.0001
    hv = (b - a) / n #h
    hs = a #x
    hd = hv
    I1 = 0
    R = 1
    x = a + hv

    while R > E:
        x = hs + hv
        s = 0
        while x <= b:
            s += f(x)
            x += hd #h
        I2 = hd * ((f(a) + f(b)) / 2 + s) #result
        R = abs(I1 - I2)
        I1 = I2
        if hd == hv:
            hd = hv / 2
            hv /= 2
        else:
            hd = hv
            hs = hd / 2
            #hv /= 2

    return I2

def doubleRec2Simp(a,b,n):
    E = 0.0001
    hv = (b - a) / n / 2 #h
    hs = a #x
    hd = hv
    I1 = 0
    R = 1
    x = a + hv

    while R > E:
        x = hs + hv
        s1 = 0
        s2 = 0
        while x <= b:
            s1 += f(x)
            x += 2 * hd #h

        x = a + 2 * hd
        while (x <= (b - hv)):
            s2 += f(x)
            x += 2 * hd

        I2 = hd / 3 * (f(a) + f(2 * b) + 4 * s1 + 2 * s2) #result
        R = abs(I1 - I2)
        I1 = I2
        if hd == hv:
            hd = hv / 2
            hv /= 2
        else:
            hd = hv
            hs = hd / 2
            #hv /= 2

    return I2
