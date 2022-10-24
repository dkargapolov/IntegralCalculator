from math import *

a = int(input('Введите a: '))
b = int(input('Введите b: '))
n = int(input('Введите n: '))
formula = input('Введите интеграл: ')

def f(x):
    return eval(formula)

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

def Left_Rect_per(a, b, n):
    E = float(input('Введите точность: '))
    IN = 0
    I2N = 0
    R = 1
    h = (b - a) / n

    while(R > E):
        sum = 0
        x = a + h

        while(x <= b):
            temp = f(x)
            sum += temp
            x += h
    
        I2N = h * sum
        R = abs(I2N - IN)
        IN = I2N
        h = h / 2
    
    return I2N

print('Выберите тип задачи:\n1.Численное интегрирование')
print('Введите число:')

type = int(input())
match type:
    case 1:
        print('Какой метод численного интегрирования вы выберите: '
              '\n 1.Метод прямоугольников левых частей '
              '\n 2.Метод прямоугольников правых частей '
              '\n 3.Метод трапеций '
              '\n 4.Метод парабол')
        print('Введите число:')
        method = int(input())
        match method:
            case 1:
                print('Вы выбрали метод прямоугольников левых частей')
                print('Выберите алгоритм работы: \n 1.Алгоритм с постоянным шагом \n 2.Алгоритм с переменным шагом')
                print('Введите число')
                algorithm = int(input())
                match algorithm:
                    case 1:
                        print('Вы выбрали алгоритм с постоянным шагом')
                        print(Left_Rect(a, b, n))
                    case 2:
                        print('Вы выбрали алгоритм с переменным шагом')
                        print(Left_Rect_per(a, b, n))
            case 2:
                print('Вы выбрали метод прямоугольников правых частей')
                print('Выберите алгоритм работы: \n 1.Алгоритм с постоянным шагом \n 2.Алгоритм с переменным шагом')
                print('Введите число')
                algorithm = int(input())
                match algorithm:
                    case 1:
                        print('Вы выбрали алгоритм с постоянным шагом')
                        print(Right_Rect(a, b, n))
                    case 2:
                        print('Вы выбрали алгоритм с переменным шагом')
            case 3:
                print('Вы выбрали метод трапеций')
                print('Выберите алгоритм работы: \n 1.Алгоритм с постоянным шагом \n 2.Алгоритм с переменным шагом')
                print('Введите число')
                algorithm = int(input())
                match algorithm:
                    case 1:
                        print('Вы выбрали алгоритм с постоянным шагом')
                        print(Trapeze(a, b, n))
                    case 2:
                        print('Вы выбрали алгоритм с переменным шагом')
            case 4:
                print('Вы выбрали метод парабол')
                print('Выберите алгоритм работы: \n 1.Алгоритм с постоянным шагом \n 2.Алгоритм с переменным шагом')
                print('Введите число')
                algorithm = int(input())
                match algorithm:
                    case 1:
                        print('Вы выбрали алгоритм с постоянным шагом')
                        print(Parabol(a, b, n))
                    case 2:
                        print('Вы выбрали алгоритм с переменным шагом')