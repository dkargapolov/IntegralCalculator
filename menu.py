from webbrowser import get
from integration import *
from multipleIntegration import *
from math import *


print('Выберите тип задачи:'
      '\n 1. Численное интегрирование'
      '\n 2. Кратный интеграл')

type = int(input('Введите число: '))

match type:
    case 1:
        getFormula()
        
        a = int(input('Введите нижний предел: '))
        b = int(input('Введите верхний предел: '))
        n = int(input('Введите количество разбиений: '))

        print('\nКакой метод численного интегрирования вы выберите: '
              '\n 1. Метод прямоугольников левых частей '
              '\n 2. Метод прямоугольников правых частей '
              '\n 3. Метод трапеций '
              '\n 4. Метод парабол')

        method = int(input('Введите число: '))
        match method:
            case 1:
                print('\nВы выбрали метод прямоугольников левых частей')
                print('\nВыберите алгоритм работы: '
                      '\n 1. Алгоритм с постоянным шагом' 
                      '\n 2. Двойной пересчёт'
                      '\n 3. Двойной пересчёт с отступами')

                algorithm = int(input('Введите число: '))
                match algorithm:
                    case 1:
                        print('\nВы выбрали алгоритм с постоянным шагом')
                        print(f'\nРезультат: {left(a, b, n)}')
                    case 2:
                        print('\nВы выбрали двойной пересчёт')
                        print(f'\nРезультат: {doubleRecLeft(a, b, n)}')
                    case 3:
                        print('\nВы выбрали двойной пересчёт с отступами')
                        print(f'\nРезультат: {doubleRec2Left(a, b, n)}')
            case 2:
                print('\nВы выбрали метод прямоугольников правых частей')
                print('\nВыберите алгоритм работы: '
                      '\n 1. Алгоритм с постоянным шагом' 
                      '\n 2. Двойной пересчёт'
                      '\n 3. Двойной пересчёт с отступами')

                algorithm = int(input('Введите число: '))
                match algorithm:
                    case 1:
                        print('\nВы выбрали алгоритм с постоянным шагом')
                        print(f'\nРезультат: {right(a, b, n)}')
                    case 2:
                        print('\nВы выбрали двойной пересчёт')
                        print(f'\nРезультат: {doubleRecRight(a, b, n)}')
                    case 3:
                        print('\nВы выбрали двойной пересчёт с отступами')
                        print(f'\nРезультат: {doubleRec2Right(a, b, n)}')
            case 3:
                print('\nВы выбрали метод трапеций')
                print('\nВыберите алгоритм работы: '
                      '\n 1. Алгоритм с постоянным шагом' 
                      '\n 2. Двойной пересчёт'
                      '\n 3. Двойной пересчёт с отступами')
                algorithm = int(input('Введите число: '))
                match algorithm:
                    case 1:
                        print('\nВы выбрали алгоритм с постоянным шагом')
                        print(f'\nРезультат: {trap(a, b, n)}')
                    case 2:
                        print('\nВы выбрали двойной пересчёт')
                        print(f'\nРезультат: {doubleRecTrap(a, b, n)}')
                    case 3:
                        print('\nВы выбрали двойной пересчёт с отступами')
                        print(f'\nРезультат: {doubleRec2Trap(a, b, n)}')
            case 4:
                print('\nВы выбрали метод парабол')
                print('\nВыберите алгоритм работы: '
                      '\n 1. Алгоритм с постоянным шагом' 
                      '\n 2. Двойной пересчёт'
                      '\n 3. Двойной пересчёт с отступами')

                algorithm = int(input('Введите число: '))
                match algorithm:
                    case 1:
                        print('\nВы выбрали алгоритм с постоянным шагом')
                        print(f'\nРезультат: {trap(a, b, n)}')
                    case 2:
                        print('\nВы выбрали двойной пересчёт')
                        print(f'\nРезультат: {doubleRecTrap(a, b, n)}')
                    case 3:
                        print('\nВы выбрали двойной пересчёт с отступами')
                        print(f'\nРезультат: {doubleRec2Trap(a, b, n)}')