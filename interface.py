from tkinter import *
from tkinter import messagebox
from integration import *
from multipleIntegration import *

def calculate(): 
    x = option.get()
    match x:
        case 1:
            heightx = heighttxt.get()
            widthx = widthtxt.get()
            lengthx = lengthtxt.get()
            expthx = exptxt.get()

            height = float(heightx)
            width = float(widthx)
            length = float(lengthx)
            tkGetFormula(expthx)

            y = method.get()
            match y:
                case 1:

                    z = algorithm.get()
                    match z:
                        case 1:
                            result = f'Результат: {left(height, width, length)}'
                            reslbl = Label(rec_frame, text=result, padx=5, pady=5)
                            reslbl.grid(column=1, row=5)
                        case 2:
                            result = f'Результат: {doubleRecLeft(height, width, length)}'
                            reslbl = Label(rec_frame, text=result, padx=5, pady=5)
                            reslbl.grid(column=1, row=5)
                        case 3:
                            result = f'Результат: {doubleRec2Left(height, width, length)}'
                            reslbl = Label(rec_frame, text=result, padx=5, pady=5)
                            reslbl.grid(column=1, row=5)
                case 2:

                    z = algorithm.get()
                    match z:
                        case 1:
                            result = f'Результат: {right(height, width, length)}'
                            reslbl = Label(rec_frame, text=result, padx=5, pady=5)
                            reslbl.grid(column=1, row=5)
                        case 2:
                            result = f'Результат: {doubleRecRight(height, width, length)}'
                            reslbl = Label(rec_frame, text=result, padx=5, pady=5)
                            reslbl.grid(column=1, row=5)
                        case 3:
                            result = f'Результат: {doubleRec2Right(height, width, length)}'
                            reslbl = Label(rec_frame, text=result, padx=5, pady=5)
                            reslbl.grid(column=1, row=5)
                case 3:

                    z = algorithm.get()
                    match z:
                        case 1:
                            result = f'Результат: {trap(height, width, length)}'
                            reslbl = Label(rec_frame, text=result, padx=5, pady=5)
                            reslbl.grid(column=1, row=5)
                        case 2:
                            result = f'Результат: {doubleRecTrap(height, width, length)}'
                            reslbl = Label(rec_frame, text=result, padx=5, pady=5)
                            reslbl.grid(column=1, row=5)
                        case 3:
                            result = f'Результат: {doubleRec2Trap(height, width, length)}'
                            reslbl = Label(rec_frame, text=result, padx=5, pady=5)
                            reslbl.grid(column=1, row=5)
                case 4:

                    z = algorithm.get()
                    match z:
                        case 1:
                            result = f'Результат: {simp(height, width, length)}'
                            reslbl = Label(rec_frame, text=result, padx=5, pady=5)
                            reslbl.grid(column=1, row=5)
                        case 2:
                            result = f'Результат: {doubleRecSimp(height, width, length)}'
                            reslbl = Label(rec_frame, text=result, padx=5, pady=5)
                            reslbl.grid(column=1, row=5)
                        case 3:
                            result = f'Результат: {doubleRec2Simp(height, width, length)}'
                            reslbl = Label(rec_frame, text=result, padx=5, pady=5)
                            reslbl.grid(column=1, row=5)

        case 2:
            mheightx = mheighttxt.get()
            mwidthx = mwidthtxt.get()
            mlengthx = mlengthtxt.get()
            mexpthx = mexptxt.get()
            mctx = mctxt.get()
            mdtx = mdtxt.get()
            mlengthYtx = mlengthYtxt.get()

            height = float(mheightx)
            width = float(mwidthx)
            length = float(mlengthx)
            c = float(mctx)
            d = float(mdtx)
            lengthY = float(mlengthYtx)
            tkGetFformula(mexpthx)

            y = method.get()
            match y:
                case 1:
                    result = f'Результат: {mLeft(height, width, c, d, length, lengthY)}'
                    mreslbl = Label(sphere_frame, text=result, padx=5, pady=5)
                    mreslbl.grid(column=1, row=5)
                case 2:
                    result = f'Результат: {mRight(height, width, c, d, length, lengthY)}'
                    mreslbl = Label(sphere_frame, text=result, padx=5, pady=5)
                    mreslbl.grid(column=1, row=5)
                case 3:
                    result = f'Результат: {mTrap(height, width, c, d, length, lengthY)}'
                    mreslbl = Label(sphere_frame, text=result, padx=5, pady=5)
                    mreslbl.grid(column=1, row=5)
                case 4:
                    result = f'Результат: {mSimp(height, width, c, d, length, lengthY)}'
                    mreslbl = Label(sphere_frame, text=result, padx=5, pady=5)
                    mreslbl.grid(column=1, row=5)

def recprism():
    sphere_frame.grid_forget()
    rec_frame.grid(row=1, column=0)


def sphere():
    rec_frame.grid_forget()
    sphere_frame.grid(row=1, column=0)

window = Tk() 

window.title("Интегралы")
window.geometry('820x300')

option = IntVar()

Radiobutton(window, text="Численное интегрирование", variable=option, value=1, command=recprism).grid(column=0, row=0)
Radiobutton(window, text="Кратные интегралы", variable=option, value=2, command=sphere).grid(column=1, row=0)

rec_frame = Frame(window)
sphere_frame = Frame(window)

