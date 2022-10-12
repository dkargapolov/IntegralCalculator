from tkinter import *
  
  
def numberIntegration():  
    getMethod = Label(window, text="Какой метод численного интегрирования вы выберите: ")  
    getMethod.grid(column=0, row=2)

    m1 = Button(window, text="Метод прямоугольников левых частей", command=getAlgorithm)  
    m1.grid(column=1, row=2)

    m2 = Button(window, text="Метод прямоугольников правых частей", command=getAlgorithm)  
    m2.grid(column=2, row=2)

    m3 = Button(window, text="Метод трапеций", command=getAlgorithm)  
    m3.grid(column=3, row=2)

    m4 = Button(window, text="Метод парабол", command=getAlgorithm)  
    m4.grid(column=4, row=2)

def getAlgorithm():
    algorithmTitle = Label(window, text="Выберите алгоритм работы: ")  
    algorithmTitle.grid(column=0, row=4)

    a1 = Button(window, text="Алгоритм с постоянным шагом")  
    a1.grid(column=1, row=4)

    a2 = Button(window, text="Алгоритм с переменным шагом")  
    a2.grid(column=2, row=4)

  
window = Tk()  
window.title("Интегральный калькулятор")  
window.geometry('1000x1000')  
getType = Label(window, text="Выберите тип задачи:")  
getType.grid(column=0, row=0)

getType = Label(window, text=" ")  
getType.grid(column=0, row=1)  

getType = Label(window, text=" ")  
getType.grid(column=0, row=3)

getType = Label(window, text=" ")  
getType.grid(column=0, row=5)  

NI = Button(window, text="Численное интегрирование", command=numberIntegration)  
NI.grid(column=1, row=0)

window.mainloop()