method = IntVar()
algorithm = IntVar()

blanklbl = Label(rec_frame, text=" ", padx=5, pady=5)
heightlbl = Label(rec_frame, text="Введите a: ", padx=5, pady=5) 
widthlbl = Label(rec_frame, text="Введите b: ", padx=5, pady=5)
lengthlbl = Label(rec_frame, text="Введите n: ", padx=5, pady=5)
explbl = Label(rec_frame, text="Введите выражение: ", padx=5, pady=5)
mlbl = Label(rec_frame, text="Метод:", padx=5, pady=5)
alglbl = Label(rec_frame, text="Алгоритм:", padx=5, pady=5)

mblanklbl = Label(sphere_frame, text=" ", padx=5, pady=5)
mheightlbl = Label(sphere_frame, text="Введите a: ", padx=5, pady=5) 
mwidthlbl = Label(sphere_frame, text="Введите b: ", padx=5, pady=5)
mclbl = Label(sphere_frame, text="Введите c: ", padx=5, pady=5)
mdlbl = Label(sphere_frame, text="Введите d: ", padx=5, pady=5)
mlengthlbl = Label(sphere_frame, text="Введите nX: ", padx=5, pady=5)
mlengthYlbl = Label(sphere_frame, text="Введите nY: ", padx=5, pady=5)
mexplbl = Label(sphere_frame, text="Введите выражение: ", padx=5, pady=5)
mmlbl = Label(sphere_frame, text="Метод:", padx=5, pady=5)


leftbtn = Radiobutton(rec_frame, text="Левых прямоугольников", variable=method, value=1)
rightbtn = Radiobutton(rec_frame, text="Правых прямоугольников", variable=method, value=2)
trapbtn = Radiobutton(rec_frame, text="Трапеций", variable=method, value=3)
simpbtn = Radiobutton(rec_frame, text="Симпсона", variable=method, value=4)

mleftbtn = Radiobutton(sphere_frame, text="Левых прямоугольников", variable=method, value=1)
mrightbtn = Radiobutton(sphere_frame, text="Правых прямоугольников", variable=method, value=2)
mtrapbtn = Radiobutton(sphere_frame, text="Трапеций", variable=method, value=3)
msimpbtn = Radiobutton(sphere_frame, text="Симпсона", variable=method, value=4)

perbtn = Radiobutton(rec_frame, text="Переменный шаг", variable=algorithm, value=1)
drbtn = Radiobutton(rec_frame, text="Двойной пересчёт", variable=algorithm, value=2)
dr2btn = Radiobutton(rec_frame, text="Двойной пересчёт с отступами", variable=algorithm, value=3)

exptxt = Entry(rec_frame, width=20)
heighttxt = Entry(rec_frame, width=10) 
widthtxt = Entry(rec_frame, width=10)
lengthtxt = Entry(rec_frame, width=10)

mexptxt = Entry(sphere_frame, width=20)
mheighttxt = Entry(sphere_frame, width=10) 
mwidthtxt = Entry(sphere_frame, width=10)
mlengthtxt = Entry(sphere_frame, width=10)
mctxt = Entry(sphere_frame, width=10)
mdtxt = Entry(sphere_frame, width=10)
mlengthYtxt = Entry(sphere_frame, width=10)

calcbtn = Button(rec_frame, text="Вычислить", command=calculate, padx=5, pady=5) 
mcalcbtn = Button(sphere_frame, text="Вычислить", command=calculate, padx=5, pady=5) 

blanklbl.grid(column=0, row=0)
heightlbl.grid(column=0, row=1)
widthlbl.grid(column=0, row=2)
lengthlbl.grid(column=0, row=3)
explbl.grid(column=0, row=4)
mlbl.grid(column=2, row=0)
alglbl.grid(column=3, row=0)

mblanklbl.grid(column=0, row=0)
mheightlbl.grid(column=0, row=1)
mwidthlbl.grid(column=0, row=2)
mlengthlbl.grid(column=0, row=3)
mexplbl.grid(column=0, row=4)
mmlbl.grid(column=4, row=0)

mclbl.grid(column=2, row=1)
mdlbl.grid(column=2, row=2)
mlengthYlbl.grid(column=2, row=3)

mctxt.grid(column=3, row=1)
mdtxt.grid(column=3, row=2)
mlengthYtxt.grid(column=3, row=3)

leftbtn.grid(column=2, row=1)
rightbtn.grid(column=2, row=2)
trapbtn.grid(column=2, row=3)
simpbtn.grid(column=2, row=4)

mleftbtn.grid(column=4, row=1)
mrightbtn.grid(column=4, row=2)
mtrapbtn.grid(column=4, row=3)
msimpbtn.grid(column=4, row=4)

perbtn.grid(column=3, row=1)
drbtn.grid(column=3, row=2)
dr2btn.grid(column=3, row=3)


heighttxt.grid(column=1, row=1)
widthtxt.grid(column=1, row=2)
lengthtxt.grid(column=1, row=3)
exptxt.grid(column=1, row=4)

mheighttxt.grid(column=1, row=1)
mwidthtxt.grid(column=1, row=2)
mlengthtxt.grid(column=1, row=3)
mexptxt.grid(column=1, row=4)

calcbtn.grid(column=0, row=5)
mcalcbtn.grid(column=0, row=5)

window.mainloop()